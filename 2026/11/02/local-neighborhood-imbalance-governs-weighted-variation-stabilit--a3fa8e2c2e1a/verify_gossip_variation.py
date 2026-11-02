#!/usr/bin/env python3
"""Exact-rational checks of graph-edge mixing and weighted variation.

This checks finite examples; the general theorem is proved analytically.
"""
from fractions import Fraction as F
from itertools import product
from random import Random


def variation(w, x):
    return sum((a * abs(x[i] - x[j]) for (i, j), a in w.items()), F(0))


def mix(x, u, v, theta):
    y = list(x)
    y[u] = (1-theta)*x[u] + theta*x[v]
    y[v] = theta*x[u] + (1-theta)*x[v]
    return y


def d_neighbor(w, n, u, v):
    return sum((abs(w.get(tuple(sorted((u,z))), F(0)) - w.get(tuple(sorted((v,z))),F(0))) for z in range(n) if z not in (u,v)), F(0))


def cut_formula(w, n, u, v, theta):
    best = F(1)
    best_set = None
    for mask in range(1, 1<<n):
        if (mask & (1<<u)) and not (mask & (1<<v)):
            x = [F(bool(mask & (1<<i))) for i in range(n)]
            orig = variation(w,x)
            assert orig > 0
            gain = variation(w,mix(x,u,v,theta)) / orig
            if gain > best:
                best, best_set = gain, mask
    return best, best_set


def actual_gain(w, n, u, v, theta):
    x = [F(0)] * n
    x[u] = F(1)
    for z in range(n):
        if z in (u,v):
            continue
        alpha = w.get(tuple(sorted((u,z))), F(0))
        beta = w.get(tuple(sorted((v,z))), F(0))
        x[z] = F(1) if alpha >= beta else F(0)
    return variation(w,mix(x,u,v,theta)) - variation(w,x)


def test():
    rng = Random(20261025)
    counter = {"graphs":0, "sharp_gain":0, "norm_cut":0, "nonexpansive":0, "small_data":0, "star":0}
    angles = [F(0),F(1,7),F(1,3),F(1,2),F(2,3),F(4,5),F(1)]
    for n in range(3,8):
        for rep in range(120):
            # Random weighted connected simple graph, by a random spanning tree plus other edges.
            w = {}
            for i in range(1,n):
                j = rng.randrange(i)
                w[j,i] = F(rng.randint(1,5),rng.randint(1,4))
            for i in range(n):
                for j in range(i+1,n):
                    if (i,j) not in w and rng.randrange(3)==0:
                        w[i,j] = F(rng.randint(1,5),rng.randint(1,4))
            u,v = rng.choice(list(w))
            edge = w[u,v]
            D = d_neighbor(w,n,u,v)
            counter["graphs"] += 1
            for theta in angles:
                sharp = theta*D - 2*min(theta,1-theta)*edge
                assert actual_gain(w,n,u,v,theta) == sharp
                counter["sharp_gain"] += 1
                K, _ = cut_formula(w,n,u,v,theta)
                expected_contract = sharp <= 0
                assert (K<=1)==expected_contract
                counter["nonexpansive"] += 1
                # Direct, independent max over all binary indicators (not just cuts separated by u and v).
                K_direct=max(variation(w,mix([F(bool(mask & (1<<i))) for i in range(n)],u,v,theta)) / variation(w,[F(bool(mask & (1<<i))) for i in range(n)]) for mask in range(1,(1<<n)-1))
                assert K==K_direct
                counter["norm_cut"]+=1
                for rep2 in range(4):
                    x = [F(rng.randint(-3,3),rng.randint(1,3)) for _ in range(n)]
                    if x[u]==x[v]:
                        x[u]+=1
                    diff=variation(w,mix(x,u,v,theta))-variation(w,x)
                    assert diff <= sharp*abs(x[u]-x[v])
                    if variation(w,x)>0:
                        assert variation(w,mix(x,u,v,theta)) <= K*variation(w,x)
                    counter["small_data"]+=1
    for m in range(2,15):
        n=m+1
        w={(0,i):F(1) for i in range(1,n)}
        for theta in angles:
            # Construct sharp test with x_0=1, x_1=0, and all other leaves=1.
            x=[F(1)]*n
            x[1]=F(0)
            measured=variation(w,mix(x,0,1,theta))
            asserted=abs(1-2*theta) + (m-1)*theta
            assert measured==asserted
            K,_ = cut_formula(w,n,0,1,theta)
            assert K==max(F(1),asserted)
            counter["star"]+=1
    return counter

if __name__ == '__main__':
    print(test())


def mincut_threshold_value(w, n, u, v, theta, target_norm):
    """Return min_S [(target_norm-1) cut(S) - theta sum_z sigma_z d_z]."""
    import networkx as nx
    graph=nx.DiGraph()
    graph.add_nodes_from(range(n))
    def add(a,b,c):
        if c <=0:
            return
        old=graph[a][b]['capacity'] if graph.has_edge(a,b) else F(0)
        graph.add_edge(a,b,capacity=old+c)
    for (i,j),a in w.items():
        add(i,j,(target_norm-1)*a)
        add(j,i,(target_norm-1)*a)
    offset=F(0)
    for z in range(n):
        if z in (u,v): continue
        d=w.get(tuple(sorted((u,z))),F(0))-w.get(tuple(sorted((v,z))),F(0))
        offset += theta*d
        if d>0:
            add(u,z,2*theta*d)
            offset -= 2*theta*d
        elif d<0:
            add(z,v,-2*theta*d)
    value,_=nx.minimum_cut(graph,u,v,capacity='capacity')
    return F(value)+offset


def verify_mincut():
    rng=Random(53019)
    count=0
    for n in range(3,9):
        for rep in range(80):
            w={}
            for j in range(1,n):
                i=rng.randrange(j)
                w[i,j]=F(rng.randint(1,5),rng.randint(1,4))
            for i in range(n):
                for j in range(i+1,n):
                    if (i,j) not in w and rng.randrange(3)==0:
                        w[i,j]=F(rng.randint(1,5),rng.randint(1,4))
            u,v=rng.choice(list(w))
            theta=rng.choice([F(1,4),F(1,2),F(3,4),F(1)])
            k=rng.choice([F(1),F(6,5),F(3,2),F(2),F(4)])
            exact=min((k-1)*variation(w,[F(bool(mask & (1<<i))) for i in range(n)])
                      -theta*sum(( (F(1) if (mask & (1<<z)) else F(-1)) * (w.get(tuple(sorted((u,z))),F(0))-w.get(tuple(sorted((v,z))),F(0))) for z in range(n) if z not in (u,v)), F(0))
                      for mask in range(1,1<<n) if (mask & (1<<u)) and not (mask & (1<<v)))
            asserted=mincut_threshold_value(w,n,u,v,theta,k)
            assert exact==asserted,(n,w,u,v,theta,k,exact,asserted)
            count+=1
    return count

if __name__ == '__main__':
    print('mincut comparisons',verify_mincut())
