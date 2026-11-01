"""Self-contained finite consistency checks for the discrete Sobolev phase identity.

The general assertion is proved algebraically; these finite checks are supplementary.
Run: python3 verify.py
"""
from fractions import Fraction as F
from itertools import combinations
from math import comb, isclose
from cmath import exp


def inverse(a):
    n = len(a)
    v = [[F(a[i][j]) for j in range(n)] + [F(i == j) for j in range(n)] for i in range(n)]
    for i in range(n):
        p = next(j for j in range(i, n) if v[j][i])
        v[i], v[p] = v[p], v[i]
        t = v[i][i]
        v[i] = [x / t for x in v[i]]
        for j in range(n):
            if j != i:
                t = v[j][i]
                v[j] = [x - t * y for x, y in zip(v[j], v[i])]
    return [row[n:] for row in v]


def gram(alpha, d):
    D = [[F((-1) ** (r-j) * comb(alpha, r-j)) if 0 <= r-j <= alpha else F(0)
          for j in range(d)] for r in range(d + alpha)]
    Q = [[sum(D[r][i] * D[r][j] for r in range(d+alpha)) for j in range(d)] for i in range(d)]
    return Q


def norm2Q(a, q):
    return sum(a[i].conjugate() * q[i][j] * a[j] for i in range(len(a)) for j in range(len(a)))


def check():
    tests = 0
    for alpha in range(1, 5):
        for d in range(1, 9):
            q = gram(alpha, d)
            k = inverse(q)
            for row in k:
                for t in row:
                    assert t > 0
                    tests += 1
            v = [comb(j + alpha - 1, alpha) * comb(d + alpha - j, alpha) for j in range(1, d+1)]
            b = comb(2*alpha, alpha)
            assert [sum(q[i][j]*v[j] for j in range(d)) for i in range(d)] == [b]*d
            tests += d
            C2 = sum(sum(row) for row in k)
            assert C2 == F(comb(d+2*alpha,2*alpha+1),b)
            tests += 1
            for mode in range(1, 5):
                a = [complex((i+2) * (mode+1), ((i*i+2*mode)%7)-3) for i in range(d)]
                if mode == 4 and d >= 2:
                    a[0] = 0
                s = [z/abs(z) if z else 1+0j for z in a]
                k_s = [sum(float(k[i][j])*s[j] for j in range(d)) for i in range(d)]
                norm2 = norm2Q(a,q)
                sks = sum(s[i].conjugate()*k_s[i] for i in range(d)).real
                phases = sum(float(k[i][j])*abs(s[i]-s[j])**2
                             for i in range(d) for j in range(i+1,d))
                c = sum(s[i].conjugate()*a[i] for i in range(d))/sks
                shape = norm2Q([a[i]-c*k_s[i] for i in range(d)],q)
                rhs = phases*norm2 + sks*shape
                lhs = float(C2)*norm2 - sum(abs(z) for z in a)**2
                assert abs(lhs-rhs) < 2e-8*(1+abs(lhs))
                tests += 1
    print('PASS',tests,'supplementary exact and numerical assertions')

if __name__ == '__main__':
    check()
