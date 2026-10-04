#!/usr/bin/env python3
from itertools import combinations
from math import gcd

def is_zero_divisor(a,n):
    return any((a*b)%n==0 for b in range(1,n))

def torsion_set_regular_zn(n):
    # M=R=Z/nZ.  m is torsion iff rm=0 for some nonzero r.
    return {m for m in range(n) if any((r*m)%n==0 for r in range(1,n))}

def graph_t0_zn(n):
    T=torsion_set_regular_zn(n)
    V=list(range(1,n))
    adj=[set() for _ in V]
    for i,x in enumerate(V):
        for j in range(i+1,len(V)):
            y=V[j]
            if (x+y)%n in T:
                adj[i].add(j); adj[j].add(i)
    return T,V,adj

def total_dom(S,adj):
    S=set(S)
    return all(bool(adj[v] & S) for v in range(len(adj)))

def pm(S,adj):
    S=set(S)
    if not S: return True
    if len(S)%2: return False
    v=next(iter(S))
    for u in list(adj[v] & S):
        if pm(S-{v,u},adj):
            return True
    return False

def paired_dom(S,adj):
    S=set(S)
    # matching in G[S] plus ordinary domination
    if not pm(S,adj): return False
    return all(v in S or bool(adj[v] & S) for v in range(len(adj)))

def minima(adj):
    N=len(adj)
    if N and any(len(a)==0 for a in adj):
        return None,None
    if N==0:
        return 0,0
    gt=gp=None
    for k in range(1,N+1):
        if gt is None:
            for S in combinations(range(N),k):
                if total_dom(S,adj): gt=k; break
        if gp is None and k%2==0:
            for S in combinations(range(N),k):
                if paired_dom(S,adj): gp=k; break
        if gt is not None and gp is not None: break
    return gt,gp

def expected(alpha,beta,two_zd):
    if alpha==2 or (alpha==1 and two_zd):
        return None,None
    if alpha==1:
        return beta-1,beta-1
    if two_zd:
        return 2*beta,2*beta
    return beta+1,beta+1

rows=[]
for n in [2,3,4,5,8,9]:
    T,V,adj=graph_t0_zn(n)
    alpha=len(T); beta=n//alpha
    two_zd=is_zero_divisor(2%n,n)
    gt,gp=minima(adj)
    exp=expected(alpha,beta,two_zd)
    assert (gt,gp)==exp,(n,T,alpha,beta,two_zd,gt,gp,exp)
    rows.append((n,alpha,beta,two_zd,gt,gp,sorted(len(a) for a in adj)))

# Abstract component-level replay over all admissible finite parameter profiles
# in a bounded grid.  In the second branch beta must be odd because nonzero
# quotient cosets pair with their negatives.
profiles=0
for alpha in range(1,9):
    for beta in range(1,10):
        for two_zd in [False,True]:
            if alpha==1 and beta==1: continue
            if (not two_zd) and beta%2==0: continue
            comps=[]
            if alpha-1>0: comps.append(('K',alpha-1))
            if two_zd:
                comps += [('K',alpha)]*(beta-1)
            else:
                comps += [('B',alpha)]*((beta-1)//2)
            isolated=any((typ=='K' and m==1) for typ,m in comps)
            if isolated:
                calc=(None,None)
            else:
                nonempty=[c for c in comps if not (c[0]=='K' and c[1]==0)]
                calc=(2*len(nonempty),2*len(nonempty)) if nonempty else (0,0)
            assert calc==expected(alpha,beta,two_zd),(alpha,beta,two_zd,calc,expected(alpha,beta,two_zd))
            profiles+=1

print('VERIFY_OK')
for row in rows:
    print('Zmod_case='+repr(row))
print('abstract_parameter_profiles_checked='+str(profiles))
