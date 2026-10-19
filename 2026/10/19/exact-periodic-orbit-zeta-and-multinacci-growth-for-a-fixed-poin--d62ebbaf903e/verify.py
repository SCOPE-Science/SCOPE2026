"""Exact-rational finite sanity checks for a discontinuous interval map.

All infinite-period statements require the accompanying mathematical proof.
Requires only Python 3 standard library. Run: python verify.py
"""
from fractions import Fraction
from collections import defaultdict


def branches(k):
    # Cells in increasing order: negative outer through negative inner,
    # then positive inner through positive outer. Domain [-k,k).
    out = []
    for i in range(2*k):
        lo = i-k
        hi = lo+1
        if i == k-1:
            a,b,targets = k,k,tuple(range(k,2*k))
        elif i == k:
            a,b,targets = k,-k,tuple(range(0,k))
        elif i < k:
            a,b,targets = 1,1,(i+1,)
        else:
            a,b,targets = 1,-1,(i-1,)
        out.append((lo,hi,a,b,targets))
    return out


def actual_map(k,x):
    assert -k <= x < k
    if x < -1: return x+1
    if x < 0: return k*x+k
    if x < 1: return k*x-k
    return x-1


def count(k,n):
    data=branches(k)
    marked=set()
    trace=0
    def cycle(prefix):
        nonlocal trace
        if len(prefix)==n:
            if prefix[0] not in data[prefix[-1]][4]:
                return
            trace+=1
            a,b=1,0
            for index in prefix:
                cell=data[index]
                a,b=cell[2]*a,cell[2]*b+cell[3]
            x=Fraction(-b,a-1)
            y=x
            for index in prefix:
                lo,hi,_,_,_=data[index]
                if not (lo<=y<hi):return
                y=actual_map(k,y)
            if y==x:marked.add(x)
            return
        for nxt in data[prefix[-1]][4]:
            cycle(prefix+[nxt])
    for start in range(2*k):cycle([start])
    return trace,len(marked)


def main():
    checks=0
    for k in range(2,6):
        cells=branches(k)
        # Check each noncentral branch maps its unit cell exactly onto its listed target.
        for i,(lo,hi,a,b,targets) in enumerate(cells):
            assert a*lo+b==cells[targets[0]][0]
            assert a*hi+b==cells[targets[-1]][1]
            checks+=2
        for n in range(1,11):
            graph,actual=count(k,n)
            predicted=graph-(k+1 if n%(k+1)==0 else 0)
            assert actual==predicted,(k,n,graph,actual,predicted)
            checks+=1
            if n>=2:assert actual>0
    print(f"PASS: {checks} exact finite checks, k=2..5, periods 1..10")
    print("The proof, not this finite test, establishes all k>=2 and all periods.")

if __name__=='__main__':main()
