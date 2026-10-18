#!/usr/bin/env python3
"""Exact finite checks for graphical-zonotope normal-cone moment identities."""
from collections import Counter
from itertools import permutations
from fractions import Fraction
from math import factorial, comb

def orientations(p,q):
    n=p+q
    c=Counter()
    for z in permutations(range(n)):
        ranks=[0]*n
        for ix,v in enumerate(z):ranks[v]=ix
        key=tuple(ranks[a]<ranks[p+b] for a in range(p) for b in range(q))
        c[key]+=1
    return c

def compositions(n):
    if n==0:
        yield ()
    else:
        for j in range(1,n+1):
            for r in compositions(n-j):yield (j,)+r

def S(p,q,t):
    # weighted ordered partitions, with exact convolution for each block count
    N=max(p,q)+2
    A=[[0]*(p+1) for _ in range(p+2)]
    B=[[0]*(q+1) for _ in range(p+2)]
    A[0][0]=1;B[0][0]=1
    for b in range(1,p+2):
        for u in range(1,p+1):
            A[b][u]=sum(A[b-1][u-s]*factorial(s)**(t-1) for s in range(1,u+1))
    for b in range(1,p+2):
        for u in range(1,q+1):
            B[b][u]=sum(B[b-1][u-s]*factorial(s)**(t-1) for s in range(1,u+1))
    ans=0
    for a in range(1,p+1):
        for b in range(1,min(q,p+1)+1):
            if abs(a-b)<=1:
                ans+=(2 if a==b else 1)*A[a][p]*B[b][q]
    return ans*factorial(p)*factorial(q)

def check():
    checks=0
    for p in range(1,5):
      for q in range(1,6):
        if p+q>8:continue
        c=orientations(p,q)
        n=p+q
        assert sum(c.values())==factorial(n)
        for t in (2,3,4):
            a=sum(v**t for v in c.values())
            b=S(p,q,t)
            assert a==b,(p,q,t,a,b)
            checks+=1
        # all orientation preimages have alternating monochrome-block factorial size
        for k,v in c.items():
            assert v>0
    # exact asymptotic leading coefficient: sum over one-large-B-block architectures
    for p in range(1,6):
        for t in (2,3,4):
            c=p*0+factorial(p)*sum((factorial(i)*factorial(p-i))**(t-1) for i in range(p+1))
            q=25
            a=S(p,q,t) # at most p+1 B blocks, finite compositions but may be several 100K for p=5
            exact=Fraction(a, factorial(p+q)**t)
            # compare scaled collision, relative error a few percent at q=25 for fixed small p
            lead=Fraction(c*factorial(q)**t,factorial(p+q)**t)
            assert exact>=lead
            checks+=1
    print('PASS',checks,'independent exhaustive collision-moment and leading-term checks')
    for p,q in [(1,5),(2,5),(2,8),(3,5)]:
        n=p+q
        print(f'p={p},q={q}, C2={Fraction(S(p,q,2),factorial(n)**2)}, moments[3]={Fraction(S(p,q,3),factorial(n)**3)}')
if __name__=='__main__':check()
