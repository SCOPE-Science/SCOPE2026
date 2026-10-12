#!/usr/bin/env python3
"""Independent finite verification of a one-gate-deleted complete CCZ hypergraph rank spectrum."""
from fractions import Fraction
from collections import Counter
from math import comb


def rank2(rows):
    basis={}
    for row in rows:
        while row:
            k=row.bit_length()-1
            if k in basis:row ^= basis[k]
            else:basis[k]=row;break
    return len(basis)


def direct_rank(n,a):
    parity=a.bit_count()&1
    rows=[]
    for i in range(n):
        row=0
        for j in range(n):
            if i==j:continue
            c=parity ^ ((a>>i)&1) ^ ((a>>j)&1)
            if i<3 and j<3:
                third=3-i-j
                c ^= (a>>third)&1
            row|=c<<j
        rows.append(row)
    return rank2(rows)


def compact_rank(n,h,w):
    m=n-3
    r=w&1
    s=(h+w)&1
    counts=[3-h,h,m-w,w]
    live=[i for i,k in enumerate(counts) if k>0]
    k_rows=[]
    for g in live:
        k=counts[g]
        inside=r if g<2 else s
        row=0
        if inside and not k%2:
            row=1<<live.index(g)
        else:
            for j,d in enumerate(live):
                if d==g:continue
                if g<2 and d<2: c=r
                elif g>=2 and d>=2:c=s^((g-2)^(d-2))
                else:
                    tt=g if g<2 else d
                    oo=g-2 if g>=2 else d-2
                    c=s^tt^oo
                row |= c<<j
        k_rows.append(row)
    kernel=sum(k-1 for g,k in enumerate(counts) if k and (r if g<2 else s)==0)+len(live)-rank2(k_rows)
    return n-kernel


def claimed_rank(n,h,w):
    m=n-3
    if n%2:
        if h==0: return 0 if w==0 else (2 if w%2==0 else n-1)
        if h==1:return n-3 if w%2==0 else 4
        if h==2:return (2 if w in (0,m) else 4) if w%2==0 else n-1
        if h==3:return n-3 if w%2==0 else 4
    else:
        if h==0:return 0 if w==0 else (2 if w%2==0 else n-2)
        if h==1:return n-2 if w%2==0 else (2 if w==m else 4)
        if h==2:return (2 if w==0 else 4) if w%2==0 else n-2
        if h==3:return n-4 if w%2==0 else (2 if w==m else 4)
    raise ValueError


def predicted_counts(n):
    z=2**(n-4)
    if n%2:
        parts={0:1,2:z+5,4:7*z-6,n-1:2**(n-2),n-3:2**(n-2)}
        # overlapping ranks at n=5 must be summed
        arr=[(0,1),(2,z+5),(4,7*z-6),(n-1,2**(n-2)),(n-3,2**(n-2))]
    else:
        arr=[(0,1),(2,z+6),(4,7*z-7),(n-2,7*z),(n-4,z)]
    out=Counter()
    for r,k in arr:out[r]+=k
    return out


def f(x):
    # elementary symmetric cubic in the Hamming weight, except the removed {0,1,2} triple
    return (comb(x.bit_count(),3)&1) ^ ((x&7)==7)


def fast_walsh(y):
    y=y[:]
    q=1
    while q<len(y):
        for i in range(0,len(y),2*q):
            for j in range(i,i+q):
                t=y[j];u=y[j+q]
                y[j]=t+u;y[j+q]=t-u
        q*=2
    return y


def direct_moment2(n):
    size=1<<n
    sig=[-1 if f(x) else 1 for x in range(size)]
    total=0
    for a in range(size):
        vals=[sig[x]*sig[x^a] for x in range(size)]
        total+=sum(z**4 for z in fast_walsh(vals))
    return Fraction(total,1<<(5*n))


def closed_moment(n):
    return Fraction(11,256)+Fraction((77 if n%2==0 else 70),1<<(n+4))


def run():
    cases=0
    for n in range(4,31):
        out=Counter()
        for h in range(4):
            for w in range(n-2):
                got=compact_rank(n,h,w)
                want=claimed_rank(n,h,w)
                assert got==want,(n,h,w,got,want)
                out[got]+=comb(3,h)*comb(n-3,w)
                cases+=1
        assert out==predicted_counts(n),(n,out,predicted_counts(n))
        assert sum(out.values())==1<<n
        got=sum((Fraction(k,1<<r) for r,k in out.items()),Fraction(0))/(1<<n)
        assert got==closed_moment(n),(n,got,closed_moment(n))
    for n in range(4,12):
        for a in range(1<<n):
            h=(a&7).bit_count();w=(a>>3).bit_count()
            assert direct_rank(n,a)==compact_rank(n,h,w),(n,a)
    for n in range(4,9):
        assert direct_moment2(n)==closed_moment(n),(n,direct_moment2(n),closed_moment(n))
    print('VERIFY_OK compact_pattern_cases=%d exhaustive_shifts_n=4..11 independent_Walsh_n=4..8'%(cases))

if __name__=='__main__':run()
