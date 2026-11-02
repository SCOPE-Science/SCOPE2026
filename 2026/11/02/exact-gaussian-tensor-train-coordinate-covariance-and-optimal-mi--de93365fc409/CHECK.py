"""Exact fourth-moment checks for real Gaussian tensor-train entries.

Reproducibility: python3 CHECK.py. Standard library only.
Finite checks corroborate, but do not substitute for, the stated proof.
"""
from fractions import Fraction as Q
from itertools import combinations, product


def kernel_closed(d, r, mismatches):
    """E[omega_I^2 omega_J^2], with mismatches indexed from zero."""
    mm = sorted(mismatches)
    c = Q(r + 2, r)
    if not mm:
        return 3 * c ** (d - 1)
    z = Q(r - 1, r + 2)
    value = c ** (d - 1)
    for a, b in zip(mm, mm[1:]):
        value *= (1 + 2 * z ** (b - a)) / 3
    return value


def kernel_transfer(d, r, mismatches):
    missing = set(mismatches)
    v = [Q(1) if (j == 0 or 0 not in missing) else Q(0) for j in range(3)]
    for position in range(1, d):
        u = [sum(v[i] * (Q(1) if i == j else Q(1, r))
                 for i in range(3)) for j in range(3)]
        v = u if position not in missing else [u[0], Q(0), Q(0)]
    return sum(v)


def fourth_wick(x):
    return (int(x[0] == x[1] and x[2] == x[3])
          + int(x[0] == x[2] and x[1] == x[3])
          + int(x[0] == x[3] and x[1] == x[2]))


def brute_gaussian(d, r, mismatches):
    """Independent Wick expansion, without the three-state transfer method."""
    I = (0,) * d
    J = tuple(int(j in mismatches) for j in range(d))
    paths = list(product(range(r), repeat=d - 1))
    total = 0
    for four_paths in product(paths, repeat=4):
        indices = (I, I, J, J)
        contribution = 1
        for j in range(d):
            variables = tuple((indices[t][j],
                               -1 if j == 0 else four_paths[t][j-1],
                               -1 if j == d-1 else four_paths[t][j])
                              for t in range(4))
            contribution *= fourth_wick(variables)
            if not contribution:
                break
        total += contribution
    return Q(total, r ** (2 * (d - 1)))


def theorem_bounds(d, r, k):
    c = Q(r + 2, r)
    if k == 0:
        m = 3 * c ** (d - 1)
        return m, m
    if k == 1:
        m = c ** (d - 1)
        return m, m
    if r == 1:
        m = 3 ** (d - k)
        return Q(m), Q(m)
    q, rem = divmod(d-1, k-1)
    z = Q(r-1, r+2)
    F = lambda gap: (1 + 2*z**gap)/3
    lower = c ** (d-1) * F(q)**(k-1-rem) * F(q+1)**rem
    upper = c ** (d-k)
    return lower, upper


def main():
    checks = 0
    for d, r in ((2,2),(3,2),(3,3),(4,2)):
        for mask in product((False,True), repeat=d):
            mm = tuple(j for j, flag in enumerate(mask) if flag)
            expected = kernel_closed(d,r,mm)
            assert kernel_transfer(d,r,mm) == expected
            assert brute_gaussian(d,r,mm) == expected
            checks += 2
    for d in range(2,10):
        for r in range(1,8):
            for mask in product((False,True), repeat=d):
                mm = tuple(j for j, flag in enumerate(mask) if flag)
                k = kernel_closed(d,r,mm)
                assert kernel_transfer(d,r,mm) == k
                assert k >= 1
                if len(mm) == d:
                    assert k == 1
                checks += 3
    for d in range(2,12):
        for r in range(1,9):
            for k in range(0,d+1):
                choices = [kernel_closed(d,r,x) for x in combinations(range(d),k)]
                low, high = theorem_bounds(d,r,k)
                assert min(choices) == low
                assert max(choices) == high
                checks += 2
    d,r=4,2
    diag = kernel_closed(d,r,())
    cluster = kernel_closed(d,r,(0,1))
    spread = kernel_closed(d,r,(0,3))
    assert (diag, cluster, spread) == (24, 4, Q(11,4))
    assert (2*(diag-1)+2*(cluster-1), 2*(diag-1)+2*(spread-1)) == (52,Q(99,2))
    checks += 2
    print('CHECKS_PASSED', checks)

if __name__ == '__main__':
    main()
