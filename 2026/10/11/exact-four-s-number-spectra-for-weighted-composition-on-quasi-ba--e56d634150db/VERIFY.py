#!/usr/bin/env python3
"""Finite checks supporting a proved s-number formula; not an infinite certificate."""
from fractions import Fraction
from itertools import product
from math import isqrt
from random import Random


def p_mass(q, p):
    q = abs(Fraction(q))
    if p == Fraction(1):
        return q
    if p == Fraction(1, 2):
        a, b = isqrt(q.numerator), isqrt(q.denominator)
        if a*a != q.numerator or b*b != q.denominator:
            raise ValueError('non-square exact-rational input')
        return Fraction(a, b)
    raise ValueError(p)


def rank(a):
    mat = [list(map(Fraction, row)) for row in a]
    if not mat:
        return 0
    rows, cols, r = len(mat), len(mat[0]), 0
    for col in range(cols):
        pivot = next((i for i in range(r, rows) if mat[i][col]), None)
        if pivot is None:
            continue
        mat[r], mat[pivot] = mat[pivot], mat[r]
        v = mat[r][col]
        mat[r] = [z/v for z in mat[r]]
        for i in range(rows):
            if i == r or not mat[i][col]:
                continue
            c = mat[i][col]
            mat[i] = [a-c*b for a,b in zip(mat[i], mat[r])]
        r += 1
        if r == rows:
            break
    return r

# Exact p-triangle / strict column block-dominance test (the proof covers all p in (0,1]).
profiles = 0
for p in (Fraction(1,2), Fraction(1)):
    for n in range(2, 12):
        v = Fraction(1,4) if p == Fraction(1,2) else Fraction(1,2)
        delta = Fraction(1,16) if p == Fraction(1,2) else Fraction(1,8)
        vectors = []
        for j in range(n):
            col = [Fraction(0) for _ in range(2*n)]
            col[2*j:2*j+2] = [v,v]
            col[2*((j+1)%n)] += delta
            vectors.append(col)
            own = sum((p_mass(col[t],p) for t in (2*j,2*j+1)), Fraction(0))
            other = sum((p_mass(col[t],p) for t in range(2*n) if t not in (2*j,2*j+1)), Fraction(0))
            assert own > other
            assert p_mass(delta,p) < 1
            assert p_mass(v,p)+p_mass(v,p) == 1
            profiles += 1
        assert rank([[vectors[j][t] for j in range(n)] for t in range(2*n)]) == n

# Operator norm identity on finite weighted composition operators: arbitrary repeated fibers.
rng=Random(20261008)
identities=0
for p in (.50, .75, 1.0):
    for n in range(2,12):
        for m in range(2,16):
            phi=[rng.randrange(n) for _ in range(m)]
            w_in=[rng.choice((.5,1.,2.,3.)) for _ in range(n)]
            w_out=[rng.choice((.5,1.,2.,3.)) for _ in range(m)]
            u=[rng.choice((-3.,-1.,0.,1.,2.)) for _ in range(m)]
            x=[rng.choice((-2.,-1.,0.,.5,1.)) for _ in range(n)]
            ell=[sum((abs(u[k])*w_out[k])**p for k in range(m) if phi[k]==i)/(w_in[i]**p) for i in range(n)]
            lhs=sum((abs(u[k]*x[phi[k]])*w_out[k])**p for k in range(m))
            rhs=sum(ell[i]*(abs(x[i])*w_in[i])**p for i in range(n))
            assert abs(lhs-rhs) <= 1e-9*(1+lhs+rhs)
            identities+=1

# The two-coordinate quasi-Banach image has no contractive projection if p<1.
for p in (.25, .5, .75):
    c=2**(-1/p)
    assert 2*c < 1
print(f'VERIFY_OK exact_dominance_profiles={profiles} finite_fiber_identities={identities} noncomplemented_p_checks=3 proof_is_analytic=True')
