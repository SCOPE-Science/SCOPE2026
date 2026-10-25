"""Independent geometric checks for the extremal central cube-section area law.

Run: python3 verify_cube_section_tail.py
Requires numpy and scipy. The exact limiting law is proved in RESULT.md;
this verifier independently reconstructs section polygons and performs
finite-threshold integrations. It does not prove a limiting assertion.
"""
import itertools
from math import sqrt, pi
import numpy as np
from scipy.optimize import brentq
from scipy.integrate import quad
from scipy.spatial import ConvexHull

VERTICES=np.array(list(itertools.product((-1.,1.),repeat=3)))
EDGES=[(i,j) for i in range(8) for j in range(i+1,8)
       if np.count_nonzero(VERTICES[i]!=VERTICES[j])==1]

def independent_section(u):
    u=np.asarray(u,dtype=float)
    u/=np.linalg.norm(u)
    values=VERTICES@u
    points=[]
    for i,j in EDGES:
        a,b=values[i],values[j]
        if a*b<0:
            t=a/(a-b)
            points.append(VERTICES[i]+t*(VERTICES[j]-VERTICES[i]))
    points=np.asarray(points)
    assert len(points) in (4,6)
    w=np.eye(3)[int(np.argmin(np.abs(u)))]
    e1=np.cross(u,w)
    e1/=np.linalg.norm(e1)
    e2=np.cross(u,e1)
    hull=ConvexHull(np.column_stack((points@e1,points@e2)))
    return hull.volume,len(hull.vertices)

def analytic_section(u):
    a,b,c=sorted(np.abs(u)/np.linalg.norm(u),reverse=True)
    if a>=b+c:
        return 4/a,4
    return (4*b*c-(b+c-a)**2)/(a*b*c),6

rng=np.random.default_rng(20261019)
for group in range(3):
    for k in range(180):
        if group==0:
            u=rng.normal(size=3)
        else:
            s=rng.uniform(0.0001,0.09)
            t=rng.uniform(0.0001,0.09)
            if group==1:
                s=max(s,t)*1.2
            else:
                t=max(s,t)*1.2
            u=np.array([1.,1.-s,t])
            u*=rng.choice([-1,1],size=3)
            u=u[rng.permutation(3)]
        A,N=analytic_section(u)
        Ah,Nh=independent_section(u)
        assert N==Nh,(u,N,Nh)
        assert abs(A-Ah)<3e-11,(u,A,Ah)
print('INDEPENDENT_CUBE_EDGE_INTERSECTION_AREAS_AND_FACE_COUNTS_OK 540')

AMAX=4*sqrt(2)
def A_ratio(y,z):
    q=max(y+z-1.,0.)
    if q==0: return 4*sqrt(1+y*y+z*z)
    return 4*sqrt(1+y*y+z*z)*(1-q*q/(4*y*z))

def exact_tail_by_type(delta):
    target=AMAX-delta
    zmax=brentq(lambda z:A_ratio(1,z)-target,1e-15,0.12,xtol=1e-15)
    cross=brentq(lambda z:A_ratio(1-z,z)-target,1e-15,zmax,xtol=1e-15)
    def smax(z):
        if z>zmax*(1-1e-14): return 0.
        return brentq(lambda s:A_ratio(1-s,z)-target,0,0.2,xtol=2e-15)
    def mass(z,lo,hi):
        c=1+z*z
        F=lambda x:x/(c*sqrt(x*x+c))
        return F(1-lo)-F(1-hi)
    q4=12/pi*quad(lambda z:mass(z,z,smax(z)),0,cross,
                 epsabs=1e-13,epsrel=1e-11)[0]
    q6=12/pi*(quad(lambda z:mass(z,0,z),0,cross,
                 epsabs=1e-13,epsrel=1e-11)[0]
                +quad(lambda z:mass(z,0,smax(z)),cross,zmax,
                 epsabs=1e-13,epsrel=1e-11)[0])
    return q4,q6

C4=3*sqrt(2)/(16*pi)
C6=3*sqrt(2)*(2+pi)/(32*pi)
assert abs(C4/(C4+C6)-2/(4+pi))<1e-14
for delta in (0.04,0.02,0.01,0.005,0.002):
    p4,p6=exact_tail_by_type(delta)
    print(f'delta={delta:.3f} p4/delta^2={p4/delta**2:.10f} '
          f'p6/delta^2={p6/delta**2:.10f}')
    assert abs(p4/delta**2/C4-1)<0.7*delta
    assert abs(p6/delta**2/C6-1)<1.4*delta
print('INDEPENDENT_EXACT_DIRECTIONAL_INTEGRATION_TAIL_COEFFICIENTS_OK')
print('FOUR_VS_SIX_SIDED_ASYMPTOTIC_SPLIT_OK')
print('ALL_CUBE_SECTION_TAIL_CHECKS_OK')
