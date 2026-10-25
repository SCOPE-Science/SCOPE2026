#!/usr/bin/env python3
"""Independent finite enumeration for cycle-power clique/Alexander-dual complexes."""
from collections import defaultdict
from math import comb

def cliques(n,p):
    nb=[]
    for i in range(n):
        nb.append(sum(1<<j for j in range(n) if j!=i and min((i-j)%n,(j-i)%n)<=p))
    levels=defaultdict(list)
    def recur(mask,candidates,depth):
        for i in range(n):
            if (candidates>>i)&1:
                b=mask|(1<<i)
                levels[depth].append(b)
                recur(b,candidates & nb[i] & ~((1<<(i+1))-1),depth+1)
    recur(0,(1<<n)-1,0)
    return levels

def rank_mod2(cols):
    pivots={}
    for v in cols:
        while v:
            k=v.bit_length()-1
            if k in pivots: v^=pivots[k]
            else: pivots[k]=v;break
    return len(pivots)

def reduced_betti(levels):
    degrees=sorted(levels)
    prev_rank=0
    # dimension k: number k-simplices rank boundary d_k, rank boundary d_{k+1}.
    ranks={}
    for k in degrees:
        if k==0: ranks[k]=0;continue
        rows={f:i for i,f in enumerate(levels[k-1])}
        cols=[]
        for f in levels[k]:
            z=0; m=f
            while m:
                b=m&-m;m-=b;z|=1<<rows[f^b]
            cols.append(z)
        ranks[k]=rank_mod2(cols)
    top=max(degrees)
    return {k:len(levels[k])-ranks[k]-ranks.get(k+1,0)-(1 if k==0 else 0) for k in degrees if len(levels[k])-ranks[k]-ranks.get(k+1,0)-(1 if k==0 else 0)}

def expected(n,p):
    m=n-2*p
    r=p//m
    if p%m==0:
        return {n-2*r-3:m-1}, {2*r:m-1}
    return {n-2*r-4:1}, {2*r+1:1}

def verify_clique():
    cases=0;faces=0
    for p in range(3,8):
        for n in range(2*p+3,min(3*p,21)+1):
            L=cliques(n,p)
            faces+=sum(map(len,L.values()))
            actual=reduced_betti(L)
            K, predicted=expected(n,p)
            assert actual==predicted,(n,p,actual,predicted)
            print('CLIQUE',n,p, 'homology',actual,'faces',sum(map(len,L.values())))
            cases+=1
    return cases,faces

def direct_dual(n,p):
    L=cliques(n,p)
    cl={0} | set(f for group in L.values() for f in group)
    full=(1<<n)-1
    A=defaultdict(list)
    for f in range(1,1<<n):
        if (full^f) not in cl:
            A[f.bit_count()-1].append(f)
    return A

def verify_dual():
    # Three independently generated Alexander-dual chain complexes, no use of a duality formula in computation.
    checked=0;faces=0
    for n,p in [(9,3),(11,4),(12,4)]:
        A=direct_dual(n,p)
        betti=reduced_betti(A)
        exp,_=expected(n,p)
        assert betti==exp,(n,p,betti,exp)
        c=sum(map(len,A.values()))
        faces+=c;checked+=1
        print('DIRECT_DUAL',n,p,'homology',betti,'faces',c)
    return checked,faces

if __name__=='__main__':
    a,b=verify_clique()
    c,d=verify_dual()
    print('SUMMARY clique_cases',a,'clique_faces',b,'dual_cases',c,'dual_faces',d)

# Independent signed fixed-simplex Lefschetz check of the new representation formula.
from math import gcd

def check_character():
    tests=0
    for p in range(3,8):
        for n in range(2*p+3,min(3*p,21)+1):
            C=cliques(n,p)
            m=n-2*p
            j=2*(p//m)+(0 if p%m==0 else 1)
            for a in range(n):
                h=gcd(n,a);t=n//h
                ff=-1
                for k,faces in C.items():
                    for S in faces:
                        moved=0
                        for i in range(n):
                            if S>>i&1: moved|=1<<((i+a)%n)
                        if S==moved:
                            if t%2:
                                # Odd cycle permutes vertices evenly on every invariant orbit.
                                orientation=1
                            else:
                                orientation=(-1)**(S.bit_count()//t)
                            ff+=(-1)**k*orientation
                measured=(-1)**j * (-1)**(n-h)*ff
                predicted= (-1)**(n-h)*((m-1) if (h%m==0) else -1) if p%m==0 else (-1)**(n-h)
                assert measured==predicted, (n,p,a,ff,measured,predicted)
                tests+=1
    print('SIGNED_ROTATION_CHECKS',tests)
    return tests

if __name__=='__main__':
    check_character()
    print("VERIFY_OK")
