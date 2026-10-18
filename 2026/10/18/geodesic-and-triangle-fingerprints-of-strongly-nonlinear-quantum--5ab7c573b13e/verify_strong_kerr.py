#!/usr/bin/env python3
"""Reproduce finite-graph strong-Kerr scaling sanity checks (not an infinite proof)."""
from __future__ import annotations
import cmath
from collections import deque
from math import factorial, pi


def graph(n, edges):
    out=[set() for _ in range(n)]
    for a,b in edges:
        assert a!=b and 0<=a<n and 0<=b<n
        out[a].add(b);out[b].add(a)
    return tuple(tuple(sorted(s)) for s in out)


def graph_geometry(G, source=0):
    dist=[-1]*len(G)
    paths=[0]*len(G)
    dist[source]=0;paths[source]=1
    q=deque([source])
    while q:
        x=q.popleft()
        for y in G[x]:
            if dist[y]<0:
                dist[y]=dist[x]+1;q.append(y)
            if dist[y]==dist[x]+1:
                paths[y]+=paths[x]
    return dist, paths


def exponential_remainder(level, time):
    return cmath.exp(1j*time)-sum((1j*time)**k/factorial(k) for k in range(level))


def evolve_scaled(G, g, s, steps=1800):
    n=len(G);h=s/steps
    state=[0j]*n;state[0]=1+0j
    def vector_field(z):
        return [1j*(sum(z[j] for j in G[v])/g + abs(z[v])**2*z[v]) for v in range(n)]
    def add(z,k,a):return [z[v]+a*k[v] for v in range(n)]
    for _ in range(steps):
        k1=vector_field(state)
        k2=vector_field(add(state,k1,h/2))
        k3=vector_field(add(state,k2,h/2))
        k4=vector_field(add(state,k3,h))
        state=[state[v]+h*(k1[v]+2*k2[v]+2*k3[v]+k4[v])/6 for v in range(n)]
    return state


def energy(G, z,g):
    interaction=-sum((z[u].conjugate()*z[v]).real for u in range(len(G)) for v in G[u])
    return interaction -g*sum(abs(x)**4 for x in z)/2


def main():
    cases={
     'path5':graph(5,[(0,1),(1,2),(2,3),(3,4)]),
     'diamond5':graph(5,[(0,1),(0,2),(1,3),(2,3),(3,4)]),
     'star5':graph(5,[(0,1),(0,2),(0,3),(0,4)]),
     'triangle-tail5':graph(5,[(0,1),(1,2),(2,0),(2,3),(3,4)]),
     'square':graph(4,[(0,1),(1,2),(2,3),(3,0)]),
    }
    checks=0
    for label,G in cases.items():
        dist, paths=graph_geometry(G)
        for g in (100,300,900):
            z=evolve_scaled(G,g,pi)
            norm=sum(abs(v)**2 for v in z)
            assert abs(norm-1)<2e-9,(label,g,'mass',norm)
            checks+=1
            assert abs(energy(G,z,g)+g/2)<2e-8,(label,g,'energy')
            checks+=1
            escape=sum(abs(v)**2 for v in z[1:])
            degree=len(G[0])
            triangles=sum(1 for u in G[0] for v in G[0] if u<v and v in G[u])
            # The convergence rate may be O(1/g) when triangles exist.
            assert abs(g*g*escape/(4*degree)-1)<3.0/g,(label,g,'escape')
            checks+=1
            # The next-order leakage coefficient detects triangles at the source.
            measured=g*(g*g*escape-4*degree)
            assert abs(measured-16*triangles)<75.0/g,(label,g,'triangles',measured,triangles)
            checks+=1
            for v in range(1,len(G)):
                h=dist[v]
                if h<0:continue
                expected=paths[v]*exponential_remainder(h,pi)
                observed=g**h*z[v]
                assert abs(observed-expected)<10.0*abs(expected)/g,(label,g,v,observed,expected)
                checks+=1
    print(f'PASS {checks} standalone finite numerical checks; no infinite family is inferred from them.')

if __name__=='__main__':main()
