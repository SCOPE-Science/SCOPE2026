#!/usr/bin/env python3
from collections import Counter
from itertools import product

def partitions(n, minimum=1):
    if n == 0:
        yield []
        return
    for first in range(minimum, n + 1):
        for rest in partitions(n - first, first):
            yield [first] + rest

def lower_witness(parts):
    c = Counter(parts)
    smax = max(parts)
    mmax = max(c.values())
    M = max(smax, mmax)
    if smax == M:
        q = list(parts)
        q[q.index(smax)] = smax + 1
        return sorted(q), M
    s = next(s for s, m in c.items() if m == M)
    return sorted(list(parts) + [s]), M

def capped_signature(parts, k):
    c = Counter(parts)
    exact = [min(k, c.get(s, 0)) for s in range(1, k)]
    large = min(k, sum(m for s, m in c.items() if s >= k))
    return tuple(exact + [large])

def eq_structure(parts):
    out = []
    for ci, size in enumerate(parts):
        out.extend([ci] * size)
    return out

def partial_iso(state, Aclass, Bclass):
    active = [p for p in state if p[0] >= 0]
    for a, b in active:
        for aa, bb in active:
            if (a == aa) != (b == bb):
                return False
            if (Aclass[a] == Aclass[aa]) != (Bclass[b] == Bclass[bb]):
                return False
    return True

def duplicator_wins(partsA, partsB, k, max_states=200000):
    Aclass = eq_structure(partsA)
    Bclass = eq_structure(partsB)
    nA, nB = len(Aclass), len(Bclass)
    options = [(-1, -1)] + [(a, b) for a in range(nA) for b in range(nB)]
    if len(options) ** k > max_states:
        raise ValueError("state space too large")
    states = [s for s in product(options, repeat=k) if partial_iso(s, Aclass, Bclass)]
    winning = set(states)
    changed = True
    while changed:
        changed = False
        remove = []
        for st in list(winning):
            bad = False
            for idx in range(k):
                for a in range(nA):
                    if not any(tuple(list(st[:idx]) + [(a, b)] + list(st[idx+1:])) in winning for b in range(nB)):
                        bad = True
                        break
                if bad:
                    break
                for b in range(nB):
                    if not any(tuple(list(st[:idx]) + [(a, b)] + list(st[idx+1:])) in winning for a in range(nA)):
                        bad = True
                        break
                if bad:
                    break
            if bad:
                remove.append(st)
        if remove:
            changed = True
            for st in remove:
                winning.discard(st)
    empty = tuple([(-1, -1)] * k)
    return empty in winning

profile_cases = 0
for n in range(1, 13):
    for parts in partitions(n):
        witness, M = lower_witness(parts)
        assert capped_signature(parts, M) == capped_signature(witness, M)
        assert capped_signature(parts, M + 1) != capped_signature(witness, M + 1)
        profile_cases += 1

pebble_cases = 0
for n in range(1, 7):
    for parts in partitions(n):
        witness, M = lower_witness(parts)
        sizeM = (1 + len(eq_structure(parts)) * len(eq_structure(witness))) ** M
        if M <= 3 and sizeM < 200000:
            assert duplicator_wins(parts, witness, M)
            if M + 1 <= 3:
                size_next = (1 + len(eq_structure(parts)) * len(eq_structure(witness))) ** (M + 1)
                if size_next < 200000:
                    assert not duplicator_wins(parts, witness, M + 1)
            pebble_cases += 1

balanced_cases = 0
for r in range(1, 9):
    for s in range(1, 9):
        parts = [s] * r
        c = Counter(parts)
        width = 1 + max(max(parts), max(c.values()))
        assert width == max(r, s) + 1
        balanced_cases += 1

print(f"VERIFY_OK profile_cases={profile_cases} pebble_cases={pebble_cases} balanced_cases={balanced_cases}")
