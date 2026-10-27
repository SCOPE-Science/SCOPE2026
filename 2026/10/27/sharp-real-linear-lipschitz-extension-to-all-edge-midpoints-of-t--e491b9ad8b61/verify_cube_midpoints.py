#!/usr/bin/env python3
"""Numerical cross-check of cubic midpoint-extension theorem.
Python standard library only. This is not a machine proof of the radical inequalities.
"""
from itertools import product, combinations
from math import sqrt, dist, comb, factorial

EPS = 1e-11

def cube(d):
    vertices = [tuple(t) for t in product((0, 1), repeat=d)]
    midpoints = []
    for axis in range(d):
        for other in product((0, 1), repeat=d - 1):
            coords = list(other)
            coords.insert(axis, 0.5)
            midpoints.append(tuple(coords))
    return vertices, midpoints

def measures(d, b):
    vertices, midpoints = cube(d)
    a = 0.5 - (d - 1)*b
    result = {}
    for z in vertices:
        result[z] = [float(v == z) for v in vertices]
    for z in midpoints:
        axis = z.index(0.5)
        vals = []
        for v in vertices:
            h = sum(v[j] != z[j] for j in range(d) if j != axis)
            vals.append(a if h == 0 else (b if h == 1 else 0.0))
        assert abs(sum(vals) - 1) < 1e-12
        assert min(vals) >= 0
        result[z] = vals
    return vertices, midpoints, result

class MinCost:
    def __init__(self, n):
        self.graph=[[] for _ in range(n)]
    def edge(self,u,v,cap,cost):
        forward=[v,cap,cost,len(self.graph[v])]
        backward=[u,0.0,-cost,len(self.graph[u])]
        self.graph[u].append(forward)
        self.graph[v].append(backward)
    def solve(self,src,sink,total):
        amount=0.0
        cost=0.0
        n=len(self.graph)
        for _ in range(250):
            if total-amount<=EPS:
                break
            distance=[float('inf')]*n
            prev=[None]*n
            distance[src]=0.0
            for _round in range(n):
                changed=False
                for u in range(n):
                    if distance[u]==float('inf'): continue
                    for k,e in enumerate(self.graph[u]):
                        v,cap,c,_=e
                        cand=distance[u]+c
                        if cap>EPS and cand<distance[v]-EPS:
                            distance[v]=cand
                            prev[v]=(u,k)
                            changed=True
                if not changed:break
            assert prev[sink] is not None, 'transport flow incomplete'
            push=total-amount
            v=sink
            while v!=src:
                u,k=prev[v]
                push=min(push,self.graph[u][k][1])
                v=u
            assert push>EPS
            v=sink
            while v!=src:
                u,k=prev[v]
                edge=self.graph[u][k]
                edge[1]-=push
                self.graph[v][edge[3]][1]+=push
                cost+=push*edge[2]
                v=u
            amount+=push
        assert abs(amount-total)<1e-9
        return cost

def w1(vertices,mu,nu):
    n=len(vertices)
    solver=MinCost(2*n+2)
    start,end=2*n,2*n+1
    for i in range(n):
        solver.edge(start,i,mu[i],0.0)
        solver.edge(i+n,end,nu[i],0.0)
        for j in range(n):
            solver.edge(i,j+n,2.0,dist(vertices[i],vertices[j]))
    return solver.solve(start,end,sum(mu))

def test(d):
    if d==2:
        b=((1+sqrt(2))/sqrt(5)-1)/(2*sqrt(2)*(1+1/sqrt(5)))
        t=1+2*sqrt(2)*b
        baseline=(1+sqrt(2))/sqrt(5)
    elif d==3:
        b=(1+sqrt(2)-sqrt(5))/(4*sqrt(10)+2*(1+sqrt(2)-sqrt(3)))
        t=1+4*sqrt(2)*b
        baseline=(1+sqrt(3))/sqrt(6)
    else:raise ValueError
    vertices,mids,mu=measures(d,b)
    S=vertices+mids
    maxnorm=0.0
    maximizing=[]
    for x,y in combinations(S,2):
        r=w1(vertices,mu[x],mu[y])/dist(x,y)
        if r>maxnorm+1e-9:
            maxnorm=r
            maximizing=[(x,y)]
        elif abs(r-maxnorm)<1e-9:
            maximizing.append((x,y))
    assert abs(maxnorm-t)<1e-9, (maxnorm,t)
    assert baseline>t+0.005
    print(f'dimension={d}, vertices={len(vertices)}, midpoints={len(mids)}, pairs={len(S)*(len(S)-1)//2}')
    print(f'  b={b:.15f}, target_norm={t:.15f}, measured_norm={maxnorm:.15f}, midpoint_interpolation_norm={baseline:.15f}, maximizing_pairs={len(maximizing)}')
    if d==3:
        x=(0,0,0)
        f2={ (0,0,0):0,(1,0,0):1,(0,1,0):1,(0,0,1):1,
             (1,1,0):sqrt(2),(1,0,1):sqrt(2),
             (0,1,1):0,(1,1,1):sqrt(2)-1 }
        assert all(abs(f2[u]-f2[v]) <= dist(u,v)+1e-12 for u,v in combinations(vertices,2))
        near=(0.5,0,0)
        assert abs(sum(p*f2[u] for p,u in zip(mu[near],vertices))-t*.5) < 1e-10
        print('  second near-midpoint dual witness: 1-Lipschitz and sharp')

if __name__=='__main__':
    test(2)
    test(3)
    print('PASS: all 218 source-target pairs and the dual-witness checks')
