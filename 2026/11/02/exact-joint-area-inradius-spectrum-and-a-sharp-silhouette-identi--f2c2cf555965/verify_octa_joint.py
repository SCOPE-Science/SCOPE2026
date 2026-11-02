"""Reproducibility checks for joint area/inradius spectrum of octahedron shadows.

Requires Python 3, numpy and scipy. These are finite diagnostics, not a
replacement for the analytic classification of all viewing directions.
"""
import math
import numpy as np
from scipy.spatial import ConvexHull

rng = np.random.default_rng(20261031)
V = np.vstack((np.eye(3), -np.eye(3)))
q_star = math.sqrt(math.sqrt(2.0) - 1.0)
r_star = 1.0 / math.sqrt(1.0 + math.sqrt(2.0))
assert abs(q_star-r_star) < 1e-14

def bounds(q):
    h_lower = (3.0-q) / math.sqrt(q*q - 2.0*q + 3.0)
    h_upper = math.sqrt(2.0 * (q*q + 3.0) / (q*q + 2.0))
    q_lower = 2.0 / math.sqrt(1.0 + q*q)
    q_upper = 2.0 / math.sqrt(1.0 + 0.5*q*q)
    return h_lower, h_upper, q_lower, q_upper

def formula(u):
    a,b,c = np.sort(np.abs(u))
    if c > a+b:
        q = (a+b)/c
        area = 2.0*c
        shape = 4
    else:
        q = (c-a)/b
        area = a+b+c
        shape = 6
    return area, 1.0/math.sqrt(2+q*q), shape

def direct_geometry(u):
    basis = np.eye(3)[int(np.argmin(np.abs(u)))]
    x = np.cross(u,basis); x /= np.linalg.norm(x)
    y = np.cross(u,x)
    projection = np.column_stack([V@x,V@y])
    hull = ConvexHull(projection)
    area = hull.volume
    radius = min(abs(e[-1])/np.linalg.norm(e[:2]) for e in hull.equations)
    return area,radius,len(hull.vertices)

for _ in range(2500):
    u = rng.normal(size=3);u/=np.linalg.norm(u)
    A,r,n = formula(u)
    aa,rr,nn = direct_geometry(u)
    assert abs(A-aa)<2e-12,(A,aa,u)
    assert abs(r-rr)<2e-12,(r,rr,u)
    assert n==nn,(n,nn,u)

for q in np.linspace(0.0001,0.9999,61):
    HL,HU,QL,QU=bounds(q)
    assert HL<=HU+1e-12 and QL<=QU+1e-12
    assert HL<QL and HU<QU
    if q<q_star-1e-4:assert HU<QL
    elif q>q_star+1e-4:assert HU>QL
    # Exact parameterization of all ordered positive normals; compare bands.
    for t in np.linspace(1.0-q,1.0,101):
        v=np.array([t,1,t+q],dtype=float);v/=np.linalg.norm(v)
        A,r,n=formula(v)
        assert abs(r-1/math.sqrt(2+q*q))<2e-13
        assert HL-2e-12<=A<=HU+2e-12, (q,t,A,HL,HU)
    for z in np.linspace(0,1,101):
        v=np.array([q*(1-z)/2,q*(1+z)/2,1],dtype=float)
        v/=np.linalg.norm(v)
        A,r,n=formula(v)
        assert abs(r-1/math.sqrt(2+q*q))<2e-13
        assert QL-2e-12<=A<=QU+2e-12,(q,z,A,QL,QU)
    # The analytic hex upper maximizer lies in the allowed parameter range.
    tstar=1+(q*q-q)/2
    assert 1-q-1e-12 <= tstar <= 1+1e-12
    u=np.array([tstar,1,tstar+q]);u/=np.linalg.norm(u)
    assert abs(formula(u)[0]-HU)<2e-12

for q in [0.0,0.2,0.5,q_star,0.8,1.0]:
    HL,HU,QL,QU=bounds(q)
    delta=QL-HU
    if q==q_star: assert abs(delta)<1e-13
    print('q',round(q,10),'r',round(1/math.sqrt(2+q*q),10),
          'hex',tuple(round(v,10) for v in (HL,HU)),
          'quad',tuple(round(v,10) for v in (QL,QU)),
          'gap',round(delta,10))

# The exact contact point where the two area bands touch.
HL,HU,QL,QU=bounds(q_star)
assert abs(HU-2**0.75)<1e-12
assert abs(QL-2**0.75)<1e-12

# Independent random sampling reproduces absence of area in forbidden bands.
normal = rng.normal(size=(200000,3))
normal/=np.linalg.norm(normal,axis=1)[:,None]
abc=np.sort(np.abs(normal),axis=1)
a,b,c=abc.T
quad=c>a+b
q=np.where(quad,(a+b)/c,(c-a)/b)
area=np.where(quad,2*c,a+b+c)
HL=(3-q)/np.sqrt(q*q-2*q+3)
HU=np.sqrt(2*(q*q+3)/(q*q+2))
QL=2/np.sqrt(1+q*q)
QU=2/np.sqrt(1+q*q/2)
assert np.all(np.where(quad,(area>=QL-1e-13)&(area<=QU+1e-13),
                               (area>=HL-1e-13)&(area<=HU+1e-13)))
assert np.all(np.where(q<q_star,(area<=HU+1e-13)|(area>=QL-1e-13),True))
print('OCTAHEDRON_JOINT_AREA_INRADIUS_CHECKS_PASSED')
