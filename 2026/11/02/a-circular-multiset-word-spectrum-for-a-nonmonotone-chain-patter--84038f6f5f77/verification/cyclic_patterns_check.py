#!/usr/bin/env python3
"""Independent checks for cyclic occurrence distributions of length-five patterns."""
from itertools import permutations, combinations, product
from collections import defaultdict, Counter
from fractions import Fraction
from math import comb, factorial
PATS=((1,2,4,3,5),(1,3,2,4,5))

def occurs(w,p):
    n=len(w); ans=0
    for s in range(n):
        a=[w[(s+j)%n] for j in range(5)]
        if len(set(a))!=5: continue
        red=tuple(1+sum(t<x for t in a) for x in a)
        ans+=red==p
    return ans

def direct(m,p):
    a=tuple(i+1 for i,c in enumerate(m) for _ in range(c))
    hist=Counter()
    for w in set(permutations(a)):
        hist[occurs(w,p)]+=1
    return hist

def clusters(n):
    out=[]
    for r in range(1,n):
        for ds in product((3,4),repeat=r-1):
            size=5+sum(ds)
            if size>n:continue
            out.append((size,r))
        if 5+3*r>n:break
    return Counter(out)

def rooted_circular_coeff(m):
    a=len(m); n=sum(m); z=(0,)*a
    atoms=[]
    for j in range(a):
        u=tuple(int(i==j) for i in range(a))
        atoms.append((u,0,1))
    for (size,r),mult in clusters(n).items():
        for idx in combinations(range(a),size):
            u=tuple(int(i in idx) for i in range(a))
            atoms.append((u,r,mult))
    cur={(z,0):1}; q=defaultdict(Fraction)
    for k in range(1,n+1):
        nex=defaultdict(int)
        for (u,r),val in cur.items():
            for v,s,mult in atoms:
                w=tuple(x+y for x,y in zip(u,v))
                if all(x<=cap for x,cap in zip(w,m)):
                    nex[(w,r+s)]+=val*mult
        cur=nex
        for (u,r),val in cur.items():
            if u==m:q[r]+=Fraction(n*val,k)
    assert all(v.denominator==1 for v in q.values()), q
    return dict((r,int(v)) for r,v in q.items())

def direct_marked(hist):
    q={}
    for r in range(0,max(hist)+1):q[r]=sum(comb(k,r)*v for k,v in hist.items() if k>=r)
    return {r:v for r,v in q.items() if v}

def check_overlap(p,rs=6):
    for r in range(1,rs+1):
        for gaps in product((3,4),repeat=r-1):
            ss=[0]
            for gap in gaps:ss.append(ss[-1]+gap)
            n=ss[-1]+5
            reach=[[False]*n for _ in range(n)]
            for s in ss:
                for i in range(5):
                    for j in range(5):
                        if p[i]<p[j]:reach[s+i][s+j]=True
            for k in range(n):
                for i in range(n):
                    if reach[i][k]:
                        for j in range(n):reach[i][j]|=reach[k][j]
            assert all(reach[i][j] != reach[j][i] for i in range(n) for j in range(i)),(p,gaps)
    return True

def main():
    cases=[(1,1,1,1,1),(2,1,1,1,1),(1,2,1,1,1),(2,2,1,1,1),
           (1,1,1,1,1,1,1,1),(2,1,1,1,1,1,1,1)]
    total=0
    for p in PATS:check_overlap(p)
    for m in cases:
        g=rooted_circular_coeff(m)
        for p in PATS:
            hist=direct(m,p); total+=sum(hist.values())
            q=direct_marked(hist)
            assert g==q,(m,p,g,q,hist)
            print('OK',m,''.join(map(str,p)), 'hist',sorted(hist.items()),'marked',sorted(q.items()))
    print('VERIFY_OK cyclic_exact_graphic_marked_formula total_direct_words',total,'induced_overlap_orders_r_to_6',sum(2**(r-1) for r in range(1,7))*2)
if __name__=='__main__':main()
