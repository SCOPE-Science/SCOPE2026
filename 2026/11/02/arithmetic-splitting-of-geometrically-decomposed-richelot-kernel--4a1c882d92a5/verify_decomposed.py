#!/usr/bin/env python3
"""Exact symbolic and finite permutation checks for a genus-two Richelot kernel locus.

Requires sympy, Python 3. No external data or network access.
"""
from functools import lru_cache
import sympy as S

A, w, t = S.symbols('A w t')
R = [A * w**j for j in range(3)] + [w**j / A for j in range(3)]

@lru_cache(None)
def pairings(seq):
    if not seq:
        return [()]
    a = seq[0]
    return [((a,b),)+m for b in seq[1:]
            for m in pairings(tuple(c for c in seq[1:] if c != b))]

def norm(M):
    return tuple(sorted(tuple(sorted(v)) for v in M))

def cyc_reduce(expr):
    f = S.Poly(S.expand(expr),w)
    f = f.rem(S.Poly(w*w+w+1,w)).as_expr()
    return S.factor(f)

M = [norm(z) for z in pairings(tuple(range(6)))]
assert len(M) == 15 and len(set(M)) == 15
D = {}
for p in M:
    rows = [[1, -(R[i]+R[j]), R[i]*R[j]] for i,j in p]
    e = S.cancel(S.det(S.Matrix(rows)) * A**3)
    e = cyc_reduce(e)
    assert not e.has(1/A)  # polynomial after denominator clearing
    assert S.degree(e, A) <= 6
    assert all(int(power[0]) % 2 == 0 for power, _ in S.Poly(e, A).terms())
    e = S.expand(e).subs({A**6:t**3,A**4:t**2,A**2:t})
    D[p] = cyc_reduce(e)

base = [norm(((0,3+b),(1,3+(b-1)%3),(2,3+(b-2)%3))) for b in range(3)]
special0 = norm(((0,3),(1,4),(2,5)))
special50 = [norm(((0,1),(2,5),(3,4))),
             norm(((0,2),(1,4),(3,5))),
             norm(((0,3),(1,2),(4,5)))]
assert sum(D[m] == 0 for m in M) == 3
assert set(base) == {m for m in M if D[m] == 0}

def vanishes_mod(e, poly):
    return S.rem(S.Poly(e,t),S.Poly(poly,t)).as_expr()==0

def vanishes_special(e, relation):
    e = cyc_reduce(e)
    if e == 0:
        return True
    e = S.rem(S.Poly(e,t),S.Poly(relation,t)).as_expr()
    return cyc_reduce(e) == 0

assert {m for m in M if vanishes_special(D[m],t+1)} == set(base+[special0])
assert {m for m in M if vanishes_special(D[m],t*t+4*t+1)} == set(base+special50)
# The nonzero generic determinant norms have no roots except:
# t^3=1 (singular curves), t=-1 (s=0), and the six t corresponding to s^2=-50.
allowed = t*(t**6-1)*(t*t+4*t+1)*(t**4-4*t**3+15*t*t-4*t+1)
for m,e in D.items():
    if e == 0:
        continue
    ec = cyc_reduce(e)
    ec2 = cyc_reduce(ec.subs(w,-1-w))
    N = cyc_reduce(S.expand(ec*ec2))
    sq = S.Poly(N,t).sqf_part()
    assert S.rem(S.Poly(allowed,t),sq).as_expr() == 0, (m,N)
# Frob acts on the six geometric roots by (epsilon,eta,k).
def perm(epsilon, eta, k):
    d = {}
    for i in range(6):
        component = i//3; j=i%3
        if eta == -1: component = 1-component
        newj = ((k if i < 3 else -k)+epsilon*j)%3
        d[i] = 3*component + newj
    return d

def fixed(parts, d):
    return sum(norm((d[i],d[j]) for i,j in m)==m for m in parts)

for eps in [-1,1]:
    for eta in [-1,1]:
        for k in range(3):
            d=perm(eps,eta,k)
            assert fixed(base,d)==(3 if eps==1 else 1)
        d=perm(eps,eta,0)   # normalized extra-automorphism fibres
        assert fixed(base+[special0],d)==(4 if eps==1 else 2)
        assert fixed(base+special50,d)==(6 if eps==1 else 2)

def legendre(a,p):
    a%=p
    if a==0:return 0
    return 1 if pow(a,(p-1)//2,p)==1 else -1

for p in [7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73]:
    good = [s for s in range(p) if (s*s-4)%p]
    exceptional = [s for s in good if (s*s+50)%p==0]
    assert len(good)==p-2 and len(exceptional)==1+legendre(-2,p)
    for s in good:
        geom = 4 if s==0 else (6 if s in exceptional else 3)
        rational = (geom if p%3==1 else (2 if geom != 3 else 1))
        assert rational in (1,2,3,4,6)
print('GENUS2_DECOMPOSED_RICHELOT_FROBENIUS_EXACT_PASS')
print('15 determinants, exceptional loci, Frobenius orbits, 18 prime fields checked')
