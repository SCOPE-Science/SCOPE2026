#!/usr/bin/env python3
"""Standalone finite checks for adaptive-confidence pairwise averaging.

These tests check transition formulas and examples, not infinite-time probability-one claims.
"""
from fractions import Fraction as Q
from random import Random


def step(x, c, edges, edge_index, mu, gamma, delta):
    x = list(x)
    c = list(c)
    i, j = edges[edge_index]
    active = abs(x[i] - x[j]) < c[edge_index]
    if active:
        xi, xj = x[i], x[j]
        x[i] = (1 - mu) * xi + mu * xj
        x[j] = mu * xi + (1 - mu) * xj
        c[edge_index] = c[edge_index] + gamma * (1 - c[edge_index])
    else:
        c[edge_index] = delta * c[edge_index]
    return x, c, active


def energy(x):
    return sum((z*z for z in x), Q(0))


def exact_checks():
    rng = Random(20261024)
    edges = [(0,1),(1,2),(2,3)]
    for _ in range(250):
        x = [Q(rng.randrange(101),100) for _ in range(4)]
        c = [Q(rng.randrange(1,100),100) for _ in edges]
        mu = Q(rng.randrange(1,51),100)
        gamma = Q(rng.randrange(1,101),100)
        delta = Q(rng.randrange(0,100),100)
        k = rng.randrange(len(edges))
        y, d, active = step(x,c,edges,k,mu,gamma,delta)
        assert sum(y) == sum(x)
        assert all(Q(0)<=v<=Q(1) for v in y+d)
        i,j = edges[k]
        assert energy(x)-energy(y) == (
            2*mu*(1-mu)*(x[i]-x[j])**2 if active else Q(0)
        )
        if active:
            assert d[k]>=gamma
        else:
            assert d[k]==delta*c[k]
        for h in range(len(edges)):
            if h!=k: assert d[h]==c[h]
    return 250


def exact_fixed_examples():
    rng=Random(44)
    edges=[(0,1),(1,2)]
    # One permanently receptive edge and one permanently blocked edge.
    x=[Q(1,10),Q(3,25),Q(9,10)]
    c=[Q(1,4),Q(1,4)]
    for t in range(800):
        assert abs(x[0]-x[1])<c[0]
        assert abs(x[1]-x[2])>=c[1]
        x,c,_=step(x,c,edges,rng.randrange(2),Q(1,4),Q(1,3),Q(3,5))
    assert c[0]>Q(999,1000) and c[1]<Q(1,1000000)
    return 800


def floating_smoke():
    rng=Random(2026)
    edges=[(0,1),(1,2),(2,3),(3,4),(0,4)]
    total=0
    for _ in range(30):
        x=[rng.random() for _ in range(5)]
        c=[0.2+0.7*rng.random() for _ in edges]
        mu=0.15+0.3*rng.random()
        gamma=0.08+0.7*rng.random()
        delta=0.1+0.8*rng.random()
        target=sum(x)
        oldenergy=sum(z*z for z in x)
        for _ in range(400):
            k=rng.randrange(len(edges))
            x,c,_=step(x,c,edges,k,mu,gamma,delta)
            newenergy=sum(z*z for z in x)
            assert abs(sum(x)-target)<1e-9
            assert newenergy<=oldenergy+1e-13
            assert all(-1e-15<=v<=1+1e-15 for v in c)
            oldenergy=newenergy
            total+=1
    return total


if __name__=='__main__':
    a=exact_checks()
    b=exact_fixed_examples()
    z=floating_smoke()
    print(f'VERIFY_OK exact_rational_transitions={a} exact_fixed_updates={b} stochastic_steps={z}')
