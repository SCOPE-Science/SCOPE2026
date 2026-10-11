#!/usr/bin/env python3
"""Reproduce spherical graphical-zonotope width moment checks.

Uses only Python's standard library; finite diagnostics do not establish the
all-dimensional theorem, whose proof is supplied separately.
"""
import itertools
import math
import random

DELTA = 1.0 / 3.0 + (2.0 * math.sqrt(3.0) - 4.0) / math.pi
assert DELTA > 0


def prufer_edges(seq, n):
    degree = [1] * n
    for x in seq:
        degree[x] += 1
    edges = []
    for x in seq:
        leaf = next(i for i in range(n) if degree[i] == 1)
        edges.append((min(leaf, x), max(leaf, x)))
        degree[leaf] -= 1
        degree[x] -= 1
    a, b = [i for i, v in enumerate(degree) if v == 1]
    edges.append((min(a,b),max(a,b)))
    return edges


def graph_moments(n, edges):
    assert n >= 3
    deg = [0] * n
    for i, j in edges:
        deg[i] += 1
        deg[j] += 1
    m = len(edges)
    wedges = sum(k * (k-1)//2 for k in deg)
    d = n-1
    c = math.exp(math.lgamma(d/2)-math.lgamma((d+1)/2)) / math.sqrt(math.pi)
    mean = m * math.sqrt(2) * c
    second = (2*m + 8*math.comb(m,2)/math.pi + 2*wedges*DELTA)/d
    return mean, second, second-mean**2, wedges


def check_pairs(n, edges):
    w = 0
    for e,f in itertools.combinations(edges,2):
        a,b = e
        c,d = f
        dot = (a==c)-(a==d)-(b==c)+(b==d)
        assert dot in (-1,0,1)
        if dot:
            w += 1
    assert w == graph_moments(n,edges)[3]


def circular_correlation(rho, count=65536):
    angle = math.acos(rho)
    total = math.fsum(abs(math.cos((i+0.5)*2*math.pi/count) * math.cos((i+0.5)*2*math.pi/count-angle)) for i in range(count))
    return 2*total/count

for rho in (0,0.5,-0.5,1):
    expected = 2/math.pi*(math.sqrt(1-rho**2)+rho*math.asin(rho))
    got = circular_correlation(rho)
    assert abs(got-expected)<1.0e-8, (rho, got,expected)

count=0
for n in range(3,8):
    for seq in itertools.product(range(n),repeat=n-2):
        edges=prufer_edges(seq,n)
        count+=1
        check_pairs(n,edges)
        mean,second,var,w=graph_moments(n,edges)
        assert var>0 and n-2 <= w <= math.comb(n-1,2)
        degree=[0]*n
        for i,j in edges:
            degree[i]+=1
            degree[j]+=1
        if w==n-2:
            assert max(degree)<=2
        if w==math.comb(n-1,2) and n>=4:
            assert max(degree)==n-1

# Direct random spherical width checks are independent of the pair-correlation decomposition.
rng = random.Random(104729)
for n,edges in (
    (4,[(0,1),(1,2),(2,3)]),
    (4,[(0,1),(0,2),(0,3)]),
    (6,[(0,i) for i in range(1,6)]),
    (6,[(i,i+1) for i in range(5)]),
    (5,[(0,1),(1,2),(2,3),(3,0),(0,4)]),
):
    sample=[]
    for _ in range(160000):
        g=[rng.gauss(0,1) for _ in range(n)]
        mu=sum(g)/n
        norm=math.sqrt(sum((z-mu)**2 for z in g))
        sample.append(sum(abs(g[i]-g[j]) for i,j in edges)/norm)
    mean=sum(sample)/len(sample)
    sec=sum(v*v for v in sample)/len(sample)
    target_mean,target_sec,var,w=graph_moments(n,edges)
    assert abs(mean-target_mean)<0.025, (n,edges,'mean',mean,target_mean)
    assert abs(sec-target_sec)<0.075, (n,edges,'second',sec,target_sec)

n=1001
d=n-1
path=graph_moments(n,[(i,i+1) for i in range(n-1)])[2]
star=graph_moments(n,[(0,i) for i in range(1,n)])[2]
limit=2+2*DELTA-6/math.pi
assert abs(path-limit)<0.001
assert abs(star/n-DELTA)<0.001
print('VERIFY_OK', 'trees_checked=',count, 'delta=',format(DELTA,'.15f'), 'path_limit=',format(limit,'.15f'), 'large_n_path=',format(path,'.12f'), 'large_n_star_per_n=',format(star/n,'.12f'))
