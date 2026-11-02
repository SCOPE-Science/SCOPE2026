#!/usr/bin/env python3
"""Exact arithmetic spot checks for prime-index Franel power polynomials.

Standalone standard-library script; finite tests corroborate, not replace,
the symbolic Eisenstein, multiplier-sequence and discriminant arguments.
"""
from fractions import Fraction
from math import comb


def mul(a, b):
    c = [0] * (len(a) + len(b) - 1)
    for i, ai in enumerate(a):
        for j, bj in enumerate(b):
            c[i+j] += ai*bj
    return c


def divide_x_plus_one(a):
    # a in increasing coefficient order, divisor 1+X.
    q = [0] * (len(a)-1)
    q[-1] = a[-1]
    for j in range(len(q)-2, -1, -1):
        q[j] = a[j+1] - q[j+1]
    assert a[0] == q[0]
    assert mul(q, [1, 1]) == a
    return q


def translate_plus(a, shift):
    # f(Y+shift), coefficient order low to high.
    return [sum(a[k]*comb(k,j)*shift**(k-j)
                for k in range(j, len(a))) for j in range(len(a))]


def bareiss_det(a):
    a = [list(row) for row in a]
    n = len(a)
    if n == 0: return 1
    sgn, prev = 1, 1
    for k in range(n-1):
        if not a[k][k]:
            t = next((i for i in range(k+1,n) if a[i][k]), None)
            if t is None: return 0
            a[k],a[t] = a[t],a[k]
            sgn = -sgn
        pivot = a[k][k]
        for i in range(k+1,n):
            for j in range(k+1,n):
                numerator = a[i][j]*pivot - a[i][k]*a[k][j]
                assert numerator%prev==0
                a[i][j]=numerator//prev
        for i in range(k+1,n): a[i][k]=0
        prev=pivot
    return sgn*a[-1][-1]


def resultant_monic(a, b):
    # resultant(f,g): Sylvester matrix descending coefficient rows.
    m,n=len(a)-1,len(b)-1
    assert m>0 and n>0
    rows = []
    for i in range(n):
        rows.append([0]*i + list(reversed(a)) + [0]*(n-1-i))
    for i in range(m):
        rows.append([0]*i + list(reversed(b)) + [0]*(m-1-i))
    assert len(rows)==m+n and all(len(row)==m+n for row in rows)
    return bareiss_det(rows)


def discriminant_monic(a):
    m=len(a)-1
    derivative=[j*a[j] for j in range(1,len(a))]
    return (-1)**(m*(m-1)//2)*resultant_monic(a,derivative)


def remove_p(n,p):
    z=0
    while n%p==0:
        n//=p
        z+=1
    return z,n


def trim(a):
    a=list(a)
    while a and a[-1]==0: a.pop()
    return a


def poly_remainder(a,b):
    a=trim(a);b=trim(b)
    while len(a)>=len(b) and a:
        factor = a[-1]/b[-1]
        ofs=len(a)-len(b)
        for j, v in enumerate(b):a[ofs+j]-=factor*v
        a=trim(a)
    return a


def sturm(a):
    p=[Fraction(v) for v in a]
    der=[i*p[i] for i in range(1,len(p))]
    seq=[p,der]
    while seq[-1]:
        r=poly_remainder(seq[-2],seq[-1])
        if not r:break
        seq.append([-v for v in r])
    return seq


def var_signs(a, at):
    vals=[]
    for p in a:
        if at=='neg_inf':
            v=p[-1]*(-1)**(len(p)-1)
        elif at=='pos_inf':v=p[-1]
        else:
            v=sum(p[i]*Fraction(at)**i for i in range(len(p)))
        if v: vals.append(1 if v>0 else -1)
    return sum(x!=y for x,y in zip(vals, vals[1:]))


def main():
    polys=0; es=0; discr=0; sturm_checks=0
    for p in (3,5,7,11):
        for r in (3,4,5):
            f=[comb(p,k)**r for k in range(p+1)]
            assert f==f[::-1]
            q=divide_x_plus_one(f)
            assert q==q[::-1] and q[0]==q[-1]==1
            h=translate_plus(q,-1)
            assert h[-1]==1
            assert all(v%p==0 for v in h[:-1])
            assert h[0]%p**2==p
            assert sum((-1)**(k-1)*k*f[k] for k in range(1,len(f)))==h[0]
            es+=len(h)
            disc=discriminant_monic(q)
            v,u=remove_p(disc,p)
            assert v==p-2 and u%p==(-1)**((p-1)//2)%p
            assert disc>0
            discr+=1
            if p<=7 and r<=4:
                seq=sturm(q)
                total=var_signs(seq,'neg_inf')-var_signs(seq,0)
                left=var_signs(seq,'neg_inf')-var_signs(seq,-1)
                right=var_signs(seq,-1)-var_signs(seq,0)
                assert (total,left,right)==(p-1,(p-1)//2,(p-1)//2)
                sturm_checks+=1
            polys+=1
    print(f'VERIFY_OK: {polys} prime/exponent polynomials, {es} shifted Eisenstein coefficients, {discr} independent integer Sylvester discriminants, {sturm_checks} exact real-root counts')


if __name__=='__main__':
    main()
