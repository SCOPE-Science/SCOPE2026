#!/usr/bin/env python3
"""Reproducible tests of ancestry-frontier collision identities in uniform 2-DAGs."""
from collections import Counter
from fractions import Fraction
from itertools import product
from math import comb, floor
import random

checks=0

def insist(condition, message):
    global checks
    checks+=1
    if not condition: raise AssertionError(message)

def stirling2(n,k):
    if n==0: return int(k==0)
    if k==0 or k>n: return 0
    row=[0]*(k+1)
    row[0]=1
    for t in range(1,n+1):
        nxt=[0]*(k+1)
        for j in range(1,min(t,k)+1):
            nxt[j]=j*row[j]+row[j-1]
        row=nxt
    return row[k]

def rising_fall(m,r):
    z=1
    for k in range(r): z*=m-k
    return z

def direct(n,m):
    counts=Counter()
    arities=[(k-1)**2 for k in range(m+1,n+1)]
    for choices in product(*(range(a) for a in arities)):
        parents={k: divmod(a,k-1) for k,a in zip(range(m+1,n+1), choices)}
        parents={k:(v[0]+1,v[1]+1) for k,v in parents.items()}
        frontier={n}
        seen=set()
        edges=[]
        while frontier:
            node=frontier.pop()
            if node in seen: continue
            seen.add(node)
            if node>m:
                for p in parents[node]:
                    edges.append((node,p))
                    frontier.add(p)
        counts_end=Counter(v for u,v in edges if v>m)
        D=sum(z-1 for z in counts_end.values())
        root_edges=[v for u,v in edges if v<=m]
        Y=len(root_edges)
        E=Y-len(set(root_edges))
        X=len(seen)
        insist(X==2*Y-1+D-E,'ancestral edge conservation')
        counts[Y,D,E,X]+=1
    return {key:Fraction(value,sum(counts.values())) for key,value in counts.items()}

def recursive(n,m):
    states={(2,0,1):Fraction(1)} # (frontier edges, internal surplus hits, non-root red vertices)
    for k in range(n-1,m,-1):
        nex={}
        for (y,d,r),p in states.items():
            for z in range(y+1):
                q=Fraction(comb(y,z)*(k-1)**(y-z),k**y)
                j=int(z>0)
                key=(y-z+2*j,d+max(z-1,0),r+j)
                nex[key]=nex.get(key,Fraction(0))+p*q
        states=nex
    ans=Counter()
    for (y,d,r),p in states.items():
        for distinct in range(1,min(y,m)+1):
            q=Fraction(stirling2(y,distinct)*rising_fall(m,distinct),m**y)
            e=y-distinct
            x=r+distinct
            insist(x==2*y-1+d-e,'recurrence edge conservation')
            ans[y,d,e,x]+=p*q
    insist(sum(ans.values())==1,'recursion probabilities')
    return ans

for n in range(4,7):
    m=2
    a=direct(n,m)
    b=recursive(n,m)
    insist(set(a)==set(b),f'support n={n}')
    for key in a:
        insist(a[key]==b[key],f'exact distribution n={n} {key}')

# Asymptotic deterministic variance compensators converge to the claimed constants.
for xi in (0.5,1.0,2.0):
    n=1_000_000
    m=round(n**(2/3))
    internal=sum((xi*n/k)**2/(2*k*k) for k in range(m+1,n))
    root=(xi*n/m)**2/(2*m)
    insist(abs(internal-xi*xi/6)<0.003,'internal compensator')
    insist(abs(root-xi*xi/2)<0.003,'root birthday compensator')

# Independent direct simulations of a DAG's ancestor set, without enumerating nonancestors.
rng=random.Random(20261027)
def sample(n,m):
    frontier=[n]; seen=set(); edges=[]
    while frontier:
        k=frontier.pop()
        if k in seen:continue
        seen.add(k)
        if k>m:
            for j in range(2):
                p=rng.randrange(1,k)
                edges.append((k,p))
                frontier.append(p)
    visits=Counter(p for _,p in edges if p>m)
    D=sum(z-1 for z in visits.values())
    roots=[p for _,p in edges if p<=m]
    y=len(roots)
    E=y-len(set(roots))
    x=len(seen)
    insist(x==2*y-1+D-E,'simulated DAG conservation')
    return D,E,y

n=1_000_000;m=10_000;N=2500
Ds=Es=Ys=0
for i in range(N):
    d,e,y=sample(n,m);Ds+=d;Es+=e;Ys+=y
# Mixed intensities: xi~Gamma(2,1), E[xi^2]=6: E D=1, E E=3.
insist(abs(Ds/N-1)<0.24, 'internal limiting mean Monte Carlo')
insist(abs(Es/N-3)<0.48, 'root limiting mean Monte Carlo')
insist(abs(Ys/N-2*n/m)<12,'gamma frontier mean Monte Carlo')
print('PASS',checks,'exact, algebraic, and seeded simulation assertions')
print('Monte Carlo means D,E,Y',round(Ds/N,5),round(Es/N,5),round(Ys/N,5))
