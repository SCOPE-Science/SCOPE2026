"""Finite exact verification of complete-graph monomer-dimer precision formulas.

Run with Python 3.9+; uses only the standard library. Finite checks do not
substitute for the unrestricted argument given in RESULT.md.
"""
from fractions import Fraction as F
from itertools import combinations
from math import comb

CHECKS = 0

def eq(a, b):
    global CHECKS
    CHECKS += 1
    assert a == b, (a, b)

def test(a):
    global CHECKS
    CHECKS += 1
    assert a

def matchings(vertices):
    """Generate all matchings independently of partition-function recurrence."""
    vertices = tuple(vertices)
    if not vertices:
        yield ()
        return
    u, *rest = vertices
    for tail in matchings(rest):
        yield tail
    for j, v in enumerate(rest):
        for tail in matchings(rest[:j] + rest[j+1:]):
            yield ((u, v),) + tail

def partition(n, t):
    z = [F(1)] * (n+1)
    for k in range(2, n+1):
        z[k] = z[k-1] + (k-1)*t*z[k-2]
    return z

def formulas(n, t):
    z = partition(n, t)
    M = comb(n, 2)
    D = comb(n-2, 2)
    p = t*z[n-2]/z[n]
    q = t*t*z[n-4]/z[n]
    l0 = p-M*p*p+D*q
    l1 = p-(n-3)*q
    l2 = p+q
    test(l0 > 0 and l1 > 0 and l2 > 0)
    r0, r1, r2 = 1/l0, 1/l1, 1/l2
    c = F(2, n*(n-1))*r0 - F(4, n*(n-2))*r1 + F(2, (n-1)*(n-2))*r2
    b = F(2, n*(n-1))*r0 + F(n-4, n*(n-2))*r1 - F(n-3, (n-1)*(n-2))*r2
    a = (r0 + (n-1)*r1 + (M-n)*r2)/M
    return p, q, (l0, l1, l2), (a, b, c)

def inverse_product(n, t):
    edges = list(combinations(range(n), 2))
    p, q, _, (a, b, c) = formulas(n, t)
    S = []
    Q = []
    for e in edges:
        srow = []
        qrow = []
        for f in edges:
            z = len(set(e) & set(f))
            srow.append(p-p*p if z == 2 else -p*p if z == 1 else q-p*p)
            qrow.append(a if z == 2 else b if z == 1 else c)
        S.append(srow)
        Q.append(qrow)
    for i in range(len(edges)):
        for j in range(len(edges)):
            eq(sum(S[i][k]*Q[k][j] for k in range(len(edges))), F(i==j))

def exhaustive():
    for n in range(4, 9):
        E = ((0, 1), (0, 2), (2, 3))
        all_m = list(matchings(range(n)))
        eq(len(all_m), partition(n, F(1))[n])
        for t in (F(1, 3), F(1), F(3)):
            z = sum(t**len(m) for m in all_m)
            ze = sum(t**len(m) for m in all_m if E[0] in m)
            za = sum(t**len(m) for m in all_m if E[1] in m)
            zd = sum(t**len(m) for m in all_m if E[2] in m)
            zed = sum(t**len(m) for m in all_m if E[0] in m and E[2] in m)
            p, q, L, P = formulas(n, t)
            eq(z, partition(n, t)[n])
            eq(ze/z, p)
            eq(za/z, p)
            eq(zd/z, p)
            eq(zed/z, q)
            test(ze * za > 0)
            inverse_product(n, t)

def asymptotics():
    for n in range(4, 15):
        for t in (F(1, 10**5), F(1, 10**6)):
            c = formulas(n, t)[-1][-1]
            test(abs(c/(t*t) + 2) < F(1, 100))
            test(c < 0)
        for t in (F(10**5), F(10**6)):
            c = formulas(n, t)[-1][-1]
            slope = F(6, n-1) if n%2 else -F(2, n-2)
            test(abs(c/t - slope) < F(1, 100))
            test(c > 0 if n%2 else c < 0)
    for n in (5, 7, 9, 11, 13):
        test(formulas(n, F(1, 10))[-1][-1] < 0)
        test(formulas(n, F(10))[-1][-1] > 0)
    eq(formulas(5, F(1))[-1][-1], F(26, 55))
    eq(formulas(5, F(1,10))[-1][-1], F(-43, 3850))

if __name__ == '__main__':
    exhaustive()
    asymptotics()
    print('PASS:', CHECKS, 'exact rational assertions')
