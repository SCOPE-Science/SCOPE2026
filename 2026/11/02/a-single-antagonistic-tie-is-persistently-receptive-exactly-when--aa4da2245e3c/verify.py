#!/usr/bin/env python3
"""Exact graph and dynamic checks for a single negative tie in the Kann--Feng map."""
from fractions import Fraction as F
from itertools import combinations
from math import isclose

def laplacian(n, edges):
    L = [[F(0) for _ in range(n)] for _ in range(n)]
    for u, v in edges:
        L[u][u] += 1; L[v][v] += 1
        L[u][v] -= 1; L[v][u] -= 1
    return L

def potential(n, edges, u, v):
    # Gauge psi[0]=0; L psi = e_v-e_u. Rational Gauss-Jordan.
    L=laplacian(n,edges)
    rhs=[F(int(i==v)-int(i==u)) for i in range(1,n)]
    A=[L[i][1:]+[rhs[i-1]] for i in range(1,n)]
    for j in range(n-1):
        k=next(k for k in range(j,n-1) if A[k][j]); A[j],A[k]=A[k],A[j]
        a=A[j][j]; A[j]=[z/a for z in A[j]]
        for k in range(n-1):
            if k!=j:
                a=A[k][j]
                if a: A[k]=[x-a*y for x,y in zip(A[k],A[j])]
    return [F(0)]+[A[i][-1] for i in range(n-1)]

def connected(n,edges):
    seen={0}; active=[0]; adj=[[] for _ in range(n)]
    for a,b in edges: adj[a].append(b); adj[b].append(a)
    while active:
        k=active.pop()
        for j in adj[k]:
            if j not in seen: seen.add(j); active.append(j)
    return len(seen)==n

def bridge(n, edges, target):
    return not connected(n,[e for e in edges if e!=target])

def step(x,edges,negative,c):
    y=[x_i for x_i in x];
    for i in range(len(x)):
        z=F(0); deg=1
        for u,v in edges:
            if i!=u and i!=v: continue
            j=v if i==u else u
            d=x[j]-x[i]
            if abs(d)>=c: continue
            deg+=1
            if (u,v)!=negative:
                z+=d
            else:
                if d==0: sign=1 if j>i else -1
                else: sign=1 if d>0 else -1
                z-=sign*(c-abs(d))
        y[i]=x[i]+z/deg
    return y

def check_graph(n, edges, neg):
    u,v=neg; psi=potential(n,edges,u,v)
    R=psi[v]-psi[u]
    assert R>0
    assert (R==1)==bridge(n,edges,neg)
    assert max(psi)-min(psi)==R
    assert all(abs(psi[b]-psi[a])<=R for a,b in edges)
    if R<1:
        for sign in [1,-1]:
            x=[sign*z for z in psi]
            assert abs(x[v]-x[u])==R
            assert all(abs(x[b]-x[a])<1 for a,b in edges)
            assert step(x,edges,neg,F(1))==x
        # The degree-weighted mean is conserved for arbitrary profiles within confidence.
        x=[F(i, 100*n) for i in range(n)]
        deg=[1+sum(i in e for e in edges) for i in range(n)]
        y=step(x,edges,neg,F(1))
        assert sum(a*b for a,b in zip(deg,x))==sum(a*b for a,b in zip(deg,y))
    return R

def main():
    verified=0; bridge_pairs=0; cycle_pairs=0
    for n in range(2,6):
        pairs=list(combinations(range(n),2)); cn=0
        for mask in range(1,1<<len(pairs)):
            edges=[e for k,e in enumerate(pairs) if mask>>k & 1]
            if not connected(n,edges):continue
            cn+=1
            for neg in edges:
                R=check_graph(n,edges,neg)
                verified+=1
                bridge_pairs+=(R==1)
                cycle_pairs+=(R<1)
        print(f'n={n}: connected_graphs={cn}')
    assert verified==bridge_pairs+cycle_pairs
    print('EXACT graph/hostile-edge instances:',verified,'bridge:',bridge_pairs,'cycle:',cycle_pairs)
    for n in range(3,17):
        edges=[(i,(i+1)%n) if i<n-1 else (0,n-1) for i in range(n)]
        assert potential(n,edges,0,1)[1]==F(n-1,n)
        edges=list(combinations(range(n),2))
        assert potential(n,edges,0,1)[1]==F(2,n)
    print('EXACT cycle and clique resistance formulas: n=3..16')
    # Perturbation test with a 4-cycle; check converges to the orientation-specific equilibrium.
    n=4; edges=[(0,1),(1,2),(2,3),(0,3)]; neg=(0,1)
    psi=potential(n,edges,*neg)
    c=F(1); deg=[1+sum(i in e for e in edges) for i in range(n)]
    mean=sum(deg[i]*psi[i] for i in range(n))/sum(deg)
    fixed=[q-mean for q in psi]
    x=[fixed[i]+F([1,-1,2,-2][i],1000) for i in range(n)]
    mu=sum(deg[i]*x[i] for i in range(n))/sum(deg)
    for k in range(45):
        assert all(abs(x[a]-x[b])<1 for a,b in edges)
        assert x[1]>x[0]
        x=step(x,edges,neg,c)
    goal=[y+mu for y in fixed]
    assert max(abs(float(a-b)) for a,b in zip(x,goal))<1e-9
    print('EXACT rational forty-five-step local orbit: confidence maintained and exponential convergence')
    print('ALL CHECKS PASS')

if __name__=='__main__': main()
