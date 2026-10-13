#!/usr/bin/env python3
import itertools
from collections import deque, Counter
from math import comb

def graph(k, ell):
    # vertices: a, x0..x{k-2}, p1..p{ell}
    V=['a']+[f'x{i}' for i in range(k-1)]+[f'p{i}' for i in range(1,ell+1)]
    idx={v:i for i,v in enumerate(V)}
    E=[]
    clique=[idx['a']]+[idx[f'x{i}'] for i in range(k-1)]
    for u,v in itertools.combinations(clique,2): E.append((u,v))
    prev=idx['a']
    for i in range(1,ell+1):
        cur=idx[f'p{i}']; E.append((prev,cur)); prev=cur
    adj=[set() for _ in V]
    for u,v in E: adj[u].add(v); adj[v].add(u)
    D=[]
    for s in range(len(V)):
        d=[10**9]*len(V); d[s]=0; q=deque([s])
        while q:
            u=q.popleft()
            for w in adj[u]:
                if d[w]>d[u]+1: d[w]=d[u]+1; q.append(w)
        D.append(d)
    return V,E,D

def is_edge_generator(S,E,D):
    seen=set()
    for u,v in E:
        sig=tuple(min(D[s][u],D[s][v]) for s in S)
        if sig in seen: return False
        seen.add(sig)
    return True

def criterion(mask,V,k,ell):
    X=[i for i,v in enumerate(V) if v.startswith('x')]
    P=[i for i,v in enumerate(V) if v.startswith('p')]
    omitted=sum(1 for i in X if not (mask>>i)&1)
    return omitted==0 or (omitted==1 and any((mask>>i)&1 for i in P))

def formula_coeff(k,ell):
    # x^(k-1)(1+x)^(ell+1) + (k-1)x^(k-2)(1+x)((1+x)^ell-1)
    c=Counter()
    for j in range(ell+2): c[k-1+j]+=comb(ell+1,j)
    for a in (0,1):
        for j in range(1,ell+1): c[k-2+a+j]+=(k-1)*comb(ell,j)
    return c

def main():
    subset_checks=criterion_checks=coefficient_checks=minimum_checks=0
    for k in range(3,7):
        for ell in range(1,6):
            V,E,D=graph(k,ell); N=len(V); got=Counter()
            good_masks=[]
            for mask in range(1<<N):
                subset_checks+=1
                S=[i for i in range(N) if (mask>>i)&1]
                direct=is_edge_generator(S,E,D)
                pred=criterion(mask,V,k,ell); criterion_checks+=1
                if direct!=pred:
                    raise AssertionError(('criterion',k,ell,mask,direct,pred))
                if direct:
                    got[len(S)]+=1; good_masks.append(mask)
            want=formula_coeff(k,ell)
            for d in range(N+1):
                coefficient_checks+=1
                if got[d]!=want[d]: raise AssertionError(('coeff',k,ell,d,got[d],want[d]))
            minimum_checks+=1
            mn=min(got)
            if mn!=k-1 or got[mn]!=1+(k-1)*ell:
                raise AssertionError(('minimum',k,ell,mn,got[mn]))
            total=sum(got.values())
            expected=2**(ell+1)+2*(k-1)*(2**ell-1)
            if total!=expected: raise AssertionError(('total',k,ell,total,expected))
            # a is in no minimum basis; every other vertex occurs in some minimum basis; none is forced.
            mins=[m for m in good_masks if m.bit_count()==mn]
            a=V.index('a')
            if any((m>>a)&1 for m in mins): raise AssertionError(('a-not-void',k,ell))
            for i,v in enumerate(V):
                if i==a: continue
                if not any((m>>i)&1 for m in mins): raise AssertionError(('unexpected-void',k,ell,v))
                if all((m>>i)&1 for m in mins): raise AssertionError(('unexpected-forced',k,ell,v))
    print(f'VERIFY_OK k_range=3..6 ell_range=1..5 subset_checks={subset_checks} criterion_checks={criterion_checks} coefficient_checks={coefficient_checks} minimum_checks={minimum_checks} max_order=11')
if __name__=='__main__': main()
