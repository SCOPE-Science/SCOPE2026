"""Exact rational checks for the discrete noisy-voter shock theorems.

Uses only Python's standard library. Run: python verify.py
Finite tests are corroboration, not proofs of the all-parameter claims.
"""
from fractions import Fraction as F


def mat_base(n, eta):
    e = F(eta)
    p = [[F(0) for _ in range(n + 1)] for _ in range(n + 1)]
    for j in range(n + 1):
        up = F(n - j, n) * (e + (1 - e) * F(j, n))
        down = F(j, n) * (e + (1 - e) * F(n - j, n))
        p[j][j] = 1 - up - down
        if j < n:
            p[j][j + 1] = up
        if j > 0:
            p[j][j - 1] = down
        assert sum(p[j]) == 1 and all(x >= 0 for x in p[j])
    return p


def solve(a, b):
    m = len(a)
    z = [[F(q) for q in a[i]] + [F(b[i])] for i in range(m)]
    for j in range(m):
        pivot = next(i for i in range(j, m) if z[i][j])
        z[j], z[pivot] = z[pivot], z[j]
        fac = z[j][j]
        z[j] = [x / fac for x in z[j]]
        for i in range(m):
            if i != j:
                fac = z[i][j]
                if fac:
                    z[i] = [u - fac * v for u, v in zip(z[i], z[j])]
    return [z[i][-1] for i in range(m)]


def stationary(n, eta, r, k):
    p = mat_base(n, eta)
    r = F(r)
    q = [[(1-r)*p[i][j] + (r if j == k else 0)
          for j in range(n+1)] for i in range(n+1)]
    a = [[q[i][j]-(1 if i == j else 0) for i in range(n+1)]
         for j in range(n)]
    a.append([F(1)]*(n+1))
    b = [F(0)]*n+[F(1)]
    pi = solve(a, b)
    assert sum(pi) == 1 and all(x > 0 for x in pi)
    assert all(sum(pi[i]*q[i][j] for i in range(n+1)) == pi[j]
               for j in range(n+1))
    return pi


def four_ratios(eta, r):
    e, r = F(eta), F(r)
    aa = (1-r)*(3+e)/(16*(r+(1-r)*e))
    bb = F(4, 1)/(1+e)*(r/(1-r)+(3+5*e)/8-e*aa)
    return aa, bb


def green(n, k, j):
    assert 1 <= k < n and 1 <= j < n
    if j <= k:
        return F(n*(n-k), n-j)
    return F(n*k, j)


def triple_peaks(pi, k):
    maxima = [j for j in range(len(pi)) if
              (j == 0 or pi[j] > pi[j-1]) and
              (j == len(pi)-1 or pi[j] > pi[j+1])]
    return maxima == [0, k, len(pi)-1]


def main():
    count = 0
    for den in [5, 10, 20, 50, 100]:
        for num in range(1, den):
            eta = F(num, den)
            for rd in [10, 25, 50, 100]:
                for rn in range(1, rd):
                    r = F(rn, rd)
                    if r >= 1:
                        continue
                    pi = stationary(4, eta, r, 2)
                    aa, bb = four_ratios(eta, r)
                    assert pi[0] == aa*pi[1] and pi[2] == bb*pi[1]
                    q = ((14-23*eta+5*eta*eta)*r*r +
                         (2+24*eta-10*eta*eta)*r + eta*(5*eta-1))
                    prediction = (0 < eta < F(1, 5) and
                                  (3-15*eta)*(1-r) > 16*r and q > 0)
                    assert triple_peaks(pi, 2) == prediction
                    count += 1
    example = stationary(4, F(1, 10), F(1, 25), 2)
    assert example == [F(z,1220) for z in (279,204,254,204,279)]
    for n in range(4, 12):
        p0 = mat_base(n, F(0))
        for k in range(1, n):
            g = [green(n, k, j) for j in range(1, n)]
            for j in range(1, n):
                assert g[j-1] - sum(g[l-1]*p0[l][j]
                                   for l in range(1, n)) == (j == k)
        r = F(1, 100000)
        eta = r*r
        for k in range(2, n-1):
            pi = stationary(n, eta, r, k)
            assert triple_peaks(pi, k)
            assert abs(sum(j*pi[j] for j in range(n+1)) -
                       ((1-r)*eta+r*k)/(r+2*(1-r)*eta/n)) == 0
    print('PASS: exact N=4 stationary ratios, modal inequalities,', count,
          'rational parameter cases; five-point example; Green identities',
          'and rare-noise trimodality for 4<=N<=11.')


if __name__ == '__main__':
    main()
