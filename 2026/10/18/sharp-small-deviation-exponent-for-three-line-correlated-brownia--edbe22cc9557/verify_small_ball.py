"""Checks for the three-line Brownian last-passage small-deviation theorem.

Requires sympy and mpmath. The infinite-probability statement is proved in
RESULT.md; these finite checks test its formulas, event inclusions, and the
leading term of the planar wedge Dirichlet heat kernel.
"""
from __future__ import annotations
import math
import random
import sympy as sp
import mpmath as mp

mp.mp.dps = 70
P = sp.Matrix([[1, 1, 4], [1, 4, 1], [4, 1, 1]])/6
J = sp.ones(3, 3)/3
A = P-J
Sigma = (sp.eye(3)-J + A*(sp.eye(3)-A).inv()
         + A.T*(sp.eye(3)-A.T).inv())/3
D = sp.Matrix([[1, -1, 0], [0, 1, -1]])
C = D*Sigma*D.T
assert C == sp.Matrix([[14, -13], [-13, 14]])/9
assert Sigma*sp.ones(3, 1) == sp.zeros(3, 1)
assert all(x > 0 for x in C.eigenvals())
assert math.isclose(float(C[0, 1]/sp.sqrt(C[0, 0]*C[1, 1])), -13/14)


def functional(x, y):
    """Grid version with Brownian differences x,y; both start at zero."""
    assert len(x) == len(y) and abs(x[0])+abs(y[0]) < 1e-14
    b3 = -(x[-1]+2*y[-1])/3
    best = -float('inf')
    mx1 = -float('inf')
    for v, w in zip(x, y):
        mx1 = max(mx1, v)
        best = max(best, mx1+w)
    return b3+best

rng = random.Random(20261009)
num_grid_checks = 0
for _ in range(100):
    x, y = [0.0], [0.0]
    for _ in range(40):
        x.append(x[-1]+rng.gauss(0, 0.06))
        y.append(y[-1]+rng.gauss(0, 0.06))
    F = functional(x, y)
    assert F >= -1e-12
    eps = F+0.0001
    assert max(x) <= 3*eps+1e-12
    assert max(y) <= 3*eps+1e-12
    assert x[-1] >= -3*eps-1e-12 and y[-1] >= -3*eps-1e-12
    num_grid_checks += 4
for _ in range(100):
    delta = 0.01+rng.random()
    x = [delta*(0.25*math.sin(2*math.pi*j/120)+0.1*j/120) for j in range(121)]
    y = [delta*(0.20*math.sin(4*math.pi*j/120)+0.15*j/120) for j in range(121)]
    assert max(x)<=delta and max(y)<=delta
    assert 0<=x[-1]<=delta/2 and 0<=y[-1]<=delta/2
    assert functional(x,y) <=2*delta+1e-12
    num_grid_checks += 3


def coords(v, rho):
    rho = mp.mpf(rho)
    u = 1/mp.sqrt(1+rho)
    w = 1/mp.sqrt(1-rho)
    a,b = (u+w)/2, (u-w)/2
    return (a*v[0]+b*v[1], b*v[0]+a*v[1])


def dot(a, b): return a[0]*b[0]+a[1]*b[1]
def det(a, b): return a[0]*b[1]-a[1]*b[0]
def length(a): return mp.sqrt(dot(a,a))


def kernel(rho, d):
    rho, d = mp.mpf(rho), mp.mpf(d)
    theta = mp.acos(-rho)
    beta = mp.pi/theta
    ray = coords((1,0),rho)
    a = coords((1,1),rho)
    b = coords((mp.mpf('0.75'),mp.mpf('0.60')),rho)
    def angle(z): return mp.atan2(det(ray,z),dot(ray,z))
    pa,pb=angle(a),angle(b)
    assert pa>0 and pb>0 and pa<theta and pb<theta
    ra,rb=length(a),length(b)
    z=d*d*ra*rb
    series=mp.fsum(mp.sin(k*beta*pa)*mp.sin(k*beta*pb)*mp.besseli(k*beta,z)
                   for k in range(1,10))
    actual=2/theta*mp.exp(-d*d*(ra*ra+rb*rb)/2)*series
    leading=(2**(1-beta)/(theta*mp.gamma(beta+1))
             *(ra*rb)**beta*mp.sin(beta*pa)*mp.sin(beta*pb))
    assert actual>0 and leading>0
    return actual/(d**(2*beta)*leading),beta

num_kernel_checks=0
for rho in (mp.mpf('-13')/14,mp.mpf('-0.8'),mp.mpf('-0.5'),mp.mpf('0'),mp.mpf('0.5')):
    r1,beta=kernel(rho,mp.mpf('0.04'))
    r2,_=kernel(rho,mp.mpf('0.02'))
    assert abs(r2-1)<abs(r1-1) and abs(r2-1)<mp.mpf('0.01')
    assert abs(beta-mp.pi/mp.acos(-rho))<mp.mpf('1e-55')
    num_kernel_checks+=3

kappa=2+2*mp.pi/mp.acos(mp.mpf(13)/14)
assert mp.mpf('18.52')<kappa<mp.mpf('18.53')
assert abs((2+2*mp.pi/mp.acos(mp.mpf('0.5')))-8)<mp.mpf('1e-55')
print('PASS exact example covariance; positive rank-two covariance')
print('PASS',num_grid_checks,'finite path-inclusion checks')
print('PASS',num_kernel_checks,'high-precision wedge heat-kernel checks')
print('Example exponent for rho=-13/14:', mp.nstr(kappa,20))
print('Note: finite checks do not replace the proof for all paths or epsilon.')
