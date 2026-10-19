#!/usr/bin/env python3
"""Independent finite-field checks of multiplication-rank strata in a square-zero complete intersection."""
from collections import Counter
from itertools import product
import random

MASKS = range(1,16)
Q2 = lambda a,b:a&b

def mul4(a,b):
    out=0
    for i in range(2):
        if (b>>i)&1:out ^= a<<i
    for i in (2,):
        if (out>>i)&1:out ^= 0b111<<(i-2)
    return out

def fieldmul(q,a,b):
    if q==2:return a&b
    if q==4:return mul4(a,b)
    raise ValueError

def matrix_mul_elem(u,q):
    """Columns indexed by subsets; all scalar entries in the natural monomial basis."""
    M=[[0]*16 for _ in range(16)]
    for c in range(16):
        for x in range(1,16):
            if x&c==0:
                M[x|c][c]^=u[x]
    return M

def rankfield(M,q):
    M=[row[:] for row in M]
    piv=0
    m=len(M); n=len(M[0])
    for col in range(n):
        k=next((r for r in range(piv,m) if M[r][col]),None)
        if k is None:continue
        M[piv],M[k]=M[k],M[piv]
        # q=2,4: inverse of nonzero a is a^2 in GF(4).
        inv=1 if q==2 else fieldmul(q,M[piv][col],M[piv][col])
        M[piv]=[fieldmul(q,a,inv) for a in M[piv]]
        for r in range(piv+1,m):
            if M[r][col]:
                scalar=M[r][col]
                M[r]=[a^fieldmul(q,scalar,b) for a,b in zip(M[r],M[piv])]
        piv+=1
        if piv==m:break
    return piv

def rankbit(u):
    b=[0]*16;rank=0
    for c in range(16):
        v=0
        for x in range(1,16):
            if ((u>>x)&1) and not(x&c):v ^= 1<<(x|c)
        while v:
            k=v.bit_length()-1
            if b[k]:v^=b[k]
            else:
                b[k]=v;rank+=1;break
    return rank

def pfaffian(u,q):
    a=lambda x:u[x]
    return fieldmul(q,a(3),a(12)) ^ fieldmul(q,a(5),a(10)) ^ fieldmul(q,a(9),a(6))

def predicted(u,q):
    linear=(1,2,4,8);quad=(3,5,6,9,10,12);cubic=(7,11,13,14)
    if any(u[x] for x in linear):return 8
    if any(u[x] for x in quad):return 6 if pfaffian(u,q) else 4
    if any(u[x] for x in cubic):return 2
    if u[15]:return 1
    return 0

def counts(q):
    return {0:1,1:q-1,2:q*(q**4-1),4:q**5*(q**2+1)*(q**3-1),
            6:q**7*(q-1)*(q**3-1),8:(q**4-1)*q**11}

def full_binary():
    cnt=Counter()
    for value in range(1<<15):
        u=(value<<1)
        r=rankbit(u)
        coeff=[(u>>x)&1 for x in range(16)]
        assert r==predicted(coeff,2),(value,r,predicted(coeff,2))
        cnt[r]+=1
    assert dict(cnt)==counts(2),(cnt,counts(2))
    print('GF2_EXHAUSTIVE',dict(sorted(cnt.items())))

def checks_quaternary():
    rng=random.Random(1701)
    cs=Counter()
    quad=(3,5,6,9,10,12)
    for v in product(range(4),repeat=6):
        u=[0]*16
        for i,x in enumerate(quad):u[x]=v[i]
        r=rankfield(matrix_mul_elem(u,4),4)
        assert r==predicted(u,4),(v,r,predicted(u,4))
        cs[r]+=1
    assert cs=={0:1,4:1071,6:3024},cs
    print('GF4_ALL_QUADRATICS',dict(sorted(cs.items())))
    for k in range(300):
        u=[0]+[rng.randrange(4) for _ in range(15)]
        r=rankfield(matrix_mul_elem(u,4),4)
        assert r==predicted(u,4),(k,u,r,predicted(u,4))
    print('GF4_RANDOM_FULL',300)

def main():
    full_binary()
    checks_quaternary()
    assert sum(counts(4).values())==4**15
    print('ALL_RANK_SPECTRUM_TESTS_PASSED')

if __name__=='__main__':main()
