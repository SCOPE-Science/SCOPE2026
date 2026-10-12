#!/usr/bin/env python3
"""Direct enumerations for the rank spectrum of Lie homomorphisms of finite Heisenberg algebras."""
from itertools import product
from fractions import Fraction
from collections import Counter


def isotropic_subspaces(m,r,q):
    a=Fraction(1)
    for i in range(r):
        a *= Fraction(q**(2*(m-i))-1,q**(r-i)-1)
    assert a.denominator==1
    return int(a)

def prediction(m,q):
    n=2*m
    cnt=Counter()
    for r in range(m+1):
        d=isotropic_subspaces(m,r,q)
        maps=1
        for i in range(r): maps *= q**n-q**i
        cnt[r]+=d*maps*q**r
        cnt[r+1]+=d*maps*(q**n-q**r)
    sp=q**(m*m)
    for i in range(1,m+1): sp*=q**(2*i)-1
    cnt[2*m+1] += q**n*(q-1)*sp
    return cnt


def rank_columns(cols):
    # GF(2) independent rank algorithm
    piv={};r=0
    for c in cols:
        x=c
        while x:
            i=x.bit_length()-1
            if i not in piv:
                piv[i]=x;r+=1;break
            x^=piv[i]
    return r


def m2_binary():
    got=Counter()
    n=4
    pairs=((0,2),(1,3))
    def w(a,b):
        return ((a>>0 & 1)*(b>>2 & 1) ^ (a>>2 & 1)*(b>>0 & 1) ^
                (a>>1 & 1)*(b>>3 & 1) ^ (a>>3 & 1)*(b>>1 & 1))
    for cols in product(range(16),repeat=4):
        lam=w(cols[0],cols[2])
        if any(w(cols[i],cols[j])!= (lam if (i,j) in pairs else 0)
               for i in range(4) for j in range(i+1,4)):
            continue
        for f in range(16):
            full=[cols[i] | ((f>>i&1)<<4) for i in range(4)] + [lam<<4]
            got[rank_columns(full)]+=1
    expect=prediction(2,2)
    assert got==expect,(got,expect)
    print('m2 q2',dict(sorted(got.items())),'total',sum(got.values()))


def small_all(q):
    # Direct full matrix enumeration for H_1 in characteristic 2 and odd characteristic,
    # with binary polynomial representation for GF(4): a^2=a+1.
    def mul(a,b):
        if q!=4: return a*b%q
        z=0
        for i in range(2):
            if b>>i&1:z ^= a<<i
        if z&8:z^=0b1100
        if z&4:z^=0b0111
        return z
    def add(a,b): return a^b if q==4 else (a+b)%q
    def neg(a):return a if q==4 else (-a)%q
    def rank(cs):
        rows=[[cs[c][r] for c in range(3)] for r in range(3)]
        r=0
        for c in range(3):
            i=next((i for i in range(r,3) if rows[i][c]),None)
            if i is None:continue
            rows[r],rows[i]=rows[i],rows[r]
            for j in range(r+1,3):
                if rows[j][c]:
                    fac=next(t for t in range(1,q) if mul(t,rows[r][c])==rows[j][c])
                    rows[j]=[add(rows[j][k],neg(mul(fac,rows[r][k]))) for k in range(3)]
            r+=1
        return r
    got=Counter()
    for ent in product(range(q),repeat=9):
        cs=[ent[:3],ent[3:6],ent[6:]]
        # Heisenberg bracket is [a,b]=(a0*b1-a1*b0) z.
        b=lambda u,v:add(mul(u[0],v[1]),neg(mul(u[1],v[0])))
        if (cs[2][0] or cs[2][1] or cs[2][2]!=b(cs[0],cs[1])
            or b(cs[0],cs[2]) or b(cs[1],cs[2])):
            continue
        got[rank(cs)]+=1
    expect=prediction(1,q)
    assert got==expect,(q,got,expect)
    print('m1 q',q,dict(sorted(got.items())),'total',sum(got.values()))


def sum_checks():
    for q in [2,3,4,5,7]:
      for m in range(1,8):
        d=prediction(m,q)
        assert set(d)==set(range(m+2))|{2*m+1} if m>1 else set(d)==set(range(4))
        assert d[0]==1
        assert all(v>0 for v in d.values())
    print('symbolic finite product normalizations checked')

if __name__=='__main__':
    for q in [2,3,4]:small_all(q)
    m2_binary()
    sum_checks()
    print('VERIFY_OK_HEISENBERG_ENDOMORPHISM_RANKS')
