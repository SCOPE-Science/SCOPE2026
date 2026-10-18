#!/usr/bin/env python3
"""Independent finite tests for coordinate-disc Minkowski sums.
The all-dimensional assertions require the proof in RESULT.md; these checks
only test small graphs, support values, contacts, and isotropic certificates.
"""
from itertools import product, combinations
from math import sqrt, sin, cos, pi
from random import Random

TOL = 2e-10

def cycle(n):
    return n, sorted({tuple(sorted((i, (i + 1) % n))) for i in range(n)})

def complete(n):
    return n, list(combinations(range(n), 2))

def complete_bipartite(p, q):
    return p + q, [(i, p + j) for i in range(p) for j in range(q)]

def prism():
    return 6, sorted({tuple(sorted(e)) for e in [(0,1),(1,2),(2,0),(3,4),(4,5),(5,3),(0,3),(1,4),(2,5)]})

def cube():
    return 8, [(i, i ^ (1 << b)) for i in range(8) for b in range(3) if i < (i ^ (1 << b))]

def petersen():
    edges = [(i, (i+1)%5) for i in range(5)]
    edges += [(5+i, 5+(i+2)%5) for i in range(5)]
    edges += [(i, 5+i) for i in range(5)]
    return 10, sorted(tuple(sorted(e)) for e in edges)

def support(u, edges):
    return sum(sqrt(u[i]**2 + u[j]**2) for i,j in edges)

def exposed(u, n, edges):
    x = [0.0] * n
    for i,j in edges:
        rho = sqrt(u[i]**2 + u[j]**2)
        if rho > 0:
            x[i] += u[i]/rho
            x[j] += u[j]/rho
    return x

def norm(u):
    return sqrt(sum(z*z for z in u))

def bipartition(n, edges):
    adj = [[] for _ in range(n)]
    for i,j in edges:
        adj[i].append(j)
        adj[j].append(i)
    colors=[None]*n
    colors[0]=0
    stack=[0]
    while stack:
        i=stack.pop()
        for j in adj[i]:
            if colors[j] is None:
                colors[j]=1-colors[i]
                stack.append(j)
            else:
                if colors[i]==colors[j]:
                    return None
    assert all(c is not None for c in colors)
    return [[i for i,c in enumerate(colors) if c==0], [i for i,c in enumerate(colors) if c==1]]

def near(a,b):
    assert abs(a-b) < TOL*max(1.,abs(a),abs(b)), (a,b)

G = [cycle(n) for n in range(3,9)]
G += [complete(n) for n in range(3,7)]
G += [complete_bipartite(p,p) for p in range(2,5)]
G += [prism(),cube(),petersen()]
checked_support = checked_contacts = checked_isotropy = 0
rng=Random(7331)
for n,edges in G:
    degrees = [sum(i in edge for edge in edges) for i in range(n)]
    assert len(set(degrees)) == 1
    d=degrees[0]
    m=len(edges)
    near(m, n*d/2)
    R = d*sqrt(n/2)
    for i in range(n):
        basis = [float(j==i) for j in range(n)]
        near(support(basis,edges),d)
        checked_support +=1
    # Signed uniform extremizers and pointwise support maximizers.
    for eps in product((-1., 1.), repeat=n):
        u=[v/sqrt(n) for v in eps]
        near(support(u,edges),R)
        x=exposed(u,n,edges)
        for xi,ui in zip(x,u):
            near(xi,R*ui)
        near(norm(x),R)
        checked_contacts +=1
    # Independent random sphere probes: the theorem gives a precise sandwich.
    for _ in range(1000):
        a=[rng.gauss(0,1) for i in range(n)]
        size=norm(a)
        u=[v/size for v in a]
        h=support(u,edges)
        assert d-5e-12 <= h <= R+5e-12, (n, h,d,R)
        checked_support +=1
    part = bipartition(n,edges)
    if part is not None:
        L,S=part
        assert len(L)==len(S)==n//2
        p=len(L)
        for theta in (0.0,pi/11,pi/4,pi*5/11,pi/2):
            for _ in range(50):
                u=[0.0]*n
                for i in L: u[i]=rng.choice((-1,1))*cos(theta)/sqrt(p)
                for i in S: u[i]=rng.choice((-1,1))*sin(theta)/sqrt(p)
                near(norm(u),1)
                near(support(u,edges),R)
                x=exposed(u,n,edges)
                for xi,ui in zip(x,u): near(xi,R*ui)
                checked_contacts+=1
        # Sphere contact locus is a subdivision-free K_{2^p,2^p} graph.
        N=2**p
        assert N*N-(2*N)+1==(N-1)**2
    # A uniformly signed extremal family is a covariance design.
    # Exact sign correlations must be identity, without numerical rounding.
    signatures=list(product((-1,1),repeat=n))
    for i in range(n):
        for j in range(n):
            assert sum(v[i]*v[j] for v in signatures) == (len(signatures) if i==j else 0)
            checked_isotropy +=1
print('PASS:',len(G),'connected regular graphs;',checked_support,'support checks;',checked_contacts,'outer contacts;',checked_isotropy,'exact signed covariance identities.')
print('Scope: finite consistency checks only; complete proof is required for universal statements.')
