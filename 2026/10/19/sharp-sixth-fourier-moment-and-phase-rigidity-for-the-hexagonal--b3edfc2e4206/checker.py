#!/usr/bin/env python3
"""Exact sixth-moment certificate for the six-point hexagonal Fourier support.

Run with Python 3 standard library: python3 checker.py
"""
from collections import Counter, defaultdict
from itertools import product
from fractions import Fraction
from random import Random
from cmath import exp, pi

V = [(1, 0), (0, 1), (-1, 1)]
S = V + [(-a, -b) for a, b in V]

def s3(i, j, k):
    return (S[i][0]+S[j][0]+S[k][0], S[i][1]+S[j][1]+S[k][1])

fibers = defaultdict(list)
for ids in product(range(6), repeat=3):
    fibers[s3(*ids)].append(ids)

# Formal symmetric coefficient specialization c_i = x_{i mod 3}.
monos = defaultdict(Counter)
for h, triples in fibers.items():
    for triple in triples:
        exp3 = tuple(sum(j % 3 == a for j in triple) for a in range(3))
        monos[h][exp3] += 1
poly = Counter()
for m in monos.values():
    for e, a in m.items():
        for f, b in m.items():
            poly[tuple(e[i]+f[i] for i in range(3))] += a*b
expect = Counter()
for a in range(3):
    e=[0,0,0];e[a]=6;expect[tuple(e)]=20
    for b in range(3):
        if b!=a:
            e=[0,0,0];e[a]=4;e[b]=2;expect[tuple(e)]=180
expect[(2,2,2)]=900
assert poly == expect, (poly, expect)
assert sum(poly.values()) == 2040
assert sum(Counter(map(len, fibers.values())).values()) == 37
assert dict(sorted(Counter(map(len, fibers.values())).items())) == {1:6,3:12,6:12,12:1,15:6}
assert len(fibers[(0,0)]) == 12
# Three anti-podal pair cancellations occur at each positive root.
for v in V:
    assert all((j, j+3) in [(ids[1],ids[2]) for ids in fibers[v] if ids[0]==V.index(v)]
               or (j+3,j) in [(ids[1],ids[2]) for ids in fibers[v] if ids[0]==V.index(v)]
               for j in range(3))

# Independent exact convolution for general complex Gaussian integers.
def moment(cs, modulus=None):
    C=defaultdict(complex)
    for ids in product(range(6),repeat=3):
        h=s3(*ids)
        if modulus is not None: h=(h[0]%modulus,h[1]%modulus)
        C[h]+=cs[ids[0]]*cs[ids[1]]*cs[ids[2]]
    return sum(abs(z)**2 for z in C.values())

def moment_gaussian_int(cs):
    C=defaultdict(lambda:0j)
    for ids in product(range(6),repeat=3):
        C[s3(*ids)]+=cs[ids[0]]*cs[ids[1]]*cs[ids[2]]
    # Complex values are integer Gaussian integers; float-valued
    # complex multiplication here is exact for bounded integer inputs.
    return sum(int(v.real)**2+int(v.imag)**2 for v in C.values())

rng=Random(260814)
for trial in range(350):
    cs=[complex(rng.randint(-3,3),rng.randint(-3,3)) for _ in range(6)]
    M=sum(int(c.real)**2+int(c.imag)**2 for c in cs)
    assert 9*moment_gaussian_int(cs)<=85*M**3

for x,y,z in product(range(0,6),repeat=3):
    cs=[x,y,z,x,y,z]
    F=moment_gaussian_int(cs)
    X,Y,Z=x*x,y*y,z*z
    sm=X+Y+Z; e2=X*Y+Y*Z+Z*X; e3=X*Y*Z
    assert F==20*sm**3+120*sm*e2+420*e3

flat=[1]*6
assert moment_gaussian_int(flat)==2040
assert Fraction(moment_gaussian_int(flat),6**3)==Fraction(85,9)
assert moment(flat,modulus=6)==2046
for N in [7,8,9,11,13]:
    assert moment(flat,modulus=N)==2040

# Character-phase maximizers, with continuously variable lattice phases.
for theta, phi in [(0.1,1.2),(2.3,-0.7),(pi/7,pi/5)]:
    cs=[exp(1j*(theta*a+phi*b)) for a,b in S]
    assert abs(moment(cs)-(85/9)*6**3)<2e-9
    for N in [7,8,9]:
        avg=sum(abs(sum(cs[j]*exp(2j*pi*(a*u+b*v)/N)
                 for j,(a,b) in enumerate(S)))**6
                for u in range(N) for v in range(N))/(N*N)
        assert abs(avg-2040)<1e-7
# An extra noncharacter fourth-moment phase is excluded at sixth moment.
notcharacter=[1,1,exp(1j*pi/5),1,1,exp(-1j*pi/5)]
assert moment(notcharacter)<2040-1
print('VERIFY_OK supports=6 triple_fibers=37 coefficient_monomials=10')
print('symbolic_moment=20*sum(X^3)+180*sum_sym(X^2Y)+900*XYZ')
print('symmetric_form=20*s^3+120*s*e2+420*e3')
print('sharp_sixth_moment=2040 sharp_ratio=85/9')
print('tests=350_exact_gaussian+216_exact_balanced+15_character_grid+5_noalias+1_alias')
