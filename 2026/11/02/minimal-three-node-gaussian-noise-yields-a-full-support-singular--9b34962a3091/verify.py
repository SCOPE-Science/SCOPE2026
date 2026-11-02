"""Exact arithmetic checks for the three-node OU innovation example.

Only Python's standard library is required. Universal measure-theoretic
statements have separate proofs and are not certified by these finite checks.
"""
from fractions import Fraction as F
from math import comb, log

r = F(1, 3)
v = F(9, 8)
c2 = v * (1-r*r)  # one for this normalization
assert c2 == 1


def moments_gaussian(j):
    if j % 2:
        return F(0)
    out = F(1)
    for q in range(1, j, 2):
        out *= q
    return out


def moments_three(j):
    if j % 2:
        return F(0)
    return F(1,3) * 3**(j//2) if j else F(1)

for j in range(6):
    assert moments_three(j) == moments_gaussian(j), j
assert moments_three(6) == 9
assert moments_gaussian(6) == 15


def stationary_moments(mom):
    m = [F(1)]
    for j in range(1, 7):
        acc = F(0)
        for ell in range(j):
            innovation_degree = j-ell
            if innovation_degree%2:
                continue
            acc += F(comb(j,ell))*r**ell*c2**(innovation_degree//2)*m[ell]*mom(innovation_degree)
        m.append(acc/(1-r**j))
    return m

x = stationary_moments(moments_three)
g = stationary_moments(moments_gaussian)
assert x[:6] == g[:6] == [F(1),F(0),v,F(0),3*v*v,F(0)]
assert g[6] == 15*v**3
assert x[6] == F(981,91)*v**3
assert g[6]-x[6] == F(384,91)*v**3

# Exact matching of stationary joint moments at one lag up to total degree five.
for p in range(6):
    for q in range(6-p):
        def joint(m, noise):
            out=F(0)
            for ell in range(q+1):
                d = q-ell
                if d%2: continue
                out+=F(comb(q,ell))*r**ell*c2**(d//2)*m[p+ell]*noise(d)
            return out
        assert joint(x, moments_three) == joint(g, moments_gaussian), (p,q)

# An explicit finite-time n=1..12 test with deterministic X0=2, all moments up to degree 5.
ref=[]
for noise in (moments_three, moments_gaussian):
    m=[F(2)**i for i in range(6)]
    for n in range(1,13):
        m=[sum(F(comb(j,ell))*r**ell*c2**((j-ell)//2)*m[ell]*noise(j-ell)
                  for ell in range(j+1) if (j-ell)%2==0)
           for j in range(6)]
        if noise is moments_three:
            ref.append(m)
        else:
            assert m==ref[n-1], n

# Full support threshold: adjacent first-level images touch precisely for r=1/3.
for z in (F(1,4),F(1,3),F(2,5)):
    radius=1/(1-z)
    half_image=z*radius
    assert (2*half_image >= 1)==(z>=F(1,3))

p=[F(1,6), F(2,3), F(1,6)]
H=-sum(float(t)*log(float(t)) for t in p)
d=H/log(3)
assert 0.78 < d < 0.80
print('VERIFY_OK: innovation moments 0..6, stationary moments 0..6, 21 lagged mixed moments, 12 finite-time steps, support threshold, entropy dimension')
print('sixth_moment_deficit_as_multiple_of_v_cubed',F(384,91))
print('dimension',format(d,'.12f'))
