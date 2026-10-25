"""Reproducible finite and stochastic diagnostics for a root-polytope width law.

Python standard library only: run `python checker_stdlib.py`.
Simulation is not an infinite-dimensional mathematical proof.
"""
import itertools
import math
import random
import statistics

r = random.Random(20261020)

def exp1():
    return -math.log(1-r.random())

def quantile(a, q):
    s=sorted(a)
    j=(len(s)-1)*q
    lo=int(j)
    hi=min(lo+1,len(s)-1)
    return s[lo]*(hi-j)+s[hi]*(j-lo) if hi>lo else s[lo]

def finite():
    n=5
    edges=list(itertools.combinations(range(n),2))
    perms=list(itertools.permutations(range(n)))
    v=[-5.,2.,0.,9.,3.]
    g=[x-sum(v)/n for x in v]
    for mask in range(1<<len(edges)):
        chosen=[e for j,e in enumerate(edges) if mask>>j&1]
        direct=max([abs(g[i]-g[j]) for i,j in chosen],default=0.)
        root=max([d for i,j in chosen for d in (g[i]-g[j],g[j]-g[i])],default=0.)
        assert direct==root
        edge_set={tuple(sorted(e)) for e in chosen}
        hits=sum(tuple(sorted((perm[0],perm[-1]))) in edge_set for perm in perms)
        assert hits*len(edges)==len(perms)*len(chosen)
    print('EXACT_COMBINATORIAL_PASS',1<<len(edges),len(perms))

def finite_graph_range(n,p):
    g=sorted((r.gauss(0,1) for _ in range(n)),reverse=True)
    best=0.
    for i in range(n-1):
        if g[i]-g[-1]<=best:break
        for j in range(n-1,i,-1):
            d=g[i]-g[j]
            if d<=best:break
            if r.random()<p:best=d
    return best

def mixture(p,k):
    arrival=0.
    coeff=p
    A=0.
    for j in range(k):
        arrival+=exp1()
        A+=coeff/arrival
        coeff*=1-p
    return -math.log(exp1())+math.log(A)

def marked(p,k):
    u=[];v=[];s=0.
    for _ in range(k):
        s+=exp1();u.append(-math.log(s))
    s=0.
    for _ in range(k):
        s+=exp1();v.append(-math.log(s))
    best=-1.e100
    for x in u:
        for y in v:
            if r.random()<p and x+y>best:best=x+y
    return best

def run():
    finite()
    p=.4;n=3000;N=1400
    b=statistics.NormalDist().inv_cdf(1-1/n)
    finit=[b*(finite_graph_range(n,p)-2*b) for _ in range(N)]
    mix=[mixture(p,110) for _ in range(3*N)]
    mark=[marked(p,42) for _ in range(3*N)]
    qs=(.25,.5,.75)
    f=[quantile(finit,q) for q in qs]
    a=[quantile(mix,q) for q in qs]
    bq=[quantile(mark,q) for q in qs]
    print('FINITE_GRAPH_QUANTILES',*[round(v,5) for v in f])
    print('POISSON_MIXTURE_QUANTILES',*[round(v,5) for v in a])
    print('INDEPENDENT_MARKED_PROCESS_QUANTILES',*[round(v,5) for v in bq])
    assert max(abs(a0-b0) for a0,b0 in zip(a,bq))<.27
    assert max(abs(a0-b0) for a0,b0 in zip(a,f))<.85
    mix1=[mixture(1.,2) for _ in range(3*N)]
    sumg=[-math.log(exp1())-math.log(exp1()) for _ in range(3*N)]
    assert max(abs(quantile(mix1,q)-quantile(sumg,q)) for q in qs)<.25
    print('FINITE_LIMIT_DIAGNOSTICS_PASS',n,N)
if __name__=='__main__':run()
