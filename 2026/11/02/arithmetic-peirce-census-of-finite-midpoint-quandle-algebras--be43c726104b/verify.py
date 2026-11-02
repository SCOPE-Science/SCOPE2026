#!/usr/bin/env python3
"""Finite cyclic checks for midpoint-quandle idempotents and Peirce polynomials.

Usage: python3 verify.py
Only the standard Python library is required. Numerical checks corroborate,
but do not replace, the characteristic-zero proof for arbitrary finite groups.
"""
from itertools import product
from cmath import exp
from math import pi
from collections import Counter

TOL = 2.e-7

def cycles(m):
    a = (m + 1) // 2
    unseen = set(range(m))
    ans = []
    while unseen:
        k = min(unseen)
        orbit = []
        z = k
        while z in unseen:
            unseen.remove(z)
            orbit.append(z)
            z = (z * a) % m
        assert z == k
        ans.append(tuple(orbit))
    return ans

def parameters(m):
    os = cycles(m)
    visited = set()
    params = []
    for o in os:
        if o in visited:
            continue
        partner = next(v for v in os if (-o[0]) % m in v)
        visited.add(o)
        visited.add(partner)
        ell = len(o)
        if o == (0,):
            params.append(('trivial', o, partner, [(0, 0), (1, 1)]))
        elif o == partner:
            assert ell % 2 == 0
            h = ell // 2
            assert o[h] == (-o[0]) % m
            order = 2**h + 1
            params.append(('self', o, partner, [(0, 0)] + [(j, order) for j in range(order)]))
        else:
            order = 2**ell - 1
            params.append(('paired', o, partner, [(0, 0)] + [(j, order) for j in range(order)]))
    return os, params

def emit(m, choices):
    cs = [0j] * m
    factors = []
    _, ps = parameters(m)
    for (kind, orb, other, _), (j, mod) in zip(ps, choices):
        ell = len(orb)
        active = mod != 0
        if kind == 'trivial':
            cs[0] = complex(j)
            factors.append((1, active, 1))
            continue
        if not active:
            factors.append((ell, False, 2 if kind == 'paired' else 1))
            continue
        z = exp(2j*pi*j/mod)
        for i, k in enumerate(orb):
            cs[k] = z**(2**((ell-i) % ell)) if i else z
            if kind == 'paired':
                cs[(-k) % m] = cs[k].conjugate()
        factors.append((ell, True, 2 if kind == 'paired' else 1))
    return cs, factors

def idempotent_coeffs(m, cs):
    # Inverse unnormalized character transform.
    return [sum(cs[k] * exp(-2j*pi*k*x/m) for k in range(m))/m for x in range(m)]

def direct_square(m, a):
    out = [0j]*m
    inv2 = (m+1)//2
    for x, vx in enumerate(a):
        for y, vy in enumerate(a):
            out[((x+y)*inv2) % m] += vx*vy
    return out

def multiply_poly(a, b):
    c=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b): c[i+j] += x*y
    return c

def expected_poly(factors):
    polynomial=[1]
    for ell, active, mult in factors:
        factor=([-1]+[0]*(ell-1)+[1]) if active else ([0]*ell+[1])
        for _ in range(mult): polynomial=multiply_poly(polynomial,factor)
    return polynomial

def matmul(A,B):
    n=len(A)
    return [[sum(A[i][k]*B[k][j] for k in range(n)) for j in range(n)] for i in range(n)]

def charpoly(M):
    # Faddeev-LeVerrier; ascending polynomial coefficients output.
    n=len(M)
    B=[[1.+0.j if i==j else 0j for j in range(n)] for i in range(n)]
    coefs=[1.+0j]
    for k in range(1,n+1):
        B=matmul(M,B)
        c=-sum(B[i][i] for i in range(n))/k
        coefs.append(c)
        for i in range(n): B[i][i]+=c
    return list(reversed(coefs))

def check(m):
    os, ps=parameters(m)
    pred_c = 1
    for o in os: pred_c*=2**len(o)
    assert pred_c==2**m
    pred_r = 1
    for typ,orb,other,options in ps: pred_r*=len(options)
    total = 0
    distribution = Counter()
    for choices in product(*[x[3] for x in ps]):
        total+=1
        cs,factors=emit(m,choices)
        assert max(abs(cs[(-k)%m]-cs[k].conjugate()) for k in range(m))<TOL
        # Idempotent equations in character coordinates (exact exponent pattern).
        for k in range(m):
            assert abs(cs[k]-cs[(k*(m+1)//2)%m]**2)<TOL, (m,k,choices)
        a=idempotent_coeffs(m,cs)
        assert max(abs(v.imag) for v in a)<TOL
        assert max(abs(x-y) for x,y in zip(a,direct_square(m,a)))<TOL
        expected=expected_poly(factors)
        M=[[a[(2*y-x)%m] for x in range(m)] for y in range(m)]
        observed=charpoly(M)
        assert max(abs(v-w) for v,w in zip(observed,expected))<5.e-5, (m,choices,observed,expected)
        distribution[tuple(expected)]+=1
    assert total==pred_r
    return {"m":m,"complex_idempotents":pred_c,"real_idempotents":total,"distinct_peirce_polynomials":len(distribution)}



def check_elementary_three_square():
    # An independent nine-dimensional noncyclic example G=C_3 x C_3.
    coordinates = list(product(range(3), repeat=2))
    iof = {v:i for i,v in enumerate(coordinates)}
    zero = (0,0)
    pairs = []
    seen={zero}
    for k in coordinates:
        if k in seen:
            continue
        neg=tuple((-t)%3 for t in k)
        pairs.append((k,neg))
        seen.add(k);seen.add(neg)
    assert len(pairs)==4
    phases=[0, 1, exp(2j*pi/3), exp(4j*pi/3)]
    distinct=set()
    poly_counts=Counter()
    for eps in (0,1):
        for values in product(phases,repeat=4):
            c={zero:complex(eps)}
            for (k,neg),v in zip(pairs,values):
                c[k]=v
                c[neg]=v*v
            assert all(abs(c[k]-c[tuple((-t)%3 for t in k)].conjugate())<TOL for k in coordinates)
            assert all(abs(c[k]-c[tuple(2*t%3 for t in k)]**2)<TOL for k in coordinates)
            a=[]
            for x in coordinates:
                val=sum(c[k]*exp(-2j*pi*sum(u*v for u,v in zip(k,x))/3) for k in coordinates)/9
                a.append(val)
            assert max(abs(v.imag) for v in a)<TOL
            sq=[0j]*9
            for x in coordinates:
                for y in coordinates:
                    target=tuple(2*(u+v)%3 for u,v in zip(x,y))
                    sq[iof[target]]+=a[iof[x]]*a[iof[y]]
            assert max(abs(t-v) for t,v in zip(sq,a))<TOL
            factors=[(1,bool(eps),1)]
            factors.extend((2,bool(abs(v)>TOL),1) for v in values)
            expected=expected_poly(factors)
            M=[]
            for y in coordinates:
                row=[]
                for x in coordinates:
                    z=tuple((2*u-v)%3 for u,v in zip(y,x))
                    row.append(a[iof[z]])
                M.append(row)
            got=charpoly(M)
            assert max(abs(z-w) for z,w in zip(expected,got))<5e-5
            poly_counts[tuple(expected)]+=1
            distinct.add(tuple(round(v.real,7) for v in a))
    assert len(distinct)==512
    print({'group':'C3 x C3','complex_idempotents':512,'real_idempotents':len(distinct),'distinct_peirce_polynomials':len(poly_counts)})

if __name__=='__main__':
    for m in (1,3,5,7,9,11,13):
        print(check(m))
    check_elementary_three_square()
    print('VERIFY_OK')
