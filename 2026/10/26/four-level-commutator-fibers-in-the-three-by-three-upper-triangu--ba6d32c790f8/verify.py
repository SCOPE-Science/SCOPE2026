#!/usr/bin/env python3
"""Independent finite checks of commutator fibers in 3x3 triangular algebras.

Python 3 standard library only. This program enumerates literal matrices over
F_2 and F_3, then checks coefficient ranks over F_4. It does not prove the
all-field assertion, which follows from the separate symbolic rank argument.
"""
from collections import Counter
from itertools import product


def expected(q, s, t, h):
    return (q**5 * (q*q-1)**2
            + q**6 * (q*q-1) * ((s == 0) + (t == 0))
            + q**8 * (s == 0 and t == 0 and h == 0))


def mul(a,b,q):
    # Storage (diagonal first, then 12,23,13).
    A,B,C,x,z,u = a
    D,E,F,y,w,v = b
    return ((A*D)%q,(B*E)%q,(C*F)%q,
            (A*y+x*E)%q,(B*w+z*F)%q,
            (A*v+x*w+u*F)%q)


def literal_all(q):
    counter=Counter()
    elements=list(product(range(q),repeat=6))
    for a in elements:
        for b in elements:
            ab=mul(a,b,q);ba=mul(b,a,q)
            target=tuple((ab[i]-ba[i])%q for i in (3,4,5))
            counter[target]+=1
    for target in product(range(q),repeat=3):
        assert counter[target]==expected(q,*target),(q,target,counter[target],expected(q,*target))
    assert sum(counter.values()) == q**12
    print('LITERAL_OK',q,len(elements)**2)


# GF4 is GF2[t]/(t^2+t+1), represented by two binary coefficients.
def gf_mul(a,b):
    out=0
    for i in range(2):
        for j in range(2):
            if (a>>i)&1 and (b>>j)&1:
                out ^= (1<<(i+j))
    if out&4:
        out ^= 7  # t^2 = t + 1
    return out


def rank_mod(m,q):
    m=[row[:] for row in m]
    r=0
    for j in range(len(m[0])):
        i=next((i for i in range(r,len(m)) if m[i][j]),None)
        if i is None:continue
        m[r],m[i]=m[i],m[r]
        pivot=m[r][j]
        if q==4:
            inv=next(x for x in (1,2,3) if gf_mul(x,pivot)==1)
            for k in range(j,len(m[0])):m[r][k]=gf_mul(m[r][k],inv)
        else:
            inv=pow(pivot,-1,q)
            for k in range(j,len(m[0])):m[r][k]=(m[r][k]*inv)%q
        for i in range(len(m)):
            if i==r or not m[i][j]:continue
            v=m[i][j]
            for k in range(j,len(m[0])):
                if q==4:m[i][k]^=gf_mul(v,m[r][k])
                else:m[i][k]=(m[i][k]-v*m[r][k])%q
        r+=1
    return r


def pairing_ranks(q):
    neg=lambda a:a if q==4 else (-a)%q
    for s,t,h in product(range(q),repeat=3):
        # [A,B] pairing matrix on basis (diag differences 12,23, E12,E23,E13).
        M=[[0,0,s,0,h],
           [0,0,0,t,h],
           [neg(s),0,0,h,0],
           [0,neg(t),neg(h),0,0],
           [neg(h),neg(h),0,0,0]]
        observed=rank_mod(M,q)
        desired=4 if h else 2*(int(s!=0)+int(t!=0))
        assert observed==desired,(q,s,t,h,observed,desired)
    print('PAIRING_RANKS_OK',q,q**3)


def sum_fibers(q):
    return sum(expected(q,*x) for x in product(range(q),repeat=3))


if __name__=='__main__':
    for q in (2,3):literal_all(q)
    for q in (2,3,4):pairing_ranks(q)
    for q in (2,3,4,5,7,9,11):assert sum_fibers(q)==q**12
    print('VERIFY_OK_TRIANGULAR_COMMUTATOR_FIBERS')
