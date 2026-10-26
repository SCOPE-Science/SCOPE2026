#!/usr/bin/env python3
"""Finite independent checks for three-factor Hamming total mutual visibility."""
from itertools import product,combinations,permutations
from collections import deque
from math import factorial

def restricted_stirling(m,r):
    total=0
    for labels in product(range(r), repeat=m):
        if set(labels)!=set(range(r)) or any(labels.count(j)<2 for j in range(r)): continue
        # Canonical first-occurrence partition labels remove relabeling duplicates
        seen={}; norm=[]
        for v in labels:
            if v not in seen:seen[v]=len(seen)
            norm.append(seen[v])
        if tuple(norm)==labels:total+=1
    return total

def predicted(q):
    m=min(q);total=0
    for i,x in enumerate(q):
        if x!=m:continue
        j,k=[v for p,v in enumerate(q) if p!=i]
        for r in range(1,m//2+1):
            total+=restricted_stirling(m,r)*(factorial(j)//factorial(j-r))*(factorial(k)//factorial(k-r))
    if len(set(q))==1:total+=factorial(m)**2
    return total

def distance(u,v):return sum(x!=y for x,y in zip(u,v))

def observed(q):
    vertices=list(product(*(range(t) for t in q)))
    masks=[]
    for u in vertices:
        mask=0
        for j,v in enumerate(vertices):
            if distance(u,v)==2:mask|=1<<j
        masks.append(mask)
    allv=(1<<len(vertices))-1; answer=0
    for ids in combinations(range(len(vertices)), min(q)):
        if any(masks[i] & (1<<j) for i,j in combinations(ids,2)):continue
        covered=0
        for i in ids:covered|=masks[i]|(1<<i)
        if covered==allv:answer+=1
    return answer

def shortest_avoid(vertices,u,v,X):
    # Direct shortest-path existence rather than using a distance-two characterization.
    d=distance(u,v)
    if d==0:return True
    U=set(X); seen={u};queue=deque([(u,0)])
    while queue:
        at,k=queue.popleft()
        for nxt in vertices:
            if distance(at,nxt)!=1 or distance(nxt,v)!=d-k-1:continue
            if nxt==v:return True
            if nxt in U or nxt in seen:continue
            seen.add(nxt);queue.append((nxt,k+1))
    return False

def check_definition(q):
    vertices=list(product(*(range(t) for t in q)));n=len(vertices)
    for mask in range(1<<n):
        X={vertices[i] for i in range(n) if (mask>>i)&1}
        indirect=all(distance(u,v)!=2 for u,v in combinations(X,2))
        direct=all(shortest_avoid(vertices,u,v,X) for u in vertices for v in vertices)
        assert direct==indirect, (q,mask)
    return 1<<n

def main():
    print('Direct original geodesic-definition vs distance-two criterion:')
    print('q=(2,2,2), all subsets:',check_definition((2,2,2)))
    print('Exhaustive independent counts at minimum cardinality:')
    for q in ((2,2,2),(2,2,3),(3,3,3),(3,3,4),(4,4,4),(4,4,5)):
        a=observed(q);b=predicted(q)
        assert a==b,(q,a,b)
        print('q=%s observed=%s formula=%s PASS'%(q,a,b))
    print('ALL CHECKS PASSED; tests finite, not an infinite proof.')
if __name__=='__main__':main()
