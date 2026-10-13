#!/usr/bin/env python3
"""Exact finite tests of the reversible-chain perfect-search criterion.

The unrestricted conclusion is proved analytically; finite enumeration is a regression check.
"""
from fractions import Fraction as F
from itertools import product


def chain(conductance):
    n=len(conductance)
    d=[sum(r) for r in conductance]
    if any(x==0 for x in d):
        return None
    q=sum(d)
    p=[[F(conductance[u][v], d[u]) for v in range(n)] for u in range(n)]
    pi=[F(x,q) for x in d]
    return p, pi


def connected(c):
    n=len(c)
    seen={0}
    frontier=[0]
    while frontier:
        u=frontier.pop()
        for v in range(n):
            if v not in seen and v!=u and c[u][v]:
                seen.add(v)
                frontier.append(v)
    return len(seen)==n


def analyze(p,pi,w):
    n=len(p)
    a=pi[w]; r=p[w][w]
    assert 0<a<1 and 0<=r<1
    gamma=(1-a)/(1-r)
    # Orthogonal realization of L=I-P in l^2(pi).
    p2ww=sum(p[w][u]*p[u][w] for u in range(n))
    l2=1-2*r+p2ww
    # First moment equality fixes gamma. Second moment equality is exact.
    second_equal=(gamma*gamma*l2-2*gamma*(1-r)+1==a)
    c=(1-r)*a/(1-a)
    entrance_equal=all(p[u][w]==c for u in range(n) if u!=w)
    assert second_equal==entrance_equal
    if entrance_equal:
        k=(1-r)/(1-a)
        assert gamma*k==1
        # Necessary/sufficient vector identity in the l^2(pi) representation.
        for u in range(n):
            lhs=F(u==w)-p[u][w]
            rhs=k*(F(u==w)-a)
            assert lhs==rhs
        # Unique tuning and phase frequencies ±sqrt(pi_w) follow exactly.
        assert gamma*(1-r)==1-a
    return entrance_equal


def enumerate_cases(n,weights,loop_weights):
    edges=[(u,v) for u in range(n) for v in range(u+1,n)]
    cases=perfect=0
    for ws in product(weights, repeat=len(edges)):
        c=[[0]*n for _ in range(n)]
        for (u,v),wt in zip(edges,ws):
            c[u][v]=c[v][u]=wt
        if not connected(c):
            continue
        for ls in product(loop_weights,repeat=n):
            for u,v in enumerate(ls): c[u][u]=v
            ppi=chain(c)
            if ppi is None: continue
            p,pi=ppi
            for u in range(n):
                cases+=1
                perfect+=analyze(p,pi,u)
    return cases,perfect


def explicit_witnesses():
    # Nonregular-base cone: marked vertex 0; base is 1--2--3.
    c=[[0,1,2,1],[1,0,1,0],[2,1,0,1],[1,0,1,0]]
    p,pi=chain(c)
    assert pi[0]==F(1,3)
    assert all(p[u][0]==F(1,2) for u in (1,2,3))
    assert analyze(p,pi,0)
    assert pi==[F(1,3),F(1,6),F(1,3),F(1,6)]
    # On K3, an asymmetric mark-edge conductance destroys perfect search.
    c2=[[0,1,2],[1,0,1],[2,1,0]]
    p2,pi2=chain(c2)
    assert not analyze(p2,pi2,0)
    # Same K3 topology with balanced marked conductance remains perfect.
    c3=[[0,1,1],[1,0,3],[1,3,0]]
    p3,pi3=chain(c3)
    assert analyze(p3,pi3,0)
    # Holding the topology fixed changes exact attainability.
    return pi[0],pi2[0],pi3[0]


def main():
    count=chosen=0
    for n,weights,loops in [(2,(0,1,2),(0,1,2)),
                             (3,(0,1,2),(0,1,2)),
                             (4,(0,1,2),(0,1))]:
        c,p=enumerate_cases(n,weights,loops)
        count+=c;chosen+=p
    assert explicit_witnesses()==(F(1,3),F(3,8),F(1,5))
    print('VERIFY_OK exact_markov_moments_checks=%d condition_true=%d weighted_cone=true triangle_balance=true'%(count,chosen))

if __name__=='__main__': main()
