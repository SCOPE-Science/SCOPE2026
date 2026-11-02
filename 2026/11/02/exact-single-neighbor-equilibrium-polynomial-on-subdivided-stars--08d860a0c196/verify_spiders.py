"""Exact finite checks for single-neighbor public-goods equilibria on spiders.

The exhaustive tests are finite corroboration of a separate all-arm-length proof.
"""
from itertools import product
from collections import Counter
from math import prod

def spider_graph(lengths):
    edges=[]; v=1
    for length in lengths:
        prev=0
        for j in range(length):
            edges.append((prev,v));prev=v;v+=1
    neighbors=[[] for _ in range(v)]
    for a,b in edges:
        neighbors[a].append(b);neighbors[b].append(a)
    return neighbors

def predicted(lengths):
    I2=[ell for ell in lengths if ell%3==2]
    I1=[ell for ell in lengths if ell%3==1]
    polynomial=Counter({0:1})
    for ell in I2:
        w=2*(ell+1)//3
        q=Counter(polynomial)
        for e,n in polynomial.items():q[e+w]+=n
        polynomial=q
    for ell in I2:
        w=2*(ell+1)//3
        polynomial[w]-=1
        if polynomial[w]==0:del polynomial[w]
    if not I2 and len(I1)==1:
        power=2+2*sum(ell//3 for ell in lengths)
        polynomial[power]+=1
    return +polynomial

def observed(lengths):
    nb=spider_graph(lengths)
    N=len(nb)
    pol=Counter()
    for mask in range(1<<N):
        if all(bool(mask&(1<<i)) == (sum(bool(mask&(1<<j)) for j in adj)==1) for i,adj in enumerate(nb)):
            pol[mask.bit_count()]+=1
    return pol

def run():
    tests=0;states=0
    for k in (3,4,5):
        for lengths in product(range(1,7 if k==3 else 5 if k==4 else 4),repeat=k):
            N=1+sum(lengths)
            if N>16:continue
            pred=predicted(lengths)
            obs=observed(lengths)
            if pred!=obs:
                raise AssertionError((lengths,pred,obs))
            tests+=1
            states+=(1<<N)
    print('PASS',tests,'spider instances;',states,'binary profiles exhaustively checked')
    samples=((2,2,2),(2,3,3),(1,3,3),(1,1,3),(2,2,5),(4,6,9),(1,2,3),(1,3,6))
    for lengths in samples:
        print(lengths,dict(sorted(predicted(lengths).items())))
if __name__=='__main__':run()
