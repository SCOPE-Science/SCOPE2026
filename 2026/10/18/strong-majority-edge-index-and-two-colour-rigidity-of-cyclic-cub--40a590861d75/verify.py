#!/usr/bin/env python3
"""Separate exact checks for strong-majority edge colourings of cyclic cubic ladders.

All graph instances and all adjacent-edge sets are built afresh. The zero-one
linear feasibility tests do not use the analytic period-four argument.
"""
from itertools import product
from collections import defaultdict
import numpy as np
from scipy.optimize import milp, Bounds, LinearConstraint


def build(kind,n):
    if kind=='prism':
        assert n>=3
        edges=[]
        for layer in (0,1):
            for i in range(n):
                u=layer*n+i;v=layer*n+(i+1)%n
                edges.append(tuple(sorted((u,v))))
        for i in range(n):
            edges.append((i,n+i))
    else:
        assert kind=='mobius' and n>=2
        edges=[tuple(sorted((i,(i+1)%(2*n)))) for i in range(2*n)]
        edges.extend((i,n+i) for i in range(n))
    assert len(edges)==3*n and len(set(edges))==len(edges)
    nbr=[]
    for k,(u,v) in enumerate(edges):
        nbr.append([j for j,(x,y) in enumerate(edges) if k!=j and (u==x or u==y or v==x or v==y)])
    assert all(len(x)==4 for x in nbr)
    return edges,nbr


def checked(col,nbr,number_colors):
    assert len(col)==len(nbr)
    return all(all(sum(col[j]==t for j in adj)<=len(adj)//2
                   for t in range(number_colors)) for adj in nbr)


def construction(kind,n,a0=0,a1=0,c0=0):
    assert (kind=='prism' and n%4==0) or (kind=='mobius' and n%4==2)
    aa=[a0,a1,1-a0,1-a1]
    top=[aa[i%4] for i in range(n)]
    bottom=[1-x for x in top]
    rung=[c0^i%2 for i in range(n)]
    return top+bottom+rung


def proper3(kind,n):
    if kind=='prism':
        rim=[i%2 for i in range(n)] if n%2==0 else [i%2 for i in range(n-1)]+[2]
        missing=[({0,1,2}-{rim[(i-1)%n],rim[i]}).pop() for i in range(n)]
        return rim+rim+missing
    return [i%2 for i in range(2*n)]+[2]*n


def count_exhaustive(kind,n):
    edges,nbr=build(kind,n); m=len(edges)
    count=0
    for mask in range(1<<m):
        # exactly half red among four neighbours at every edge
        if all(sum((mask>>j)&1 for j in adj)==2 for adj in nbr):count+=1
    return count


def feasible_milp(kind,n):
    _,nbr=build(kind,n)
    m=len(nbr)
    A=np.zeros((m,m))
    for i,adj in enumerate(nbr): A[i,adj]=1
    constraints=LinearConstraint(A,np.full(m,2.),np.full(m,2.))
    res=milp(np.zeros(m),integrality=np.ones(m),bounds=Bounds(0.,1.),constraints=constraints, options={'time_limit':5.0})
    if res.status==0:
        v=np.rint(res.x).astype(int).tolist()
        assert checked(v,nbr,2)
        return True
    if res.status==2: return False
    raise RuntimeError(f'MILP inconclusive for {kind} n={n}: {res.status} {res.message}')


def main():
    exhaustive=0; numerics=0; constructions=0
    for kind in ('prism','mobius'):
        first=3 if kind=='prism' else 2
        for n in range(first,7):
            num=count_exhaustive(kind,n)
            predicted=8 if ((n%4==0) if kind=='prism' else (n%4==2)) else 0
            assert num==predicted,(kind,n,num,predicted)
            exhaustive+=1
        for n in range(first,81):
            predicted=(n%4==0) if kind=='prism' else (n%4==2)
            assert feasible_milp(kind,n)==predicted,(kind,n)
            numerics+=1
            edges,nbr=build(kind,n)
            assert checked(proper3(kind,n),nbr,3)
            constructions+=1
            if predicted:
                for a0,a1,c0 in product((0,1),repeat=3):
                    color=construction(kind,n,a0,a1,c0)
                    assert checked(color,nbr,2)
                    constructions+=1
    print(f'PASS: {exhaustive} exhaustive two-colour counts (8 or 0)')
    print(f'PASS: {numerics} independent binary-MILP feasibility checks')
    print(f'PASS: {constructions} constructive two/three-colour checks')
    print('Range: prism 3..80; Mobius 2..80.')
    print('Exactly eight named two-colourings in every feasible instance.')

if __name__=='__main__':main()
