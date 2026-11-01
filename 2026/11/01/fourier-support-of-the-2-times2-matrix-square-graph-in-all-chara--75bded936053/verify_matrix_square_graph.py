#!/usr/bin/env python3
"""Exact finite-field checks for the Fourier support of the matrix-square graph.

Usage: python3 verify_matrix_square_graph.py
The sums are evaluated as integer cyclotomic coefficients (odd characteristic)
or as integer Walsh sums (characteristic two); no floating tolerance is used.
"""
from collections import Counter
from itertools import product
import random


def finite_field(q):
    if q == 4:
        p = 2
        def add(a, b): return a ^ b
        def mul(a, b):
            a0, a1 = a & 1, a >> 1
            b0, b1 = b & 1, b >> 1
            return (a0*b0 ^ a1*b1) | ((a0*b1 ^ a1*b0 ^ a1*b1) << 1)
        def character_exponent(a): return (a >> 1) & 1
    elif q == 9:
        p = 3
        def add(a, b): return ((a % 3 + b % 3) % 3) + 3*((a//3 + b//3) % 3)
        def mul(a, b):
            a0, a1 = a % 3, a // 3
            b0, b1 = b % 3, b // 3
            return ((a0*b0 + 2*a1*b1) % 3) + 3*((a0*b1 + a1*b0) % 3)
        def character_exponent(a): return (2*(a % 3)) % 3
    else:
        assert q in (2, 3, 5)
        p = q
        def add(a, b): return (a+b) % q
        def mul(a, b): return (a*b) % q
        def character_exponent(a): return a
    return p, add, mul, character_exponent


def verify(q, exhaustive=False, samples=200):
    p, add, mul, phase = finite_field(q)
    values = range(q)
    zero = (0, 0, 0, 0)
    identity = (1, 0, 0, 1)
    matrices = list(product(values, repeat=4))
    def minus(a):
        if p == 2: return a
        return next(b for b in values if add(a,b) == 0)
    def matmul(x,y):
        return (add(mul(x[0],y[0]),mul(x[1],y[2])),
                add(mul(x[0],y[1]),mul(x[1],y[3])),
                add(mul(x[2],y[0]),mul(x[3],y[2])),
                add(mul(x[2],y[1]),mul(x[3],y[3])))
    def trace(x): return add(x[0],x[3])
    def traceprod(x,y): return trace(matmul(x,y))
    def det(x): return add(mul(x[0],x[3]),minus(mul(x[1],x[2])))
    def fieldpow(a,n):
        z=1
        for _ in range(n): z=mul(z,a)
        return z
    def lincomb(a,b,x): return tuple(add(mul(a,u),mul(b,v)) for u,v in zip(identity,x))
    def predicted(A,B):
        t=trace(B)
        if p != 2:
            if B == zero: return A == zero,0
            if t == 0:
                return any(A==lincomb(a,b,B) for a in values for b in values),2
            if det(B) == 0:
                return traceprod(A,B)==mul(t,trace(A)),3
            return True,4
        if B == (B[0],0,0,B[0]):
            c=fieldpow(B[0],q//2)
            return A == (c,0,0,c),0
        B3=matmul(matmul(B,B),B)
        return (trace(A)==fieldpow(trace(B),q//2)
                and traceprod(A,B)==fieldpow(trace(B3),q//2)),2
    if exhaustive:
        pairs = product(matrices, repeat=2)
    else:
        rng=random.Random(5411 + q)
        pairs = [(rng.choice(matrices),rng.choice(matrices)) for _ in range(samples)]
        pairs += [(zero,B) for B in matrices[:min(len(matrices),150)]]
        pairs += [(identity,B) for B in matrices[:min(len(matrices),150)]]
    x_squares=[(x,matmul(x,x)) for x in matrices]
    checked=0; amplitudes=Counter()
    for A,B in pairs:
        should_survive,r=predicted(A,B)
        coeffs=[0]*p
        for X,X2 in x_squares:
            s=add(traceprod(A,X),traceprod(B,X2))
            coeffs[phase(s)]+=1
        if p == 2:
            w=coeffs[0]-coeffs[1]
            observed_survival=(w!=0)
            squared_abs=w*w
        else:
            observed_survival=(len(set(coeffs))!=1)
            corr=[sum(coeffs[j]*coeffs[(j+d)%p] for j in range(p)) for d in range(p)]
            assert len(set(corr[1:])) == 1, (q,A,B,corr)
            squared_abs=corr[0]-corr[1]
        assert observed_survival == should_survive,(q,A,B,coeffs,should_survive)
        expected=q**(8-r) if should_survive else 0
        assert squared_abs==expected,(q,A,B,squared_abs,expected)
        checked+=1
        if should_survive: amplitudes[r]+=1
    # Classify all second-coordinate frequencies independently of Fourier samples.
    classes=Counter()
    for B in matrices:
        t=trace(B)
        if p==2: r=0 if B==(B[0],0,0,B[0]) else 2
        elif B==zero:r=0
        elif t==0:r=2
        elif det(B)==0:r=3
        else:r=4
        classes[r]+=1
    if p==2:
        assert classes == Counter({0:q,2:q**4-q})
        rank=q**6-q**3+q
    else:
        assert classes==Counter({0:1,2:q**3-1,3:q**3-q,4:q**4-2*q**3+q})
        rank=q**8-2*q**7+q**6+2*q**5-q**4-q**2+1
    assert sum(v*q**r for r,v in classes.items())==rank
    print('MATRIX_SQUARE_FOURIER_OK', 'q=',q, 'tested=',checked,
          'rank=',rank, 'ambient=',q**8,'frequency_class_counts=',dict(classes),
          'observed_nonzero=',dict(amplitudes),flush=True)

if __name__=='__main__':
    for q,complete,n in [(2,True,0),(3,True,0),(4,False,400),(5,False,500),(9,False,50)]:
        verify(q,complete,n)
    print('ALL_MATRIX_SQUARE_EXACT_CHECKS_OK')
