#!/usr/bin/env python3
"""Finite checks for cyclic planar vertex-normal cone facets and rays.

All mathematical conclusions for arbitrary N follow from the proof in RESULT.md;
this checker tests combinatorial counts, explicit closure, support inequalities,
and numerical ranks for small dimensions. Uses the Python standard library only.
"""
import itertools
import math

TOL = 2e-8

def rank(rows, threshold=1e-8):
    if not rows:
        return 0
    mat = [list(row) for row in rows]
    m, n = len(mat), len(mat[0])
    r = 0
    for c in range(n):
        k = max(range(r, m), key=lambda h: abs(mat[h][c])) if r < m else None
        if k is None or abs(mat[k][c]) < threshold:
            continue
        mat[r], mat[k] = mat[k], mat[r]
        pivot = mat[r][c]
        for j in range(c, n):
            mat[r][j] /= pivot
        for i in range(r+1, m):
            factor = mat[i][c]
            for j in range(c, n):
                mat[i][j] -= factor*mat[r][j]
        r += 1
        if r == m:
            break
    return r

def expected_triangles(n):
    if n%2:
        return n*(n*n-1)//24
    return n*(n-2)*(n-4)//24

def expected_rays(n):
    if n%2:
        return n*(n*n-1)//3
    return n*(n-2)*(n-4)//3+2*n

def triples(n):
    for i,j,k in itertools.combinations(range(n),3):
        if 2*max(j-i,k-j,n+i-k) < n:
            yield (i,j,k)

def supports(n):
    # The order of the two copies of tangent t_i is: lambda_i, mu_(i-1).
    for i,j,k in triples(n):
        theta = 2*math.pi/n
        weights = (math.sin((k-j)*theta),
                   math.sin((n+i-k)*theta),
                   math.sin((j-i)*theta))
        for choices in itertools.product((0,1), repeat=3):
            coeffs = [0.0]*(2*n)
            for index, occurrence, weight in zip((i,j,k), choices, weights):
                coeffs[2*index if occurrence == 0 else 2*((index-1)%n)+1] = weight
            yield coeffs
    if n%2 == 0:
        for i in range(n//2):
            for a,b in itertools.product((0,1),repeat=2):
                coeffs=[0.0]*(2*n)
                for index,occ in ((i,a),(i+n//2,b)):
                    coeffs[2*index if occ==0 else 2*((index-1)%n)+1]=1.0
                yield coeffs

def check(n):
    theta=2*math.pi/n
    a=[(math.cos(i*theta),math.sin(i*theta)) for i in range(n)]
    t=[(-v,u) for u,v in a]
    ts=list(triples(n))
    assert len(ts)==expected_triangles(n), (n,len(ts),expected_triangles(n))
    rays=list(supports(n))
    assert len(rays)==expected_rays(n), (n,len(rays),expected_rays(n))
    # A strict interior point: x_i = a_i; its adjacent slack coordinates
    # satisfy lambda_i = mu_i = tan(pi/n) > 0.
    tangent_weight=math.tan(math.pi/n)
    baseline=[tangent_weight]*(2*n)
    # Every coordinate inequality supports a facet: transfer its positive
    # weight to the other copy of the same tangent, leaving exactly one zero.
    for q in range(2*n):
        qq=q//2
        duplicate=(2*((qq-1)%n)+1) if q%2==0 else 2*((qq+1)%n)
        witness=baseline.copy()
        witness[duplicate]+=witness[q]
        witness[q]=0.0
        assert sum(w==0.0 for w in witness)==1
        vx=sum(witness[2*i]*t[i][0]+witness[2*i+1]*t[(i+1)%n][0] for i in range(n))
        vy=sum(witness[2*i]*t[i][1]+witness[2*i+1]*t[(i+1)%n][1] for i in range(n))
        assert abs(vx)+abs(vy)<TOL
    # Each listed ray satisfies all original support inequalities and is
    # extreme, verified by active-inequality rank after fixing translations.
    for coeff in rays:
        edge=[(coeff[2*i]*t[i][0]+coeff[2*i+1]*t[(i+1)%n][0],
               coeff[2*i]*t[i][1]+coeff[2*i+1]*t[(i+1)%n][1]) for i in range(n)]
        assert sum(abs(sum(edge[i][k] for i in range(n))) for k in (0,1))<TOL
        x=[(0.,0.)]
        for i in range(n-1):
            x.append((x[-1][0]+edge[i][0],x[-1][1]+edge[i][1]))
        active=[]
        for i in range(n):
            for j in range(n):
                if i==j:continue
                slack=a[i][0]*(x[i][0]-x[j][0])+a[i][1]*(x[i][1]-x[j][1])
                assert slack>-TOL,(n,i,j,slack)
                if slack<1e-8:
                    row=[0.]*(2*n)
                    row[2*i],row[2*i+1]=a[i]
                    row[2*j],row[2*j+1]=(-a[i][0],-a[i][1])
                    active.append(row)
        assert rank(active)==2*n-3,(n,rank(active),2*n-3)
    print(f'n={n}: triangles={len(ts)}, rays={len(rays)}, facets={2*n}, rank-certified rays={len(rays)}')

if __name__=='__main__':
    for n in range(3,13):
        check(n)
    print('All finite checks passed; the arbitrary-n assertions depend on the written proof.')
