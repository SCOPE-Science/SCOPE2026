"""Independent checks of the exact expected-area identity for edge-split polygons.

No numerical experiment is used as a proof of the infinite-step identity.
"""
from fractions import Fraction as F
from itertools import product
import math
import random


def signed_area(vertices):
    return sum((a[0]*b[1]-a[1]*b[0]) for a,b in zip(vertices, vertices[1:]+vertices[:1]))/2


def split(vertices, proportions):
    return [((1-p)*a[0]+p*b[0],(1-p)*a[1]+p*b[1])
            for a,b,p in zip(vertices,vertices[1:]+vertices[:1],proportions)]


def det_area(vertices,means):
    for mean in means:
        vertices=split(vertices,[mean]*len(vertices))
    return signed_area(vertices)


def four_cycle_pairwise_independent():
    # Fair bits A,B,A xor B,C; pairwise independent but not jointly independent.
    return [(F(a,4)*2+F(1,4),F(b,4)*2+F(1,4),
             F(a^b,4)*2+F(1,4),F(c,4)*2+F(1,4))
            for a,b,c in product((0,1),repeat=3)]


P=[(F(0),F(0)),(F(4),F(0)),(F(4),F(3)),(F(0),F(3))]
states=four_cycle_pairwise_independent()
assert len(states)==8
for i in range(4):
    assert sum(q[i] for q in states)/8==F(1,2)
    for j in range(i):
        assert sum(q[i]*q[j] for q in states)/8==F(1,4)

expected=F(0)
for a,b,c in product(range(8),repeat=3):
    p=split(split(split(P,states[a]),states[b]),states[c])
    expected+=signed_area(p)/F(8**3)
exact_target=det_area(P,[F(1,2)]*3)
assert expected==exact_target
assert exact_target==F(3,2)  # square area 12 and retention (1/2)^3
print('PAIRWISE_UNCORRELATED_BUT_NOT_JOINTLY_INDEPENDENT_EXACT_512_PATHS_OK')

# Cumulative expected area for a nonregular convex pentagon,
# allowing a different mean at every time and different split marginals.
import numpy as np
rng=np.random.default_rng(917)
raw=[(0,0),(3,-1),(6,2),(4,6),(0,5)]
V=np.array(raw,dtype=float)
assert float(signed_area([(F(x),F(y)) for x,y in raw]))>0
means=[.29,.71,.43,.6]
N=120000
Vrand=np.broadcast_to(V,(N,5,2)).copy()
for time,mu in enumerate(means):
    if time%2:
        # One endpoint-biased distribution, same expectation mu.
        R=(rng.random((N,5))<mu).astype(float)
    else:
        # Uniform-on-an-interval split with the same expectation mu.
        d=min(mu,1-mu)
        R=mu+d*(2*rng.random((N,5))-1)
    Vrand=(1-R[:,:,None])*Vrand+R[:,:,None]*np.roll(Vrand,-1,axis=1)
areas=np.sum(Vrand[:,:,0]*np.roll(Vrand[:,:,1],-1,axis=1)
             -Vrand[:,:,1]*np.roll(Vrand[:,:,0],-1,axis=1),axis=1)/2
want=float(det_area([tuple(x) for x in V],means))
se=float(areas.std(ddof=1)/np.sqrt(N))
assert abs(float(areas.mean())-want)<6*se
print('IRREGULAR_PENTAGON_HETEROGENEOUS_FOUR_STEP_MONTE_CARLO_OK',N)

for n in range(3,15):
    z=np.exp(2j*np.pi*np.arange(n)/n)
    zdet=z.copy()
    for mu in means:
        zdet=(1-mu)*zdet+mu*np.roll(zdet,-1)
    area_det=np.imag(np.vdot(zdet,np.roll(zdet,-1)))/2
    lamb=np.prod([1-4*mu*(1-mu)*np.sin(np.pi/n)**2 for mu in means])
    target=n*np.sin(2*np.pi/n)*lamb/2
    assert abs(area_det-target)<2.e-13
print('REGULAR_POLYGON_ALL_ORDERS_3_THROUGH_14_SPECTRAL_LAW_OK')

# Correlated split bits: all vertices choose exactly the same endpoint.
# The polygon merely rotates its labeling; the noise-blind law must fail.
for n in range(3,10):
    z=np.exp(2j*np.pi*np.arange(n)/n)
    a0=np.imag(np.vdot(z,np.roll(z,-1)))/2
    assert abs(a0-n*np.sin(2*np.pi/n)/2)<1e-12
    assert abs(a0*(1-np.sin(np.pi/n)**2)-a0)>1e-6
print('CROSS_EDGE_DECORRELATION_NECESSITY_COUNTEREXAMPLE_OK')

# Direct Fourier reconstruction for nonregular polygons.
for n in range(3,14):
    angles=np.sort(rng.uniform(0,2*np.pi,size=n))
    z=np.exp(1j*angles)
    mu=[.3,.7,.42]
    zz=z.copy()
    for x in mu: zz=(1-x)*zz+x*np.roll(zz,-1)
    direct=np.imag(np.vdot(zz,np.roll(zz,-1)))/2
    modes=np.fft.fft(z)/n
    ks=np.arange(n)
    lam=np.prod([1-4*x*(1-x)*np.sin(np.pi*ks/n)**2 for x in mu],axis=0)
    spec=n/2*np.sum(np.abs(modes)**2*np.sin(2*np.pi*ks/n)*lam)
    assert abs(direct-spec)<2e-13
print('GENERAL_POLYGON_FOURIER_IDENTITY_ORDERS_3_THROUGH_13_OK')
print('ALL_EXPECTED_AREA_CHECKS_OK')
