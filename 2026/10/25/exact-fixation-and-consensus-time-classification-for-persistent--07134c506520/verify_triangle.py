"""Exact reproducibility checks for the three-agent persistent-voter result.

Only Python 3 standard library is required. One update means one uniformly
selected ordered pair of distinct individuals.
"""
from fractions import Fraction as Q
from itertools import product
from math import comb


def update(state, focal, speaker):
    """Each entry is (opinion 0/1, zealot flag 0/1)."""
    old = state[focal]
    msg = state[speaker]
    next_state = list(state)
    next_state[focal] = (msg[0] if old[1] == 0 else old[0],
                         int(old[0] == msg[0]))
    next_state[speaker] = (msg[0], 1)
    return tuple(next_state)


def descriptors(state):
    opinions = [u for u, _ in state]
    k = sum(opinions)
    if k in (0, 3):
        return None
    minority = 1 if k == 1 else 0
    z = next(flag for u, flag in state if u == minority)
    m = sum(flag for u, flag in state if u != minority)
    return (minority, z, m)


def minority_fixation(z, m):
    return Q(105 + 36*z - (25 + 4*z)*m + comb(m, 2), 339)


def mean_updates(z, m):
    return Q(621 + 366*z + (105 + 3*z)*m - 87*comb(m, 2), 131)


def predicted_plus(state):
    info = descriptors(state)
    if info is None:
        return Q(int(state[0][0] == 1))
    minority, z, m = info
    h = minority_fixation(z, m)
    return h if minority == 1 else 1-h


def predicted_time(state):
    info = descriptors(state)
    return Q(0) if info is None else mean_updates(info[1], info[2])


def rational_solve(matrix, rhs):
    """Exact Gauss-Jordan, independent of the proposed closed formulas."""
    n = len(rhs)
    a = [list(row) + [rhs[i]] for i, row in enumerate(matrix)]
    for k in range(n):
        pivot = next((i for i in range(k, n) if a[i][k]), None)
        assert pivot is not None, 'Transient system is singular'
        a[k], a[pivot] = a[pivot], a[k]
        den = a[k][k]
        a[k] = [v / den for v in a[k]]
        for i in range(n):
            if i == k or not a[i][k]:
                continue
            c = a[i][k]
            a[i] = [x - c*y for x, y in zip(a[i], a[k])]
    return [row[-1] for row in a]


def main():
    labeled = [tuple((x // 2, x % 2) for x in state)
               for state in product(range(4), repeat=3)]
    checked_h = checked_t = 0
    for state in labeled:
        if descriptors(state) is None:
            continue
        neighbors = [update(state, i, j)
                     for i in range(3) for j in range(3) if i != j]
        h = sum((predicted_plus(s) for s in neighbors), Q()) / 6
        t = 1 + sum((predicted_time(s) for s in neighbors), Q()) / 6
        assert h == predicted_plus(state), (state, h)
        assert t == predicted_time(state), (state, t)
        checked_h += 1
        checked_t += 1
    assert checked_h == checked_t == 48
    assert len(labeled) == 64

    # Independent 12-orbit absorption-chain construction and elimination.
    group_states = [a for a in product(range(4), repeat=4) if sum(a) == 3]
    def counts(state):
        return tuple(sum(1 for opinion, confidence in state
                         if 2*opinion + confidence == k) for k in range(4))
    transients = [a for a in group_states if a[0]+a[1] not in (0, 3)]
    assert len(group_states) == 20 and len(transients) == 12
    index = {a:i for i,a in enumerate(transients)}
    mat = [[Q(int(i == j)) for j in range(12)] for i in range(12)]
    rh = [Q(0) for _ in range(12)]
    rt = [Q(1) for _ in range(12)]
    for i,a in enumerate(transients):
        state = tuple((k//2, k%2) for k in range(4) for _ in range(a[k]))
        for focal in range(3):
            for speaker in range(3):
                if focal == speaker: continue
                dest = update(state, focal, speaker)
                b = counts(dest)
                if b in index:
                    mat[i][index[b]] -= Q(1,6)
                elif all(u == 1 for u,_ in dest):
                    rh[i] += Q(1,6)
    solved_h = rational_solve(mat, rh)
    solved_t = rational_solve(mat, rt)
    for i,a in enumerate(transients):
        state = tuple((k//2, k%2) for k in range(4) for _ in range(a[k]))
        assert solved_h[i] == predicted_plus(state)
        assert solved_t[i] == predicted_time(state)
    assert minority_fixation(0,0) == Q(35,113)
    assert minority_fixation(1,0) == Q(47,113)
    assert minority_fixation(1,1) == Q(112,339)
    assert mean_updates(0,0) == Q(621,131)
    for z in (0,1):
        for m in range(3):
            p = minority_fixation(z,m)
            assert (p > Q(1,3)) == (z == 1 and m == 0)
            assert mean_updates(z,m) > 3
    print('PASS: 48 exact hitting-probability harmonic checks')
    print('PASS: 48 exact expected-time harmonic checks')
    print('PASS: independent 12-transient-orbit exact linear solves (two right sides)')
    print('PASS: 64 labeled states / 20 orbit states / six initial-configuration classes')
    print('PASS: 35/113, 47/113, 621/131, strict thresholds and slowdown')

if __name__ == '__main__':
    main()
