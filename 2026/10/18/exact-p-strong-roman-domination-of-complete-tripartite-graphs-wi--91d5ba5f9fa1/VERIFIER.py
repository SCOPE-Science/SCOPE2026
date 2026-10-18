#!/usr/bin/env python3
"""Independent finite checks of p-strong Roman domination on complete tripartite graphs.
Run: python3 VERIFIER.py (Python standard library only).
"""
from itertools import product
from math import ceil
from collections import Counter


def ceil_div(a,b):
    return (a+b-1)//b


def predicted(parts,p):
    N=sum(parts)
    W1=[parts[i]+ceil_div(N-parts[i],p) for i in range(3)]
    W2=[]; W3=[]
    for i in range(3):
        for j in range(i+1,3):
            W2.append(2+ceil_div(N-parts[i]-1,p)+ceil_div(N-parts[j]-1,p))
            W3.append(3+ceil_div(N-parts[i]-2,p)+ceil_div(N-parts[j]-2,p))
    return min(W1+W2+W3), min(W1),min(W2),min(W3)


def direct(f,parts,p):
    group=[]
    for i,n in enumerate(parts):group.extend([i]*n)
    Z=[sum(f[v]==0 for v in range(len(f)) if group[v]==i) for i in range(3)]
    for u,x in enumerate(f):
        if x!=0:continue
        if not any(group[v]!=group[u] and f[v]>=1+ceil_div(sum(Z)-Z[group[v]],p)
                   for v in range(len(f))):
            return False
    return True


def exhaustive(parts,p):
    N=sum(parts); Delta=N-min(parts)
    cap=1+ceil_div(Delta,p)
    best=N+1; count=0; cases=0
    for f in product(range(cap+1),repeat=N):
        cases+=1
        w=sum(f)
        if w>best:continue
        if direct(f,parts,p):
            if w<best:
                best=w;count=1
            elif w==best:count+=1
    return best,count,cases


def low_weight_count(parts,p,target):
    # Counts all labelings of weight <=target, independent of the formula.
    from itertools import combinations
    N=sum(parts);Delta=N-min(parts);cap=1+ceil_div(Delta,p)
    count=0;lower=0
    for r in range(1,min(target,N)+1):
        for positions in combinations(range(N),r):
            for labels in product(range(1,cap+1),repeat=r):
                w=sum(labels)
                if w>target:continue
                f=[0]*N
                for i,label in zip(positions,labels):f[i]=label
                if direct(f,parts,p):
                    if w==target:count+=1
                    else:lower+=1
    return count,lower


def main():
    cases=[((2,2,2),3),((2,2,3),3),((2,2,4),3),((2,3,3),3),
           ((3,3,3),3),((2,2,2),4),((2,3,3),4),((3,3,3),4),
           ((2,2,3),6),((3,3,3),6)]
    total=0
    for parts,p in cases:
        actual,count,checked=exhaustive(parts,p)
        prediction=predicted(parts,p)[0]
        assert actual==prediction,(parts,p,actual,prediction)
        total+=checked
        print(f"PASS parts={parts} p={p}: optimum={actual}; minimum functions={count}; evaluated={checked}")
    for a in (4,5,6,7):
        p=2*a-2
        count,below=low_weight_count((a,a,a),p,5)
        assert (below,count)==(0,3*a*a*a),(a,p,below,count)
        print(f"PASS sharp family a={a} p={p}: weight<5 count=0, weight5 count={count}")
    for a in range(4,101):
        p=2*a-2
        v,w1,w2,w3=predicted((a,a,a),p)
        assert v==5 and w1>=6 and w2==6 and w3==5
    print(f"ALL PASS; {total} labelled assignments, 4 low-weight enumerations and 97 numerical threshold comparisons")

if __name__=='__main__':main()
