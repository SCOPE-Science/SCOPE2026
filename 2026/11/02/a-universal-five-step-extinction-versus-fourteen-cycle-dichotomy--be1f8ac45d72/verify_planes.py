#!/usr/bin/env python3
"""Independent exact binary-matrix checks for finite-field projective planes."""
from collections import Counter

def gf_mul(a,b,s,mod):
    z=0
    while b:
        if b&1:z ^= a
        b >>=1;a <<=1
        if a & (1<<s): a ^= mod
    return z

def canonical_triples(q):
    pts=[]
    for first in range(3):
        for a in range(q**(2-first)):
            vals=[0]*3;vals[first]=1
            for j in range(first+1,3):
                vals[j]=(a//q**(2-j))%q
            pts.append(tuple(vals))
    return pts

def incidence(s,mod):
    q=1<<s; pts=canonical_triples(q);v=len(pts)
    assert v==q*q+q+1
    rows=[]
    for P in pts:
        row=0
        for j,L in enumerate(pts):
            dot=0
            for a,b in zip(P,L):dot^=gf_mul(a,b,s,mod)
            if dot==0: row|=1<<j
        rows.append(row)
    return pts,rows

def bit_rank(rows):
    basis={}
    for x in rows:
        while x:
            p=x.bit_length()-1
            if p not in basis:
                basis[p]=x;break
            x^=basis[p]
    return len(basis)

def map_rows(B,edit=None):
    n=len(B)
    if edit:
        p,l=edit;B=B[:];B[p]^=1<<l
    A=[0]*(2*n)
    for i in range(n):
        A[i]=B[i]<<n
        for j in range(n):
            if (B[i]>>j)&1:A[n+j]|=1<<i
    return A

def mul(A,C):
    ans=[]
    for a in A:
        s=0
        while a:
            low=a&-a;j=low.bit_length()-1;s^=C[j];a^=low
        ans.append(s)
    return ans

def power(A,t):
    n=len(A);R=[1<<i for i in range(n)];B=A
    while t:
        if t&1:R=mul(R,B)
        B=mul(B,B);t>>=1
    return R

def test():
    for s,mod in [(1,0b11),(2,0b111),(3,0b1011)]:
        pts,B=incidence(s,mod)
        q=1<<s;v=len(B)
        expected=(1+3**s)
        r=bit_rank(B)
        assert r==expected,(q,r,expected)
        assert all(x.bit_count()==q+1 for x in B)
        assert all(((B[i]&B[j]).bit_count()==1) for i in range(v) for j in range(i+1,v))
        for label,pair in [('delete',next((i,j) for i in range(v) for j in range(v) if (B[i]>>j)&1)),
                           ('add',next((i,j) for i in range(v) for j in range(v) if not ((B[i]>>j)&1)))]:
            A=map_rows(B,pair)
            ranks=[bit_rank(power(A,t)) for t in range(6)]
            if label=='delete':
                assert ranks==[2*v,2*(r+1),6,4,2,0],(q,ranks)
            else:
                assert ranks[:3]==[2*v,2*(r+1),6],(q,ranks)
                assert power(A,16)==power(A,2)
                assert power(A,9)!=power(A,2)
                assert bit_rank(power(A,14))==6
                assert bit_rank(power(A,7))==6
            print('q=',q,'v=',v,'binary_rank=',r,'edit=',label,'pair=',pair,'power_ranks=',ranks)
    # q=2 complete state enumeration independently computes first entry and exact periods
    pts,B=incidence(1,0b11)
    for label,pair in [('delete',next((i,j) for i in range(7) for j in range(7) if (B[i]>>j)&1)),
                       ('add',next((i,j) for i in range(7) for j in range(7) if not ((B[i]>>j)&1)))]:
        A=map_rows(B,pair)
        n=len(A)
        def F(x):
            y=0
            for i,row in enumerate(A):
                if (row&x).bit_count()&1:y|=1<<i
            return y
        entries=Counter();periods=Counter();orbits=set();basins=Counter()
        for x in range(1<<n):
            seen={};seq=[];y=x
            while y not in seen:
                seen[y]=len(seq);seq.append(y);y=F(y)
            e=seen[y];p=len(seq)-e;entries[e]+=1;periods[p]+=1
            cyc=tuple(sorted(seq[e:]));orbits.add(cyc);basins[cyc]+=1
        print('exhaustive',label,'entrance',sorted(entries.items()),'period_point_counts',sorted(periods.items()),
              'orbit_counts',sorted(Counter(len(c) for c in orbits).items()),'basins',sorted(Counter((len(c),basins[c]) for c in orbits).items()))
        if label=='delete':assert entries=={0:1,1:15,2:240,3:768,4:3072,5:12288}
        else:assert entries=={0:64,1:960,2:15360};assert Counter(len(c) for c in orbits)=={1:1,7:1,14:4}
    print('ALL_CHECKS_PASS')
if __name__=='__main__':test()
