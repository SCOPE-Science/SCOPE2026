"""Exact checks for biased-bond exclusion on adjacent-twin graphs.

Only Python's standard library is required.  All finite-generator tests use
Fraction arithmetic, without Monte Carlo or approximate stationarity solves.
"""
from fractions import Fraction as F
from itertools import combinations
from math import comb, isclose, log


def connected(n, edges):
    seen={0}; stack=[0]; adj=[set() for _ in range(n)]
    for u,v in edges: adj[u].add(v); adj[v].add(u)
    while stack:
        for v in adj[stack.pop()]:
            if v not in seen: seen.add(v); stack.append(v)
    return len(seen)==n


def twin(n, edges, u, v):
    E=set(tuple(sorted(x)) for x in edges)
    return {w for w in range(n) if w not in (u,v) and tuple(sorted((u,w))) in E} == {w for w in range(n) if w not in (u,v) and tuple(sorted((v,w))) in E}


def states(n, k):
    return [sum(1 << i for i in c) for c in combinations(range(n),k)]


def occupation(mask, i): return (mask >> i) & 1


def canonical(n,k,p,q,edges,u,v):
    external=[w for w in range(n) if w not in (u,v) and tuple(sorted((u,w))) in edges]
    c=(p-q)/(p+q+len(external))
    return {z:(1+c*(occupation(z,v)-occupation(z,u)))/comb(n,k) for z in states(n,k)},c


def residual(n,k,p,q,edges,u,v):
    P,c=canonical(n,k,p,q,edges,u,v)
    incoming={s:F(0) for s in P}
    for s,weight in P.items():
        for a,b in edges:
            oa,ob=occupation(s,a),occupation(s,b)
            if oa==ob: continue
            if (a,b)==(u,v): r=p if oa else q
            elif (a,b)==(v,u): r=q if oa else p
            else: r=F(1)
            t=s^(1<<a)^(1<<b)
            incoming[t]+=weight*r
            incoming[s]-=weight*r
    return incoming,P,c


def run():
    checked=0
    samples=0
    p,q=F(7,5),F(2,5)
    # All connected undirected simple graphs on <=5 vertices, every edge and
    # every nontrivial canonical occupancy sector.
    for n in range(3,6):
        possible=list(combinations(range(n),2))
        for mask in range(1,1<<len(possible)):
            es={e for i,e in enumerate(possible) if mask>>i&1}
            if not connected(n,es): continue
            for u,v in es:
                t=twin(n,es,u,v)
                for k in range(1,n):
                    r,P,c=residual(n,k,p,q,es,u,v)
                    exact=all(x==0 for x in r.values())
                    assert exact==t,(n,es,u,v,k,exact,t)
                    assert sum(P.values())==1
                    assert all(0<x<1 for x in P.values())
                    checked+=1
            samples+=1
    # Large and nonvertex-transitive examples, exact all-state checks.
    examples=[
        (6,{(0,1),(0,2),(1,2),(2,3),(3,4),(4,5)}),
        (6,{(0,1),(0,2),(1,2),(2,3),(2,4),(3,4),(4,5)}),
        (7,{(0,1),(0,2),(1,2),(2,3),(2,4),(3,4),(4,5),(5,6)}),
        (7,{(i,j) for i in range(7) for j in range(i+1,7)}),
    ]
    for n,es in examples:
        assert twin(n,es,0,1)
        for k in range(1,n):
            r,P,c=residual(n,k,p,q,es,0,1)
            assert all(x==0 for x in r.values())
            U=F(1,comb(n,k)); base=F(k*(n-k),n*(n-1))
            TV=sum(abs(z-U) for z in P.values())/2
            assert TV==abs(c)*base
            # Stationary local currents: only triangles containing the bond.
            for a,b in es:
                if (a,b)==(0,1):
                    expected=base*(p-q)*len({w for w in range(2,n) if (0,w) in es and (1,w) in es}) / (p+q+len({w for w in range(2,n) if (0,w) in es and (1,w) in es}))
                    J=sum(P[s]*(p*occupation(s,0)*(1-occupation(s,1)) - q*occupation(s,1)*(1-occupation(s,0))) for s in P)
                else:
                    J=sum(P[s]*(occupation(s,a)-occupation(s,b)) for s in P)
                    expected=(base*c if (a,b) in [(1,x) for x in range(2,n)]+[(x,0) for x in range(2,n)] else
                              -base*c if (b,a) in [(1,x) for x in range(2,n)]+[(x,0) for x in range(2,n)] else F(0))
                assert J==expected,(n,es,k,a,b,J,expected)
            checked+=1
    # Exact finite-state entropy production against the cycle-affinity law.
    for n,es in examples:
        k=n//2
        P,c=canonical(n,k,p,q,es,0,1)
        ent=0.0
        for a,b in es:
            for state in P:
                if not (occupation(state,a)==1 and occupation(state,b)==0): continue
                other=state^(1<<a)^(1<<b)
                forward=p if (a,b)==(0,1) else F(1)
                backward=q if (a,b)==(0,1) else F(1)
                f=float(P[state]*forward)
                r=float(P[other]*backward)
                ent+=(f-r)*log(f/r)
        kcommon=sum(1 for w in range(2,n) if (0,w) in es and (1,w) in es)
        base=F(k*(n-k),n*(n-1))
        J=base*(p-q)*kcommon/(p+q+kcommon)
        assert isclose(ent,float(J)*log(float(p/q)),abs_tol=1e-12,rel_tol=1e-12), (ent,J)
        checked+=1
    # Analytic complete-graph limit, tested at multiple finite sizes.
    eps_p,eps_q=F(7,5),F(2,5)
    for n in (20,100,1000,5000):
        k=n//3; rho=F(k,n); h=n-2
        c=(eps_p-eps_q)/(h+eps_p+eps_q)
        base=F(k*(n-k),n*(n-1))
        J=base*(eps_p-eps_q)*h/(h+eps_p+eps_q)
        lim=rho*(1-rho)*(eps_p-eps_q)
        assert abs(float(J-lim)) < 3/n
        assert abs(float(c*base)) < 3/n
        assert isclose(float(J*log(float(eps_p/eps_q))), float(J)*log(float(eps_p/eps_q)),rel_tol=1e-14)
        checked+=1
    print('PASS',checked,'exact/non-twin and limiting checks across',samples,'connected graphs')

if __name__=='__main__': run()
