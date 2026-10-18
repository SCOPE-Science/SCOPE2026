#!/usr/bin/env python3
"""Numerical and exact-arithmetic checks for an isotropic-line component-count formula.
No external dependencies. This is corroborating finite computation, not an infinite proof.
"""
import math
import random
from fractions import Fraction as Q


def f(s):
    if not 0 <= s < 1:
        raise ValueError('Require 0 <= s < 1')
    return s * math.asin(s) + math.sqrt(1-s*s) - 1


def formula_pair(d, r, perimeter):
    return 2*d*f(2*r/d)/perimeter


def simpson(fn, a, b, N=16384):
    assert N % 2 == 0
    h = (b-a)/N
    return h/3*(fn(a)+fn(b)+4*sum(fn(a+h*j) for j in range(1,N,2))+2*sum(fn(a+h*j) for j in range(2,N,2)))


def integrated_pair(d, r, perimeter):
    # Discarding orientation and integrating offset overlap independently.
    return 2*simpson(lambda th: 2*r-d*math.cos(th), math.acos(2*r/d), math.pi/2)/perimeter


def sim_random_lines_two_disks():
    # Rejection sampling from invariant lines conditioned on meeting [-L,L]^2.
    L, r, d = 3., .85, 2.
    perimeter=8*L
    rng = random.Random(1729)
    matched=0
    hits=0
    N=350000
    for _ in range(N):
        while True:
            th = rng.random()*math.pi
            a,b = math.cos(th), math.sin(th)
            t = (rng.random()*2-1)*L*math.sqrt(2)
            halfwidth = L*(abs(a)+abs(b))
            if abs(t)<halfwidth:
                break
        hi = abs(t+d*a/2) <r
        hj = abs(t-d*a/2) <r
        matched += hi and hj
        hits += hi + hj
    prob=matched/N
    theoretical=formula_pair(d,r,perimeter)
    assert abs(prob-theoretical)<.004,(prob,theoretical)
    assert abs(hits/N-(4*math.pi*r/perimeter))<.006
    return prob,theoretical


def c(k):
    return Q(math.comb(2*k-2,k-1), (4**(k-1))*(2*k-1)*(2*k))


def moment_from_distances(dists, j):
    return sum((Q(1,d)**(2*j+1) for d in dists), Q(0))


def solve(A, b):
    A = [list(row)+[rhs] for row,rhs in zip(A,b)]
    n=len(b)
    for k in range(n):
        pivot=next((i for i in range(k,n) if A[i][k]), None)
        if pivot is None: raise ValueError('singular')
        A[k],A[pivot]=A[pivot],A[k]
        z=A[k][k]
        A[k]=[x/z for x in A[k]]
        for i in range(n):
            if i==k:continue
            z=A[i][k]
            A[i]=[x-z*y for x,y in zip(A[i],A[k])]
    return [A[i][-1] for i in range(n)]


def hankel_rank(moments, maxdim):
    # Leading principal Hankel minors positive until exactly the distinct support size.
    for n in range(1,maxdim+1):
        try:
            solve([[moments[i+j] for j in range(n)] for i in range(n)],
                  [Q(1)]+[Q(0)]*(n-1))
        except ValueError:
            return n-1
    return maxdim


def recover_polynomial(moments, maxdim):
    L=hankel_rank(moments,maxdim)
    A=[[moments[i+j] for j in range(L)] for i in range(L)]
    b=[-moments[i+L] for i in range(L)]
    return solve(A,b)+[Q(1)]


def polynomial_from_roots(xs):
    p=[Q(1)]
    for x in xs:
        q=[Q(0)]*(len(p)+1)
        for j,a in enumerate(p):
            q[j]-=x*a
            q[j+1]+=a
        p=q
    return p


def main():
    total=0
    for r,d,P in [(0.2,1.0,18.),(.4,1.6,24.),(.85,2.0,24.),(.1,5.,40.),(.75,4.,50.)]:
        q=integrated_pair(d,r,P)
        e=formula_pair(d,r,P)
        assert abs(q-e)<1e-10,(r,d,P,q,e)
        total+=1
    # Collinear but distinct perforation centers; six pairs, one repeated distance.
    sites=[0,1,3,6]
    ds=[abs(sites[i]-sites[j]) for i in range(4) for j in range(i+1,4)]
    assert sorted(ds)==[1,2,3,3,5,6]
    M=len(ds)
    moments=[moment_from_distances(ds,j) for j in range(2*M)]
    p=recover_polynomial(moments,M)
    roots=[Q(1,d*d) for d in sorted(set(ds))]
    assert p == polynomial_from_roots(roots)
    # Verify all 12 coefficients of the second-factorial Taylor series.
    coeffs=[]
    for k in range(1,2*M+1):
        coeff = (Q(2**(2*k+1))*c(k)/Q(80)) * moments[k-1]
        assert coeff>0
        coeffs.append(coeff)
        total+=1
    for r in (.08, .12, .17):
        direct = sum(formula_pair(float(d),r,80.) for d in ds)
        series = sum(float(coeff)*(r**(2*k)) for k,coeff in enumerate(coeffs,1))
        assert abs(direct-series)<3e-14,(r,direct,series)
    sample,theory=sim_random_lines_two_disks()
    print(f'LINE_TOPOLOGY_INVERSE_OK comparisons={total+2} exact_roots={len(roots)} sample_pair={sample:.6f} predicted_pair={theory:.6f}')

if __name__=='__main__':
    main()
