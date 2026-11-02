#!/usr/bin/env python3
"""Exact integer-only binary16 logistic-map state-graph census.

Run: python3 binary16_census.py
Option: python3 binary16_census.py --crosscheck
"""
from bisect import bisect_left
from collections import Counter
from fractions import Fraction
import hashlib
import json
import sys

D = 1 << 24
N = 0x3C01  # nonnegative IEEE-754 binary16 encodings <= 1, including +0


def scaled_binary16(code):
    assert 0 <= code < N
    exponent = code >> 10
    mantissa = code & 1023
    return mantissa if exponent == 0 else (1024 + mantissa) << (exponent - 1)


U = [scaled_binary16(code) for code in range(N)]
assert len(U) == 15361 and U[0] == 0 and U[-1] == D
assert all(U[i] < U[i + 1] for i in range(N - 1))


def round_scaled(numer, denom):
    """Nearest binary16 in [0,1], ties to even, for numer/(denom * 2**24)."""
    assert denom > 0 and 0 <= numer <= (D + 16384) * denom
    ix = bisect_left(U, (numer + denom - 1) // denom)
    if ix == 0:
        return 0
    if ix == N:
        return N - 1
    lower_gap = numer - U[ix - 1] * denom
    upper_gap = U[ix] * denom - numer
    assert lower_gap >= 0 and upper_gap >= 0
    if lower_gap < upper_gap:
        return ix - 1
    if lower_gap > upper_gap:
        return ix
    return ix if ix % 2 == 0 else ix - 1


def maps():
    staged = []
    single = []
    max_staged_numer = 0
    for u in U:
        y = U[round_scaled(D - u, 1)]  # first round 1-x
        max_staged_numer = max(max_staged_numer, 4 * u * y)
        staged.append(round_scaled(4 * u * y, D))  # round (4x)*y
        single.append(round_scaled(4 * u * (D - u), D))  # round 4x(1-x) once
    # Some staged products exceed one, but all lie below the exact
    # midpoint between 1 and its next representable binary16 number.
    assert max_staged_numer == D * (D + 8144)
    assert max_staged_numer < D * (D + 8192)
    return staged, single


def census(next_state):
    assert len(next_state) == N and all(0 <= z < N for z in next_state)
    done = [-1] * N
    steps = [0] * N
    cycles = []
    for start in range(N):
        if done[start] >= 0:
            continue
        seen = {}
        path = []
        v = start
        while done[v] < 0 and v not in seen:
            seen[v] = len(path)
            path.append(v)
            v = next_state[v]
        if v in seen:
            cycle = path[seen[v]:]
            cycle_id = len(cycles)
            cycles.append(cycle)
            for j in cycle:
                done[j] = cycle_id
        for j in reversed(path):
            if done[j] < 0:
                done[j] = done[next_state[j]]
                steps[j] = steps[next_state[j]] + 1
    basins = Counter(done)
    assert sum(basins.values()) == N
    assert all(next_state[cycle[t]] == cycle[(t + 1) % len(cycle)]
               for cycle in cycles for t in range(len(cycle)))
    assert all(steps[j] == 0 for cycle in cycles for j in cycle)
    assert all(steps[j] == steps[next_state[j]] + 1
               for j in range(N) if steps[j] != 0)
    return cycles, basins, max(steps), steps, done


def independent_census(next_state):
    """Independent Kahn peeling + cycle rotation; counts include all states."""
    from collections import deque
    indegree = [0] * N
    for j in next_state:
        indegree[j] += 1
    queue = deque(j for j in range(N) if indegree[j] == 0)
    peel_order = []
    while queue:
        v = queue.popleft()
        peel_order.append(v)
        w = next_state[v]
        indegree[w] -= 1
        if indegree[w] == 0:
            queue.append(w)
    labels = [-1] * N
    distances = [0] * N
    cycle_lengths = []
    for j in range(N):
        if indegree[j] and labels[j] == -1:
            cid = len(cycle_lengths)
            k = 0
            v = j
            while labels[v] == -1:
                assert indegree[v] > 0
                labels[v] = cid
                k += 1
                v = next_state[v]
            assert v == j
            cycle_lengths.append(k)
    for v in reversed(peel_order):
        labels[v] = labels[next_state[v]]
        distances[v] = 1 + distances[next_state[v]]
    assert all(k >= 0 for k in labels)
    basins = Counter(labels)
    return sorted((cycle_lengths[i], basins[i]) for i in range(len(cycle_lengths))), max(distances), sum(distances)


def digest(seq):
    return hashlib.sha256(b''.join(n.to_bytes(2, 'little') for n in seq)).hexdigest()


def report(label, next_state):
    cycles, basins, max_steps, steps, labels = census(next_state)
    results = [dict(period=len(c), basin=basins[i], representative=min(c),
                    orbit_from_rep=orbit_repr(min(c), next_state, len(c)))
               for i, c in enumerate(cycles)]
    results.sort(key=lambda x: (x['period'], x['representative']))
    return dict(name=label, nodes=N, cycles=results, maximum_transient_steps=max_steps,
                transition_sha256_le16=digest(next_state),
                total_transient_steps=sum(steps)), cycles, basins, labels


def orbit_repr(z, nxt, k):
    out = []
    for _ in range(k):
        out.append(z)
        z = nxt[z]
    assert z == out[0]
    return out


def crosscheck(staged, single):
    import numpy as np
    for code in range(N):
        x = np.asarray(np.uint16(code)).view(np.float16)
        with np.errstate(all='ignore'):
            a = np.float16(np.float16(np.float16(4) * x) * np.float16(np.float16(1) - x))
            # High-precision comparison is not the proof for single rounding;
            # explicitly compute a rational with the stdlib below.
        aa = int(np.asarray(a).view(np.uint16))
        assert aa == staged[code], ('staged', code, aa, staged[code])
        q = Fraction(4 * U[code] * (D - U[code]), D * D)
        candidate = single[code]
        actual = Fraction(U[candidate], D)
        diff = abs(q - actual)
        for other in (candidate - 1, candidate + 1):
            if 0 <= other < N:
                dist = abs(q - Fraction(U[other], D))
                assert diff <= dist
                assert diff != dist or candidate % 2 == 0
    print('Independent NumPy staged and rational single-rounded checks: 15,361 each PASS')


def main():
    staged, single = maps()
    if '--crosscheck' in sys.argv:
        crosscheck(staged, single)
    a, ca, ba, la = report('rounded_after_each_operation', staged)
    b, cb, bb, lb = report('rounded_once_after_exact_polynomial', single)
    for seq, r in ((staged, a), (single, b)):
        independently, longest, sumdist = independent_census(seq)
        assert independently == sorted((c['period'], c['basin']) for c in r['cycles'])
        assert longest == r['maximum_transient_steps']
        assert sumdist == r['total_transient_steps']
    atoms_a = {}
    atoms_b = {}
    for reportitem, bsn, atomdict in ((a, ba, atoms_a), (b, bb, atoms_b)):
        for c in reportitem['cycles']:
            for z in c['orbit_from_rep']:
                atomdict[z] = Fraction(c['basin'], N * c['period'])
    overlaps = sorted(set(atoms_a) & set(atoms_b))
    tv = 1 - sum((min(atoms_a[z], atoms_b[z]) for z in overlaps), Fraction(0))
    assert sum(atoms_a.values()) == sum(atoms_b.values()) == 1
    expected = {
        'rounded_after_each_operation': [(1, 5092, 0), (1, 2, 14848), (40, 10267, 7678)],
        'rounded_once_after_exact_polynomial': [(1, 15236, 0), (1, 8, 14848), (5, 117, 11709)],
    }
    for r in [a, b]:
        assert [(c['period'], c['basin'], c['representative']) for c in r['cycles']] == expected[r['name']]
    assert a['maximum_transient_steps'] == 83 and b['maximum_transient_steps'] == 109
    assert overlaps == [0, 14848]
    assert tv == Fraction(10267, 15361), (tv, overlaps)
    print(json.dumps({'staged':a,'single':b,
                      'common_cycle_codes': overlaps,
                      'cesaro_total_variation':str(tv),
                      'decimal_tv':float(tv)},indent=2))
    print('ALL EXACT ASSERTIONS PASSED')

if __name__ == '__main__': main()
