#!/usr/bin/env python3
from itertools import combinations
from fractions import Fraction
from collections import deque, Counter, defaultdict

def distances(n, edges):
    adj=[[] for _ in range(n)]
    for u,v in edges:
        adj[u].append(v); adj[v].append(u)
    all_d=[]
    for s in range(n):
        d=[-1]*n; d[s]=0; q=deque([s])
        while q:
            u=q.popleft()
            for v in adj[u]:
                if d[v]<0:
                    d[v]=d[u]+1; q.append(v)
        if -1 in d:
            return None
        for t in range(s+1,n):
            all_d.append(d[t])
    return tuple(sorted(all_d))

def L_E(hist):
    q=len(hist)
    return Fraction(sum(hist),q), sum((Fraction(1,d) for d in hist),Fraction())/q

def sign(x): return (x>0)-(x<0)

connected_counts={}
metric_counts={}
weak_counts={}
for n in range(2,7):
    poss=list(combinations(range(n),2))
    by_m=defaultdict(set)
    c=0
    for mask in range(1<<len(poss)):
        if mask.bit_count()<n-1: continue
        edges=[poss[i] for i in range(len(poss)) if (mask>>i)&1]
        hist=distances(n,edges)
        if hist is None: continue
        c+=1
        by_m[len(edges)].add(L_E(hist))
    connected_counts[n]=c
    strict=0; weak=0
    for m,vals in by_m.items():
        vals=list(vals)
        for (L1,E1),(L2,E2) in combinations(vals,2):
            dL=sign(L1-L2); dE=sign(E1-E2)
            # Lower L is better; higher E is better. Same-sign changes are strict ranking reversals.
            if dL*dE>0: strict+=1
            if (dL==0)!=(dE==0): weak+=1
    metric_counts[n]=strict
    weak_counts[n]=weak

assert connected_counts=={2:1,3:4,4:38,5:728,6:26704}
assert metric_counts=={2:0,3:0,4:0,5:0,6:0}

A=[(0,4),(1,2),(1,3),(1,4),(2,5),(2,6),(5,6)]
B=[(0,1),(0,2),(0,5),(1,4),(2,3),(3,5),(3,6)]
hA=distances(7,A); hB=distances(7,B)
assert Counter(hA)==Counter({1:7,2:6,3:6,4:2})
assert Counter(hB)==Counter({1:7,2:7,3:4,4:2,5:1})
LA,EA=L_E(hA); LB,EB=L_E(hB)
assert (LA,EA)==(Fraction(15,7),Fraction(25,42))
assert (LB,EB)==(Fraction(46,21),Fraction(188,315))
assert LA<LB and EA<EB
assert LB-LA==Fraction(1,21)
assert EB-EA==Fraction(1,630)

def degrees(n,edges):
    d=[0]*n
    for u,v in edges:d[u]+=1;d[v]+=1
    return tuple(sorted(d))
assert degrees(7,A)==degrees(7,B)==(1,1,2,2,2,3,3)

print('VERIFY_OK')
print('connected_labeled_counts', connected_counts)
print('strict_reversal_metric_pair_counts_n_le_6', metric_counts)
print('weak_tie_split_metric_pair_counts_n_le_6', weak_counts)
print('A_distance_histogram', dict(sorted(Counter(hA).items())))
print('B_distance_histogram', dict(sorted(Counter(hB).items())))
print('A_L_E', LA, EA)
print('B_L_E', LB, EB)
print('differences', LB-LA, EB-EA)
print('common_degree_sequence', degrees(7,A))
