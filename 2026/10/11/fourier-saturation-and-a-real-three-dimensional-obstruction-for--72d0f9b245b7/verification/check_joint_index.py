#!/usr/bin/env python3
"""Finite checks of Fourier--Walsh constructions for joint numerical indices.

Only checks finitely many dimensions/parameters. General statements require
and receive an analytic proof in RESULT.md. Uses Python's standard library.
"""
import cmath
import itertools
import math
import random


def hadamard(order):
    h = [[1]]
    while len(h) < order:
        h = [row + row for row in h] + [row + [-x for x in row] for row in h]
    assert len(h) == order
    return h


def inner(a,b):
    return sum(x*y for x,y in zip(a,b))


checks = 0
for m in (1,2,4,8,16):
    H=hadamard(m)
    for i in range(m):
        for j in range(m):
            assert sum(H[r][i]*H[r][j] for r in range(m)) == (m if i==j else 0)
            checks += 1
    for k in range(1,m+1):
        V = [[H[r][i]/m for i in range(k)] for r in range(m)]
        assert all(sum(abs(V[r][i]) for r in range(m))==1 for i in range(k))
        if m<=8:
            signs=itertools.product((-1,1),repeat=m)
            for sign in signs:
                outputs=[sum(sign[r]*V[r][i] for r in range(m)) for i in range(k)]
                for p in (2,3,5):
                    norm=sum(abs(t)**p for t in outputs)**(1/p)
                    assert norm<=1+1e-10,(m,k,p,norm)
                    checks += 1
        for j in range(k):
            f=[H[r][j] for r in range(m)]
            outputs=[sum(f[r]*V[r][i] for r in range(m)) for i in range(k)]
            assert all(abs(out - (1 if i==j else 0))<1e-10 for i,out in enumerate(outputs))
            checks += 1

# All complex Fourier orders, not only power-of-two, obey flatness and Parseval.
for m in (2,3,5,6,7,9):
    F=[[cmath.exp(2j*math.pi*r*i/m) for i in range(m)] for r in range(m)]
    for i in range(m):
        for j in range(m):
            val=sum(F[r][i].conjugate()*F[r][j] for r in range(m))
            assert abs(val-(m if i==j else 0))<1e-10
            checks += 1
    for k in range(1,m+1):
        for j in range(k):
            f=[F[r][j].conjugate() for r in range(m)]
            outputs=[sum(f[r]*F[r][i]/m for r in range(m)) for i in range(k)]
            assert all(abs(t-(1 if i==j else 0))<1e-10 for i,t in enumerate(outputs))
            checks += 1
        rng=random.Random(1837+m*29+k)
        for _ in range(120):
            f=[cmath.exp(2j*math.pi*rng.random()) for _ in range(m)]
            vals=[sum(f[r]*F[r][i]/m for r in range(m)) for i in range(k)]
            for p in (2,3,4):
                assert sum(abs(v)**p for v in vals)**(1/p) <= 1+1e-10
                checks += 1

# A real signed matrix of odd order three cannot be orthogonal.
for flat in itertools.product((-1,1),repeat=9):
    rows=[flat[3*r:3*r+3] for r in range(3)]
    assert any(inner(rows[i],rows[j])!=0 for i in range(3) for j in range(i+1,3))
    checks+=1

# Arbitrary integer operator tuples: the norm-index elementary lower bound.
rng=random.Random(19283)
for m in (2,3,4):
    for k in (1,2,3,4):
        for _ in range(50):
            T=[[[rng.randrange(-2,3) for j in range(m)] for i in range(m)] for _ in range(k)]
            joint_operator=max(sum(sum(abs(T[h][r][j]) for r in range(m))**2 for h in range(k))**.5 for j in range(m))
            joint_numeric=max(sum(sum(s[r]*T[h][r][j] for r in range(m))**2 for h in range(k))**.5
                for j in range(m) for s in itertools.product((-1,1),repeat=m))
            assert joint_numeric+1e-10>=joint_operator/(k**.5)
            checks+=1

print(f'VERIFY_OK checks={checks} real_orders=1,2,4,8,16 complex_orders=2,3,5,6,7,9 odd_hadamard_order3=excluded analytical_proof_required=True')
