#!/usr/bin/env python3
"""Exact checks for the near-balanced bipartite leader allocation theorem.
Standard library only. Finite checks supplement, not replace, the displayed proof.
"""
from fractions import Fraction as Q
from itertools import combinations
from math import comb

def cost(m,k,a):
    n=m+1
    b=k-a
    p=m-a
    q=n-b
    assert 0 <= a <= m and 0 <= b <= n and 1 <= k <= 2*m
    z=m*n-p*q
    assert z>0
    return Q(p,n)+Q(q,m)+Q((m+n)*p*q,m*n*z)

def expected_allocation(m,k):
    if k>=m+1:
        return [k-(m+1)]
    v=k*k-(2*m+1)
    if v<0: return [k]
    if v>0: return [0]
    return [0,k]

def invert_trace(A):
    n=len(A)
    if n==0: return Q(0)
    v=[[Q(x) for x in row]+[Q(i==j) for j in range(n)] for i,row in enumerate(A)]
    for j in range(n):
        z=next((i for i in range(j,n) if v[i][j]),None)
        assert z is not None
        v[j],v[z]=v[z],v[j]
        c=v[j][j]
        v[j]=[t/c for t in v[j]]
        for i in range(n):
            if i!=j:
                c=v[i][j]
                if c:
                    v[i]=[x-c*y for x,y in zip(v[i],v[j])]
    return sum(v[i][n+i] for i in range(n))

def direct_cost(m,selected):
    n=m+1
    F=[v for v in range(2*m+1) if v not in selected]
    A=[]
    for i in F:
        row=[]
        for j in F:
            if i==j: row.append(n if i<m else m)
            else: row.append(-int((i<m)!=(j<m)))
        A.append(row)
    return invert_trace(A)

def main():
    total=0; chords=0; direct=0; allsets=0; ties=0
    for m in range(2,101):
        for k in range(1,2*m+1):
            lo=max(0,k-(m+1)); hi=min(k,m)
            opts=expected_allocation(m,k)
            cv={a:cost(m,k,a) for a in range(lo,hi+1)}
            mn=min(cv.values())
            assert [a for a in cv if cv[a]==mn]==opts,(m,k,opts,cv)
            if k<=m:
                J0,Jk=cv[0],cv[k]
                assert Jk==Q((k+1)*(2*m+1-k),k*(m+1))
                assert Jk-J0==Q(k*k-(2*m+1),k*m*(m+1))
                if k*k==2*m+1: ties+=1
                for a in range(1,k):
                    D=k*m+a*a-k*a+a
                    gap=Q(a*(k-a)*(2*m+1)*(k*(m+1)-a-1), k*k*m*(m+1)*D)
                    chord=Q(k-a,k)*J0+Q(a,k)*Jk
                    assert gap>0 and cv[a]-chord==gap,(m,k,a)
                    chords+=1
            else:
                F=2*m+1-k
                assert cv[opts[0]]==Q(F,m+1)
                for a in cv:
                    if a!=opts[0]:assert cv[a]>Q(F,m+1)
            total+=len(cv)
    # Independent exact rational inversion for all allocation orbit representatives.
    for m in range(2,8):
        n=m+1
        for k in range(1,2*m+1):
            for a in range(max(0,k-n),min(k,m)+1):
                selected=set(range(a)) | set(range(m,m+k-a))
                assert cost(m,k,a)==direct_cost(m,selected)
                direct+=1
    # Full combinatorial enumeration checks for each leader set on small graphs.
    for m in range(2,5):
        N=2*m+1
        for k in range(1,N):
            opts=expected_allocation(m,k)
            mincost=cost(m,k,opts[0])
            count=0
            for S in combinations(range(N),k):
                a=sum(v<m for v in S)
                c=direct_cost(m,set(S))
                assert c==cost(m,k,a)
                if c==mincost:count+=1
                allsets+=1
            target=sum(comb(m,a)*comb(m+1,k-a) for a in opts)
            assert count==target,(m,k,count,target)
    print(f'VERIFY_OK exact_allocation_cases={total} strict_chord_cases={chords} '
          f'direct_orbit_inversions={direct} full_subset_inversions={allsets} integer_tie_cases={ties}')

if __name__=='__main__':main()
