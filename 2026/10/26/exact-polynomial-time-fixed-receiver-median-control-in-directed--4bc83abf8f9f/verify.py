"""Exact-rational checks for fixed-receiver edge additions in a Friedkin-Johnsen system.
Run with Python 3.9+; standard library only. Checks are finite and supplement the proof.
"""
from fractions import Fraction as Q
from itertools import combinations
import random

def mat_inv(A):
    n=len(A)
    T=[[Q(A[i][j]) for j in range(n)]+[Q(int(i==j)) for j in range(n)] for i in range(n)]
    for j in range(n):
        pivot=next(i for i in range(j,n) if T[i][j])
        T[j],T[pivot]=T[pivot],T[j]
        v=T[j][j];T[j]=[x/v for x in T[j]]
        for i in range(n):
            if i!=j:
                mul=T[i][j]
                if mul: T[i]=[x-mul*y for x,y in zip(T[i],T[j])]
    return [row[n:] for row in T]

def mv(M,x):return [sum((a*b for a,b in zip(row,x)),Q(0)) for row in M]

def fj(adj, lam, innate):
    n=len(adj)
    W=[[Q(1,len(adj[i])) if j in adj[i] else Q(0) for j in range(n)] for i in range(n)]
    M=[[Q(int(i==j))-lam[i]*W[i][j] for j in range(n)] for i in range(n)]
    G=mat_inv(M)
    z=mv(G,[(1-lam[i])*innate[i] for i in range(n)])
    return G,z

def alpha_formula(i,S,adj,lam,G,z):
    k=len(S); d=len(adj[i]);b=sum((z[v] for v in adj[i]),Q(0))/d
    h=[G[j][i] for j in range(len(adj))]
    den=d+k*h[i]-lam[i]*sum((h[j] for j in S),Q(0))
    assert den>0
    num=lam[i]*sum((z[j]-b for j in S),Q(0))
    return num/den

def optimal_by_breakpoints(i,k,adj,lam,G,z):
    m=[j for j in range(len(adj)) if j!=i and j not in adj[i]]
    if k==0:return (),Q(0)
    h=[G[j][i] for j in range(len(adj))]
    vals={Q(0)}
    for a,b in combinations(m,2):
        if h[a]!=h[b]: vals.add((z[b]-z[a])/(h[a]-h[b]))
    vals=sorted(vals)
    test=[vals[0]-1,vals[-1]+1,*vals]
    test += [(a+b)/2 for a,b in zip(vals,vals[1:])]
    best=None
    for t in test:
        top=tuple(sorted(m,key=lambda j:(z[j]+t*h[j],-j),reverse=True)[:k])
        val=alpha_formula(i,top,adj,lam,G,z)
        if best is None or val>best[1]:best=(top,val)
    return best

def test_one(adj,lam,s):
    global cases, subsets, solvechecks
    G,z=fj(adj,lam,s);n=len(adj)
    for i in range(n):
        missing=[j for j in range(n) if j!=i and j not in adj[i]]
        for k in range(1,len(missing)+1):
            opt=optimal_by_breakpoints(i,k,adj,lam,G,z)
            complete=[]
            for S in combinations(missing,k):
                a=alpha_formula(i,S,adj,lam,G,z)
                newadj=[list(row) for row in adj];newadj[i]+=S
                _,newz=fj(newadj,lam,s)
                assert newz==[z[j]+a*G[j][i] for j in range(n)]
                assert all(G[j][i]>=0 for j in range(n))
                complete.append(a)
                subsets+=1;solvechecks+=1
            assert opt[1]==max(complete)
            cases+=1

cases=subsets=solvechecks=0
adj=[[1,2],[0],[1],[2]]
lam=[Q(9,10),Q(9,10),Q(9,10),Q(1,2)]
s=[Q(2,5),Q(2,5),Q(1),Q(3,5)]
G,z=fj(adj,lam,s)
assert z==[Q(1192,2305),Q(233,461),Q(1279,2305),Q(1331,2305)]
assert z[3]>z[2]
assert alpha_formula(1,(2,),adj,lam,G,z)==Q(27,1450)
assert alpha_formula(1,(3,),adj,lam,G,z)==Q(1251,82550)
assert Q(27,1450)>Q(1251,82550)
test_one(adj,lam,s)
randomizer=random.Random(10272026)
for n in range(3,8):
    for trial in range(18):
        adj=[]
        for i in range(n):
            others=[j for j in range(n) if j!=i]
            adj.append(sorted(randomizer.sample(others,randomizer.randint(1,n-1))))
        lam=[Q(randomizer.randint(1,9),10) for _ in range(n)]
        s=[Q(randomizer.randint(0,9),9) for _ in range(n)]
        test_one(adj,lam,s)
print('PASS: fixed-receiver budget classifications',cases,'exact subset replays',subsets,'independent matrix inversions',solvechecks)
print('PASS: four-node exposure-ranking reversal, exact rational')
