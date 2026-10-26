#!/usr/bin/env python3
"""Self-contained finite checks of finite-field four-by-four group commutator fibers."""
from itertools import product
from collections import Counter


def product_g(x, y, q):
    a, b, c, d, e, f = x
    A, B, C, D, E, F = y
    return ((a+A)%q, (b+B+a*D)%q,
            (c+C+a*E+b*F)%q, (d+D)%q,
            (e+E+d*F)%q, (f+F)%q)


def inverse_g(x, q):
    a,b,c,d,e,f=x
    return ((-a)%q,(-b+a*d)%q,(-c+a*e+b*f-a*d*f)%q,
            (-d)%q,(-e+d*f)%q,(-f)%q)


def target_count(q,u,v,w):
    base=(q*q-1)*q**7
    if u or v:
        return base
    if w:
        return q**9+(q*q-2)*q**7
    return q**9+(q*q-2)*q**7+q**8


def exhaustive(q):
    universe=list(product(range(q),repeat=6))
    inverse={g:inverse_g(g,q) for g in universe}
    counts=Counter()
    for g in universe:
        for h in universe:
            z=product_g(product_g(product_g(g,h,q),inverse[g],q),inverse[h],q)
            if z[0] or z[3] or z[5]:
                raise AssertionError(('commutator_not_derived', q, z))
            counts[(z[1],z[4],z[2])]+=1
    assert len(counts)==q**3, (q,len(counts))
    for u,v,w in product(range(q),repeat=3):
        got=counts[(u,v,w)]
        expected=target_count(q,u,v,w)
        assert got==expected,(q,u,v,w,got,expected)
    assert sum(counts.values())==q**12
    print('FULL_UT4_GROUP_ENUMERATION',q,'PASS',sum(counts.values()),'pairs')


def characteristic_four():
    # GF(4) represented as F_2[t]/(t^2+t+1).
    def mul(x,y):
        a,b=x&1,(x>>1)&1
        c,d=y&1,(y>>1)&1
        return ((a*c)^(b*d)) | (((a*d)^(b*c)^(b*d))<<1)
    n=4
    count=Counter()
    for a,d,f,A,D,F in product(range(n),repeat=6):
        u=mul(a,D)^mul(A,d)
        v=mul(d,F)^mul(D,f)
        # each nonexceptional outer sextuple yields q^3 completions for every w,
        # exceptional produces q^4 completions for w=0.
        if (a,A,f,F)!=(0,0,0,0):
            for w in range(n):
                count[(u,v,w)]+=n**3*n**2
        else:
            count[(0,0,0)]+=n**4*n**2
    for u,v,w in product(range(n), repeat=3):
        assert count[(u,v,w)]==target_count(n,u,v,w),(u,v,w,count[(u,v,w)],target_count(n,u,v,w))
    print('GF4_OUTER_SEXTUPLE_ENUMERATION PASS',sum(count.values()),'pairs')


if __name__=='__main__':
    exhaustive(2)
    exhaustive(3)
    characteristic_four()
    print('VERIFY_OK_UT4_COMMUTATOR_FIBERS')
