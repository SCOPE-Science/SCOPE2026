#!/usr/bin/env python3
"""Independent finite tests for normalized squaring of weighted permutation evolution algebras."""
from itertools import permutations
from math import gcd, factorial, isclose


def cycles(perm):
    n=len(perm); seen=set(); ans=[]
    for i in range(n):
        if i not in seen:
            part=[]; j=i
            while j not in seen:
                seen.add(j);part.append(j);j=perm[j]
            assert j==i
            ans.append(part)
    return ans


def gamma(perm,weights):
    n=len(perm);g=[0.0]*n
    for cyc in cycles(perm):
        l=len(cyc)
        start=cyc[0]
        value=1.0
        for j,i in enumerate(cyc):
            value*=weights[i]**(2**(l-1-j))
        g[start]=value**(1.0/(2**l-1))
        for i in cyc[:-1]:g[perm[i]]=g[i]**2/weights[i]
    for i in range(n):
        assert isclose(g[perm[i]]*weights[i],g[i]*g[i],rel_tol=1e-9)
    return g


def norm(v):
    s=sum(v)
    return [z/s for z in v]


def T(x,p,w):
    out=[0.0]*len(x)
    for i,j in enumerate(p):out[j]=w[i]*x[i]*x[i]
    return norm(out)


def canonical(x,p):
    return T(x,p,[1.0]*len(x))


def H(x,g):return norm([a*b for a,b in zip(x,g)])


def iteration_closed(y,p,t):
    out=[0.0]*len(y)
    power=2**t
    for i,v in enumerate(y):
        j=i
        for _ in range(t):j=p[j]
        out[j]=v**power
    return norm(out)


def orbit_support(mask,p):
    a=mask;visited=[]
    while a not in visited:
        visited.append(a)
        b=0
        for i,j in enumerate(p):
            if a>>i&1:b|=1<<j
        a=b
    assert a==mask
    return visited


def lcm(a,b):return a*b//gcd(a,b)


def test_perm(p):
    n=len(p);L=1
    for cyc in cycles(p):L=lcm(L,len(cyc))
    arr=set(range(1,2**n));period_hist={}
    while arr:
        mask=next(iter(arr));orbit=orbit_support(mask,p)
        assert all(o in arr for o in orbit)
        arr.difference_update(orbit)
        period_hist[len(orbit)]=period_hist.get(len(orbit),0)+1
    for r in range(1,L+1):
        if L%r:continue
        P=list(range(n))
        for _ in range(r):P=[p[i] for i in P]
        c=len(cycles(P))
        fixed_from_orbits=sum(k*v for k,v in period_hist.items() if r%k==0)
        assert fixed_from_orbits==2**c-1,(p,r,c,period_hist)
    W=[0.9+((i*7+n)%7)/5 for i in range(n)]
    g=gamma(p,W)
    tests=[[i+2.5 for i in range(n)],[1.0]*(n-1)+[3.0]]
    for x0 in tests:
        x=norm(x0)
        h=H(x,g)
        assert all(isclose(a,b,abs_tol=3e-11) for a,b in zip(H(T(x,p,W),g),canonical(h,p)))
        for t in range(1,6):
            h=canonical(h,p)
            exact=iteration_closed(H(x,g),p,t)
            assert all(isclose(a,b,abs_tol=1e-9) for a,b in zip(h,exact)),(p,t,h,exact)
    return period_hist


if __name__=='__main__':
    checked=0
    for n in range(1,7):
        for p in permutations(range(n)):
            test_perm(p)
            checked+=1
    # Nontrivial tied maximum: the limit is the rotating uniform indicator, not one vertex.
    p=(1,2,3,0)
    w=[1.3,2.1,0.7,1.6]
    g=gamma(p,w)
    y=[0.4,0.4,0.1,0.1]
    x=norm([y[i]/g[i] for i in range(4)])
    for t in range(7):x=T(x,p,w)
    h=H(x,g)
    target=[0.0]*4
    for k in (0,1):target[(k+7)%4]=0.5
    assert max(abs(a-b) for a,b in zip(h,target))<1e-10,(h,target)
    print('VERIFY_OK', 'permutations',checked,'exact_period_counts_all_subsets_checked_n_le_6','weighted_conjugacy_and_iterates_checked')
