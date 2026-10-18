"""Finite exhaustive checks for rooted starlike bounded-morphism enumeration.

No external packages needed. Run: python3 check_starlike.py
"""
from itertools import product
from math import comb


def frame(arms):
    vertices = [None] + [(i, s) for i, a in enumerate(arms) for s in range(1, a + 1)]
    def le(x, y):
        return x is None or (y is not None and x[0] == y[0] and x[1] <= y[1])
    return [[le(x, y) for y in vertices] for x in vertices]


def full_brute(src, dst):
    P, Q = frame(src), frame(dst)
    m, n = len(P), len(Q)
    count = 0
    # Fix root -> root, enumerate every map of the other worlds, independently
    # of the branchwise normal form being checked.
    for choices in product(range(1, n), repeat=m - 1):
        f = (0,) + choices
        if all({f[y] for y in range(m) if P[x][y]} ==
               {z for z in range(n) if Q[f[x]][z]} for x in range(m)):
            count += 1
    return count


def weights(src, dst):
    W = [[sum(comb(a - 1, d - 1) for d in range(1, min(a, b) + 1))
          for b in dst] for a in src]
    F = [[comb(a - 1, b - 1) if a >= b else 0
          for b in dst] for a in src]
    return W, F


def formula(src, dst):
    W, F = weights(src, dst)
    count = 0
    for subset in product((0, 1), repeat=len(dst)):
        term = 1
        for i in range(len(src)):
            term *= sum(W[i]) - sum(F[i][j] for j in range(len(dst)) if subset[j])
        count += (-1)**sum(subset) * term
    return count


def direct_candidate_defect_counts(src, dst):
    # Independently enumerate all nondecreasing maps on each arm, then keep
    # exactly those that have image a nonempty terminal interval of one arm.
    opts = []
    for a in src:
        local = []
        for j, b in enumerate(dst):
            for v in product(range(1, b + 1), repeat=a):
                if all(v[t] <= v[t + 1] for t in range(a - 1)) and \
                   set(v) == set(range(v[0], b + 1)):
                    local.append((j, v[0] == 1))
        opts.append(local)
    histogram = [0] * (len(dst) + 1)
    for combination in product(*opts):
        full = {j for j, flag in combination if flag}
        histogram[len(dst) - len(full)] += 1
    return histogram


def theoretical_defect_counts(src, dst):
    from math import comb as choose
    W, F = weights(src, dst)
    k = len(dst)
    # E[(Z)_s] counting non-surjective candidates, inverted to exact counts.
    subset_sums = [0] * (k + 1)
    for mask in product((0, 1), repeat=k):
        t = sum(mask)
        value = 1
        for i in range(len(src)):
            value *= sum(W[i]) - sum(F[i][j] for j in range(k) if mask[j])
        subset_sums[t] += value
    # subset_sums[t] is the sum of numbers with every member of S uncovered.
    # Binomial inversion of binom(Z,t) gives exact histogram of Z.
    return [sum((-1)**(t-z)*choose(t, z)*subset_sums[t] for t in range(z, k+1))
            for z in range(k+1)]


def main():
    ntests = 0
    nprofile = 0
    for nr in (1, 2, 3):
        for nk in (2, 3):
            for src in product((1, 2, 3), repeat=nr):
                for dst in product((1, 2), repeat=nk):
                    if sum(src) + 1 > 7 or sum(dst) + 1 > 6:
                        continue
                    direct = full_brute(src, dst)
                    algebraic = formula(src, dst)
                    assert direct == algebraic, (src, dst, direct, algebraic)
                    ntests += 1
                    if sum(src) <= 6 and nr <= 3:
                        observed = direct_candidate_defect_counts(src, dst)
                        expected = theoretical_defect_counts(src, dst)
                        assert observed == expected, (src, dst, observed, expected)
                        assert expected[0] == algebraic
                        nprofile += 1
    print('VERIFY_OK', ntests, 'rooted-frame exact checks;',
          nprofile, 'independent complete defect-profile checks')
    for a, b in [((2, 2), (2, 2)), ((2, 2, 2), (2, 2)),
                 ((3, 3), (2, 2)), ((3, 3, 3), (2, 2))]:
        print('example', a, b, formula(a, b))

if __name__ == '__main__':
    main()
