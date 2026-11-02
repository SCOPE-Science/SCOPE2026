"""Exact arithmetic checks for RK4 positivity on reflecting path graphs.

This file is a finite verification aid; the all-size theorem follows from
symbolic identities in RESULT.md rather than the finite test loop.
"""
from fractions import Fraction as F
from math import comb


def matmul(a, b):
    n = len(a)
    return [[sum((a[i][k] * b[k][j] for k in range(n)), F(0))
             for j in range(n)] for i in range(n)]


def generator(n):
    q = [[F(0) for _ in range(n)] for _ in range(n)]
    for i in range(n-1):
        q[i][i] -= 1
        q[i+1][i+1] -= 1
        q[i][i+1] = q[i+1][i] = 1
    return q


def polynomial(q, z):
    n = len(q)
    out = [[F(int(i == j)) for j in range(n)] for i in range(n)]
    power = [[F(int(i == j)) for j in range(n)] for i in range(n)]
    fact = 1
    for k in range(1,5):
        power = matmul(power, q)
        fact *= k
        factor = z**k / fact
        for i in range(n):
            for j in range(n):
                out[i][j] += factor * power[i][j]
    return out


def bernstein_coefficients(monomial_coeffs, bound):
    d = len(monomial_coeffs)-1
    transformed = [a*bound**k for k,a in enumerate(monomial_coeffs)]
    return [sum((transformed[k]*F(comb(j,k),comb(d,k))
                 for k in range(j+1)),F(0)) for j in range(d+1)]


def test():
    count = 0
    def check(c, why):
        nonlocal count
        assert c, why
        count += 1

    # Formal algebraic positivity certificate for all first- and
    # second-neighbor polynomials on the exceptional small paths.
    tables = {
        4: (F(2,3), [
             [F(1),-F(3,2),F(3,2),-F(7,6)],
             [F(1),-F(2),F(5,2),-F(9,4)],
             [F(1,2),-F(5,6),F(5,6)]]),
        5: (F(4,7), [
             [F(1),-F(3,2),F(3,2),-F(7,6)],
             [F(1),-F(2),F(5,2),-F(55,24)],
             [F(1,2),-F(5,6),F(5,6)],
             [F(1,2),-F(1),F(7,6)]])
    }
    for n,(bound,polys) in tables.items():
        for p in polys:
            for c in bernstein_coefficients(p,bound):
                check(c>0,(n,p,c))
    for n in range(2,31):
        q=generator(n)
        if n == 2:
            # Boundary at the positive root of z^3-2z^2+3z-3.
            lo=F(1392646781702,10**12)
            hi=F(1392646781703,10**12)
            def p(z):return z**3-2*z**2+3*z-3
            check(p(lo)<0<p(hi),'n2-root')
            bounds=[F(0),F(1,2),F(1),lo]
            beyond=hi
        elif n == 3:
            lo=F(928431187801,10**12)
            hi=F(928431187802,10**12)
            def p(z):return 9*z**3-12*z**2+12*z-8
            check(p(lo)<0<p(hi),'n3-root')
            bounds=[F(0),F(1,2),lo]
            beyond=hi
        else:
            bound={4:F(2,3),5:F(4,7)}.get(n,F(1,2))
            bounds=[F(0),F(1,4),F(1,2),bound]
            beyond=bound+F(1,100)
        for z in bounds:
            a=polynomial(q,z)
            for i in range(n):
                check(sum(a[i])==1, ('mass',n,z,i))
                for j in range(n):
                    check(a[i][j]>=0, ('positive',n,z,i,j,a[i][j]))
        a=polynomial(q,beyond)
        check(any(a[i][j]<0 for i in range(n) for j in range(n)),
              ('sharp',n,beyond))
        if n>=6:
            check(a[1][4]<0, ('distance-three obstruction',n))
    # General degree-sum identity for distance-three entries on paths.
    for n in range(4,31):
        q=generator(n)
        # Extract coefficients by successive exact matrix products.
        q3=matmul(matmul(q,q),q)
        q4=matmul(q3,q)
        degrees=[1]+[2]*(n-2)+[1]
        for i in range(n-3):
            check(q3[i][i+3]==1, ('walk length three',n,i))
            check(q4[i][i+3]==-sum(degrees[i:i+4]),
                  ('degree-sum obstruction',n,i))
    print('PASS', count, 'exact assertions')

if __name__=='__main__':
    test()
