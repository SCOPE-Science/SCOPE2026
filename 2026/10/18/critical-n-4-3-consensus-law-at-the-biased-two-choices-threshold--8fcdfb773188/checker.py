"""Standalone checks for the critical biased two-choices consensus theorem.

Requires only the Python standard library. Finite checks are diagnostics, not
proof of the asymptotic theorem; its proof is in RESULT.md.
"""
from fractions import Fraction
from math import gamma, pi, sqrt, log


def transitions(n, k, modified=False):
    if not (n >= 3 and 0 <= k < n):
        raise ValueError((n, k))
    x = Fraction(k, n)
    a = Fraction(1, 9)
    denom = n if modified else n - 1
    up = (1 - x) * (a + (1 - a) * Fraction(k * k, denom * denom))
    down = x * (1 - a) * Fraction((n - k)**2, denom**2)
    return up, down


def differences_exact(n, modified=False):
    ans = []
    prev = Fraction(0)
    for k in range(n):
        up, down = transitions(n, k, modified)
        prev = (1 + down * prev) / up
        ans.append(prev)
    return ans


def independent_linear_equations(n, modified=False):
    # Solve the n-by-n absorbing hitting-time equations independently of
    # the difference recursion, by exact-rational Gaussian elimination.
    A = [[Fraction(0) for _ in range(n + 1)] for _ in range(n)]
    for k in range(n):
        up, down = transitions(n, k, modified)
        A[k][k] = up + down
        if k: A[k][k - 1] = -down
        if k < n - 1: A[k][k + 1] = -up
        A[k][n] = Fraction(1)
    for j in range(n):
        p = next(r for r in range(j, n) if A[r][j])
        A[p], A[j] = A[j], A[p]
        factor = A[j][j]
        A[j] = [v/factor for v in A[j]]
        for r in range(n):
            if r != j:
                factor = A[r][j]
                if factor:
                    A[r] = [a-factor*b for a,b in zip(A[r],A[j])]
    return [A[k][n] for k in range(n)]


def mean_all_float(n, modified=False):
    prev = 0.0
    d = []
    for k in range(n):
        x = k / n
        den = n if modified else n-1
        up = (1-x) * (1 + 8*(k/den)**2) / 9
        down = x*8*((n-k)/den)**2 / 9
        prev = (1 + down*prev) / up
        d.append(prev)
    v = 0.0
    for k in range(n-1,-1,-1):
        v+=d[k]
        d[k] = v
    return d


def constant():
    a = 32/9
    return (8/3) * sqrt(pi/(3*a)) * (4/a)**(1/6) * gamma(1/6)


def main():
    for n in range(3, 10):
        for modified in (True, False):
            ds = differences_exact(n, modified)
            expected = []
            total = Fraction(0)
            for di in reversed(ds):
                total += di
                expected.append(total)
            expected.reverse()
            independent = independent_linear_equations(n, modified)
            assert expected == independent, (n, modified)
            assert all(d > 0 for d in ds)
            for k in range(1, n):
                up, down = transitions(n, k, modified)
                assert up*ds[k]-down*ds[k-1] == 1
    C = constant()
    print('Exact absorbing-chain checks passed: sizes 3 through 9, both sampling rules')
    print('Predicted critical constant:', format(C, '.12f'))
    for n in (1000, 10000, 100000, 200000):
        e = mean_all_float(n)
        e0 = e[0] / n**(4/3)
        ec = e[n//4] / n**(4/3)
        efast = e[n//2] / (n*log(n))
        assert C < e0 < C+1.2
        assert 5.3 < ec < 7.0
        assert 1.0 < efast < 1.5
        print('n=%d initial-zero/n^(4/3)=%.9f threshold-start/n^(4/3)=%.9f high-start/(n log n)=%.9f' % (n,e0,ec,efast))
    print('Finite asymptotic sanity checks passed; only the analytic proof establishes limits')

if __name__ == '__main__':
    main()
