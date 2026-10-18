#!/usr/bin/env python3
"""Exact Laurent-polynomial short-time checks for a flux-threaded unicyclic network."""
from collections import defaultdict
from fractions import Fraction
from math import factorial
from itertools import product

def build_graph(m,d,twigs=False,weighted=True):
    assert m>=3 and d>=0
    n=m+d+(2 if twigs else 0)
    edges=[]
    for j in range(m):
        edges.append((j,(j+1)%m,2 if weighted and j%2==0 else 1,1 if j==m-1 else 0))
    for t in range(d):
        edges.append((m-1 if t==0 else m+t-1,m+t,3 if weighted and t%2==0 else 1,0))
    if twigs:
        edges += [(0,m+d,2,0), (m//2,m+d+1,3,0)]
    start=(m+d-1 if d else 0)
    return n,edges,start

def multiply(a,b):
    c=defaultdict(int)
    for k,x in a.items():
        for j,y in b.items(): c[k+j]+=x*y
    return {k:v for k,v in c.items() if v}

def moments(n,edges,start,maxorder):
    adj=[[] for _ in range(n)]
    for u,v,w,flux in edges:
        adj[u].append((v,w,flux))
        adj[v].append((u,w,-flux))
    # row evolving, path weights commute (only one loop flux)
    vectors=[{0:1} if v==start else {} for v in range(n)]
    out=[vectors[start]]
    for r in range(maxorder):
        new=[defaultdict(int) for _ in range(n)]
        for u in range(n):
            for v,w,p in adj[u]:
                for k,c in vectors[u].items():new[v][k+p]+=w*c
        vectors=[{k:v for k,v in row.items() if v} for row in new]
        out.append(vectors[start])
    return out

def return_probability_coefficients(mom,K):
    out=[]
    for j in range(K+1):
        c=defaultdict(Fraction)
        for p in range(j+1):
            q=j-p
            # (-i)^p (i)^q / (p!q!) relative to imaginary powers
            # j even only: i^(q-p) = (-1)^((q-p)/2)
            if j%2:continue
            factor=Fraction((1 if ((q-p)//2)%2==0 else -1),factorial(p)*factorial(q))
            for e,v in multiply(mom[p],mom[q]).items():c[e]+=factor*v
        out.append({e:v for e,v in c.items() if v})
    return out

def check_case(m,d,twigs,weighted):
    n,edges,root=build_graph(m,d,twigs,weighted)
    K=(m+2*d if m%2==0 else 2*(m+d))
    P=return_probability_coefficients(moments(n,edges,root,K),K)
    for r in range(K):
        assert all(e==0 for e in P[r]), (m,d,r,P[r])
    C=1;path=1
    for u,v,w,f in edges:
        if u<m and v<m:C*=w
        elif u>=m or v>=m:
            if (u==m-1 and v==m) or (m<=u<m+d and m<=v<m+d):path*=w
    if m%2==0:
        ex=Fraction(2*((-1)**(K//2))*C*path**2,factorial(K))
        exponent=1
    elif d>0:
        ex=Fraction(2*((-1)**(m+d))*C**2*path**2,factorial(K))
        exponent=2
    else:
        ex=C**2*(Fraction(1,factorial(m)**2)-Fraction(2,factorial(2*m)))
        exponent=2
    assert P[K].get(exponent,Fraction(0))==ex,(m,d,P[K],ex)
    assert P[K].get(-exponent,Fraction(0))==ex,(m,d,P[K],ex)
    assert all(e in (0,exponent,-exponent) for e in P[K]),(m,d,P[K])
    return n,K,ex

def main():
    checks=[]
    for m,d,twigs,weighted in product(range(3,9),range(4),(False,True),(False,True)):
        checks.append(check_case(m,d,twigs,weighted))
    print('VERIFY_OK rooted_unicyclic_profiles=',len(checks), 'lengths=',min(x[0] for x in checks),'..',max(x[0] for x in checks), 'orders=',min(x[1] for x in checks),'..',max(x[1] for x in checks))
if __name__=='__main__':main()
