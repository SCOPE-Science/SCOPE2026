"""Finite verification of an all-graph nonlinear edge-Lipschitz rigidity theorem.

Run: python verify_universal_pheat.py
Requires Python 3 and SciPy for trajectory diagnostics. None of the finite tests
substitutes for the mathematical argument in RESULT.md.
"""
from collections import deque
from fractions import Fraction
import itertools
import math


def all_edges(n):
    return [(i, j) for i in range(n) for j in range(i+1, n)]


def distances(n, edges, source):
    adj=[[] for _ in range(n)]
    for u,v in edges:
        adj[u].append(v);adj[v].append(u)
    d=[-1]*n;d[source]=0
    queue=deque([source])
    while queue:
        v=queue.popleft()
        for w in adj[v]:
            if d[w]<0:
                d[w]=d[v]+1;queue.append(w)
    assert all(z>=0 for z in d)
    return d


def induced_triple(n, edges):
    E={tuple(sorted(e)) for e in edges}
    for j,i,k in itertools.permutations(range(n),3):
        if tuple(sorted((j,i))) in E and tuple(sorted((i,k))) in E and tuple(sorted((j,k))) not in E:
            return j,i,k
    return None


def flow(x, edges, conductances, masses, p):
    F=[0.0]*len(x)
    for (i,k),c in zip(edges,conductances):
        d=x[k]-x[i]
        z=math.copysign(abs(d)**(p-1),d) if d else 0.0
        F[i]+=c*z/masses[i]
        F[k]-=c*z/masses[k]
    return F


def initial_rate(n, edges, p, eps, R):
    triple=induced_triple(n, edges)
    if triple is None:
        return None
    j,i,k=triple
    h=distances(n, edges, j)
    assert h[j]==0 and h[i]==1 and h[k]==2
    assert max(abs(h[u]-h[v]) for u,v in edges)==1
    if p>2:
        a=[0.0]*n; a[k]=R
    else:
        a=[float(5+v) for v in range(n)]
        a[i]=a[k]=0.0;a[j]=1.0
    v=[a[z]+eps*h[z] for z in range(n)]
    conductances=[1+0.13*(z%5) for z in range(len(edges))]
    masses=[1+0.17*(z%7) for z in range(n)]
    F0=flow(a,edges,conductances,masses,p)
    F1=flow(v,edges,conductances,masses,p)
    rate=((F1[i]-F0[i])-(F1[j]-F0[j]))/eps
    return rate,triple


def exact_p3_check():
    edges=[(0,1),(1,2)] # j=0,i=1,k=2
    h=[0,1,2]
    m=[Fraction(3,2),Fraction(4,3),Fraction(5,2)]
    c=[Fraction(7,5),Fraction(11,7)]
    def exact_flow(x):
        f=[Fraction(0) for _ in x]
        for (a,b),w in zip(edges,c):
            d=x[b]-x[a];z=d*abs(d)
            f[a]+=w*z/m[a];f[b]-=w*z/m[b]
        return f
    eps=Fraction(1,10**5);R=Fraction(100)
    a=[Fraction(0),Fraction(0),R]
    v=[a[z]+eps*h[z] for z in range(3)]
    q0=exact_flow(a);q1=exact_flow(v)
    growth=((q1[1]-q0[1])-(q1[0]-q0[0]))/eps
    assert growth>0
    print('EXACT_P3_GROWTH_OK rate=',float(growth))


def test_complete():
    import numpy as np
    from scipy.integrate import solve_ivp
    num=0
    for n in [2,3,5,7]:
        edges=all_edges(n)
        cs=[0.8+0.09*(z%7) for z in range(len(edges))]
        ms=[1+0.15*(z%5) for z in range(n)]
        for p in [1.35,2.0,3.2]:
            a=np.array([(z*z%7)*.29-.7 for z in range(n)])
            b=np.array([math.sin(z*1.9)*.57 for z in range(n)])
            d=a-b
            L0=float(max(d)-min(d))
            sol1=solve_ivp(lambda t,x:flow(x,edges,cs,ms,p),(0,.07),a,rtol=2e-10,atol=2e-12,dense_output=True)
            sol2=solve_ivp(lambda t,x:flow(x,edges,cs,ms,p),(0,.07),b,rtol=2e-10,atol=2e-12,dense_output=True)
            assert sol1.success and sol2.success
            for t in np.linspace(0,.07,11):
                z=sol1.sol(t)-sol2.sol(t)
                assert max(z)-min(z)<=L0+2e-8,(n,p,t,max(z)-min(z),L0)
                num+=1
    print('COMPLETE_GRAPH_NUMERICAL_NONEXPANSIVITY_OK samples=',num)


def test_noncomplete():
    fam=[]
    for n in range(3,8):
        fam.append((f'path{n}',n,[(i,i+1) for i in range(n-1)]))
    for n in range(4,9):
        fam.append((f'cycle{n}',n,[(i,(i+1)%n) for i in range(n)]))
    fam.append(('K23',5,[(i,j) for i in range(2) for j in range(2,5)]))
    fam.append(('K5_minus_edge',5,[e for e in all_edges(5) if e!=(0,1)]))
    fam.append(('wheel7',7,[(i,(i+1)%6) for i in range(6)]+[(i,6) for i in range(6)]))
    for label,n,edges in fam:
        for p in [1.35,1.5,1.85,2.4,3.0,4.1]:
            if p<2:
                ans=initial_rate(n,edges,p,1e-8,0)
            else:
                ans=initial_rate(n,edges,p,1e-4,1e4)
            assert ans is not None and ans[0]>0,(label,p,ans)
    print('NONCOMPLETE_INDUCED_PATH_WITNESS_OK cases=',len(fam)*6)
    edges=[(0,1),(1,2)]
    for p in [1.5,3.0]:
        for scale in [10,100,1000]:
            eps=scale**(-6) if p<2 else 1e-4
            rate=initial_rate(3,edges,p,eps,scale)[0]
            assert rate>0
    print('ARBITRARILY_LARGE_RATE_DIAGNOSTICS_OK exponents=1.5,3')


if __name__=='__main__':
    exact_p3_check()
    test_noncomplete()
    test_complete()
    print('ALL_GRAPH_PHEAT_LIPSCHITZ_CHECKS_OK')
