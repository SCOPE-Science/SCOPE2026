#!/usr/bin/env python3
"""Exact checks for electrical cut-space projection on multipartite graphs.

Run: python verify_electrical_multipartite.py
Requires sympy. Comparisons use rational arithmetic, not floating point.
"""
from fractions import Fraction
from itertools import combinations
from sympy import Matrix, Rational

def partitions(n, high=None):
    if high is None:
        high=n
    if n==0:
        yield ()
        return
    for k in range(min(high,n),0,-1):
        for tail in partitions(n-k,k):
            yield (k,)+tail

def g(n,s):
    return Fraction(n+s-2)-Fraction(2*(s-1),n-s)

def formula(n, parts):
    return max((g(n,a)+g(n,b))/n for a,b in combinations(parts,2))

def signed_edges(parts):
    owner=[j for j,m in enumerate(parts) for _ in range(m)]
    return [(i,j) for i in range(len(owner)) for j in range(i+1,len(owner)) if owner[i]!=owner[j]]

def direct_norm(parts):
    n=sum(parts)
    edges=signed_edges(parts)
    L=[[0 for _ in range(n)] for _ in range(n)]
    for i,j in edges:
        L[i][i]+=1;L[j][j]+=1;L[i][j]-=1;L[j][i]-=1
    inv=Matrix([row[:-1] for row in L[:-1]]).inv()
    vecs=[]
    for i,j in edges:
        b=Matrix([int(t==i)-int(t==j) for t in range(n-1)])
        vecs.append(b)
    return max(sum(abs((bi.T*inv*bj)[0]) for bj in vecs) for bi in vecs)

def winner_formula(n):
    if n==3:
        return Fraction(4,3)
    if n==5:
        return Fraction(26,15)
    if n%2==0:
        return Fraction(3)-Fraction(8,n)+Fraction(8,n*n)
    return Fraction(3)-Fraction(8,n+1)

def main():
    verified=0
    for n in range(2,10):
        for parts in partitions(n):
            if len(parts)<2: continue
            v=direct_norm(parts)
            ref=formula(n,parts)
            assert v==ref,(n,parts,v,ref)
            verified+=1
    winners={2:[(1,1)],3:[(1,1,1)],4:[(2,2),(2,1,1),(1,1,1,1)],5:[(2,2,1)],6:[(3,3)],7:[(4,3),(3,3,1)]}
    for n in range(2,26):
        data=[(formula(n,p),p) for p in partitions(n) if len(p)>=2]
        mx=max(x for x,p in data)
        want=winner_formula(n)
        assert mx==want,(n,mx,want)
        actual=[p for v,p in data if v==mx]
        if n in winners: assert actual==winners[n],(n,actual,winners[n])
        else: assert actual==[(n//2+(n%2),n//2)],(n,actual)
    print(f'PASS: {verified} independent exact Laplacian-pseudoinverse norm comparisons for all multipartite partitions with 2<=N<=9.')
    print('PASS: all exact maximizing values and graph profiles for 2<=N<=25.')
    for n in [3,4,5,6,7,8,9,12,25]:
        print('N=',n,' maximum=',str(winner_formula(n)))
if __name__=='__main__':main()
