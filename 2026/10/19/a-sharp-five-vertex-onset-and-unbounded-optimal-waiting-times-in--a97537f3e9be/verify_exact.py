#!/usr/bin/env python3
"""Exact rational checks for finite-stage neutral fixation on growing graphs.
Scientific reproduction uses only Python standard-library fractions and itertools.
"""
from fractions import Fraction as Q
from itertools import product

S1=[(0,1)]
S2=[(0,1),(1,2)]
FIVE=[(0,1),(1,2),(2,3),(0,3),(0,4)]
checks=0

def eq(a,b):
    global checks
    assert a==b,(a,b)
    checks+=1

def deg(n,edges):
    return [sum((i==v or j==v) for i,j in edges) for v in range(n)]

def step_expectation(vec,edges):
    n=len(vec);d=deg(n,edges)
    return [Q(n-1,n)*vec[i]+sum((vec[j]/d[i] for a,b in edges for j in ([b] if a==i else ([a] if b==i else []))),Q(0))/n for i in range(n)]

def expected_closed(g,n,edges):
    e=Q(1,2);v=[e,e,Q(0)]
    for _ in range(g): v=step_expectation(v,S2)
    dd=deg(n,edges)
    return sum((dd[i]*v[i] for i in range(3)),Q(0))/sum(dd)

def formula(g,n,edges):
    dd=deg(n,edges);a,b,c=dd[:3];volume=sum(dd)
    return Q(3*(a+b+c),8*volume)+Q(a-c,4*volume)*Q(2,3)**g+Q(b-a-c,8*volume)*Q(1,3)**g

# Exact eigen-expansion on the three-vertex path.
for g in range(0,41):
    v=[Q(1,2),Q(1,2),Q(0)]
    for _ in range(g):v=step_expectation(v,S2)
    eig=[Q(3,8)+Q(1,4)*Q(2,3)**g-Q(1,8)*Q(1,3)**g,
         Q(3,8)+Q(1,8)*Q(1,3)**g,
         Q(3,8)-Q(1,4)*Q(2,3)**g-Q(1,8)*Q(1,3)**g]
    for i in range(3):eq(v[i],eig[i])

# Check every induced, connected 4-node extension of a three-node path.
for e0,e1,e2 in product((0,1),repeat=3):
    if not e0+e1+e2: continue
    edges=S2+[(i,3) for i,e in enumerate((e0,e1,e2)) if e]
    d=deg(4,edges)
    # The closed-form increment cannot change sign for g >= 0.
    u=d[0]-d[1]+d[2];v=d[0]-d[2]
    signs=[]
    for g in range(0,25):
        diff=formula(g+1,4,edges)-formula(g,4,edges)
        eq(diff,Q(u-v*2**g,12*sum(d)*3**g))
        signs.append((diff>0)-(diff<0))
    nonzero=[x for x in signs if x]
    eq(len(set(nonzero))<=1,True)

# Every induced connected 4-node extension of K3 has a single decaying mode.
for e0,e1,e2 in product((0,1),repeat=3):
    if not e0+e1+e2:continue
    edges=[(0,1),(1,2),(0,2)]+[(i,3) for i,e in enumerate((e0,e1,e2)) if e]
    x=[Q(1,2),Q(1,2),Q(0)]
    targets=[]
    for g in range(25):
        dd=deg(4,edges)
        targets.append(sum((dd[i]*x[i] for i in range(3)),Q(0))/sum(dd))
        x=step_expectation(x,[(0,1),(1,2),(0,2)])
    diffs=[targets[g+1]-targets[g] for g in range(24)]
    for g in range(23):eq(diffs[g+1],diffs[g]/2)

# Five-node exact formula and unique strict maximizing dwell of 2 generations.
for g in range(41):
    val=expected_closed(g,5,FIVE)
    eq(val,formula(g,5,FIVE))
    eq(val,Q(21,80)+Q(1,40)*Q(2,3)**g-Q(3,80)*Q(1,3)**g)
    incr=formula(g+1,5,FIVE)-val
    eq(incr,Q(3-2**g,120*3**g))
    eq((incr>0) if g in (0,1) else (incr<0),True)
eq(formula(1,5,FIVE),Q(4,15))
eq(formula(2,5,FIVE),Q(97,360))
eq(formula(3,5,FIVE),Q(29,108))

# Full voter-chain distribution, independent of the one-point expectation recursion.
def transitions(s,n,edges):
    d=deg(n,edges)
    ans={}
    for i in range(n):
        for a,b in edges:
            if i not in (a,b):continue
            j=b if a==i else a
            out=(s & ~(1<<i))|(((s>>j)&1)<<i)
            ans[out]=ans.get(out,Q(0))+Q(1,n*d[i])
    eq(sum(ans.values()),Q(1))
    return ans

def evolve(dist,n,edges,steps):
    for _ in range(steps):
        nd={}
        for s,p in dist.items():
            for r,z in transitions(s,n,edges).items():nd[r]=nd.get(r,Q(0))+p*z
        dist=nd
    return dist

# Solve 30x30 absorbing chain via exact rational Gaussian elimination.
n=5;mask=(1<<n)-1;states=list(range(1,mask));dim=len(states)
trans={s:transitions(s,n,FIVE) for s in states}
A=[]
for s in states:
    row=[(Q(int(s==t))-trans[s].get(t,Q(0))) for t in states]
    row.append(trans[s].get(mask,Q(0)));A.append(row)
for k in range(dim):
    p=next(i for i in range(k,dim) if A[i][k]);A[k],A[p]=A[p],A[k]
    scale=A[k][k];A[k]=[z/scale for z in A[k]]
    for i in range(dim):
        if i==k: continue
        fac=A[i][k]
        if fac:A[i]=[a-fac*b for a,b in zip(A[i],A[k])]
values={0:Q(0),mask:Q(1)}
values.update((s,A[i][-1]) for i,s in enumerate(states))
d=deg(5,FIVE)
for s in range(mask+1):eq(values[s],sum((d[i]*((s>>i)&1) for i in range(5)),Q(0))/sum(d))
for g in range(11):
    dist=evolve({1:Q(1,2),2:Q(1,2)},2,S1,g)
    dist=evolve(dist,3,S2,g) # newcomer 2 is a defector (bit 2 unset)
    val=sum((p*values[s] for s,p in dist.items()),Q(0)) # newcomers 3,4 initially defector
    eq(val,formula(g,5,FIVE))

# Arbitrarily late optimum on trees: t leaves at vertex 2, t+1 leaves at vertex 0.
for t in range(1,101):
    edges=S2[:]
    for j in range(t+1):edges.append((0,3+j))
    for j in range(t):edges.append((2,3+t+1+j))
    n=2*t+4
    dd=deg(n,edges)
    eq(dd[:3],[t+2,2,t+1])
    import math
    q=(2*t+1).bit_length() # 2**(q-1) <=2t+1 <2**q ; 2t+1 odd nonpower for t>=1
    gopt=q
    eq(formula(gopt,n,edges)>formula(gopt-1,n,edges),True)
    eq(formula(gopt,n,edges)>formula(gopt+1,n,edges),True)
    eq(len(edges),n-1)
print('PASS', checks, 'exact assertions')
