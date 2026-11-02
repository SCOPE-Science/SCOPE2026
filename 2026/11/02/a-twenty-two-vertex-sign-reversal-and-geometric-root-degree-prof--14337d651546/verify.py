"""Independent finite checks for the root-degree/outdegree-profile covariance law.
Run with Python 3.9+ (standard library only). Finite checks corroborate an all-size proof.
"""
from fractions import Fraction as F
from itertools import product


def recursion(N):
    # State at n=1: one root of outdegree zero.
    p, mu, cov = [F(1)], [F(1)], [F(0)]
    out = {1: (p, mu, cov)}
    for n in range(1, N):
        pp, mm, cc = [F(0)] * (n + 1), [F(0)] * (n + 1), [F(0)] * (n + 1)
        for k in range(n + 1):
            a = p[k] if k < len(p) else F(0)
            b = p[k - 1] if 0 < k <= len(p) else F(0)
            x = mu[k] if k < len(mu) else F(0)
            y = mu[k - 1] if 0 < k <= len(mu) else F(0)
            v = cov[k] if k < len(cov) else F(0)
            w = cov[k - 1] if 0 < k <= len(cov) else F(0)
            pp[k] = a + (b - a) / n
            mm[k] = x + int(k == 0) + (y - x) / n
            cc[k] = v + (w - v) / n + (b - a) / n - (y - x) / (n*n)
        p, mu, cov = pp, mm, cc
        out[n + 1] = (p, mu, cov)
    return out


def enumerate_recursive_trees(n):
    # Exhaust every parent array: parent(i) lies in {1,...,i-1}.
    sums = [0] * n
    sums_cross = [0] * n
    sum_root = 0
    count = 0
    for parents in product(*(range(i) for i in range(1, n))):
        deg = [0] * n
        for parent in parents:
            deg[parent] += 1
        d = deg[0]
        counts = [0] * n
        for child_count in deg:
            counts[child_count] += 1
        count += 1
        sum_root += d
        for k in range(n):
            sums[k] += counts[k]
            sums_cross[k] += d * counts[k]
    means = [F(a, count) for a in sums]
    covs = [F(a, count) - F(sum_root, count) * means[k]
            for k, a in enumerate(sums_cross)]
    return means, covs


def root_pgf(n, z):
    v = F(1)
    for t in range(1, n):
        v *= (F(t - 1) + z) / t
    return v


def profile_pgf(n, z):
    rho = root_pgf(n, z)
    assert z != 2
    return (n + (1-z)*rho) / (2-z)


def main():
    checks = 0
    hist = recursion(110)
    for n in range(1, 10):
        p, mu, cv = hist[n]
        assert sum(p) == 1
        assert sum(mu) == n
        assert sum(cv) == 0
        checks += 3
        for k in range(n):
            assert sum(p) == 1
            checks += 1
        if n >= 2:
            assert mu[0] == F(n, 2)
            assert cv[0] == F(n - 2, 2*(n - 1))
            checks += 2
        if n >= 3:
            H = sum((F(1, j) for j in range(1, n - 1)), F(0))
            target = (F(n, 4) - F(3, 2)*H - F(1, 2*(n-1))) / (n - 1)
            assert cv[1] == target
            checks += 1
        for z in (F(0), F(1, 2), F(3, 4), F(1), F(3, 2)):
            lhs = sum(mu[k] * z**k for k in range(len(mu)))
            assert lhs == profile_pgf(n, z)
            checks += 1
        if n >= 2:
            em, ec = enumerate_recursive_trees(n)
            for k in range(n):
                assert mu[k] == em[k], (n, k, 'mean')
                assert cv[k] == ec[k], (n, k, 'covariance')
                checks += 2
    for n in range(10, 111):
        _, mu, cv = hist[n]
        if n >= 3:
            H = sum((F(1, j) for j in range(1, n - 1)), F(0))
            f = F(n, 4) - F(3, 2)*H - F(1, 2*(n-1))
            assert cv[1] == f / (n - 1)
            assert (cv[1] > 0) == (n >= 22)
            checks += 2
        assert cv[0] == F(n - 2, 2*(n - 1))
        checks += 1
    assert hist[21][2][1] == F(-4997771, 1034633600)
    assert hist[22][2][1] == F(2470115, 651819168)
    checks += 2
    # Exact symbolic finite difference of the numerator:
    for n in range(7, 111):
        Hn = sum((F(1, j) for j in range(1, n - 1)), F(0))
        Hnp1 = Hn + F(1, n-1)
        Fn = F(n, 4) - F(3, 2)*Hn - F(1, 2*(n - 1))
        Fnp1 = F(n + 1, 4) - F(3, 2)*Hnp1 - F(1, 2*n)
        assert Fnp1 - Fn == F(n*n - 7*n + 2, 4*n*(n-1)) > 0
        checks += 1
    print('PASS', checks, 'exact assertions; full parent-array enumeration for sizes 1..9')
    print('unary covariance n=21:', hist[21][2][1], '; n=22:', hist[22][2][1])


if __name__ == '__main__':
    main()
