#!/usr/bin/env python3
"""Reproduce the 30-site icosidodecahedral spherical contact distribution.

Requires Python >=3.9, numpy, scipy. No network or external data.
"""
import math
import itertools
import numpy as np
from scipy.spatial import ConvexHull
from scipy.integrate import quad

PHI=(1+math.sqrt(5.0))/2
A=1/PHI**2
B=1/PHI
RHO=math.pi/10
R1=math.atan(A)
R2=math.atan(B)
CENTER=math.atan(A/B)


def Qarea(r):
    """Area of one of four congruent spherical right triangles in a cell."""
    if r <= 0:
        return 0.0
    if r >= R2:
        return math.pi/30
    baseline=(math.pi/2)*(1-math.cos(r))
    if r <= RHO:
        return baseline
    delta=math.acos(min(1.,math.tan(RHO)/math.tan(r)))
    lo=max(0.,CENTER-delta)
    hi=min(math.pi/2,CENTER+delta)
    def H(theta):
        return math.asin(math.cos(RHO)*math.sin(theta-CENTER))
    return baseline + math.cos(r)*(hi-lo) - (H(hi)-H(lo))


def cdf(r):
    return min(1.,max(0.,30/math.pi*Qarea(r)))


def independent_angular_quad(r):
    """Direct numerical polar integration in a gnomonic cell quadrant."""
    if r <= 0:return 0.
    t=math.tan(min(R2,r))
    def integrand(theta):
        edge=1/(math.cos(theta)/A + math.sin(theta)/B)
        rr=min(t,edge)
        return 1-1/math.sqrt(1+rr*rr)
    return 30/math.pi*quad(integrand,0,math.pi/2,epsabs=2e-12,epsrel=2e-12,limit=1500,points=[CENTER])[0]


def site_vertices():
    phi=PHI
    points=[]
    for s,t in itertools.product((-1,1),repeat=2):
        points.extend(((0.,s,t*phi),(s,t*phi,0.),(s*phi,0.,t)))
    points=np.asarray(points,dtype=np.float64)
    points/=np.linalg.norm(points,axis=1)[:,None]
    edge_pairs=[(i,j) for i,j in itertools.combinations(range(12),2)
                if abs(float(np.dot(points[i],points[j])) -1/math.sqrt(5))<1e-11]
    assert len(edge_pairs)==30
    sites=np.array([(points[i]+points[j])/np.linalg.norm(points[i]+points[j])
                    for i,j in edge_pairs])
    assert len(sites)==30
    return points,sites


def test():
    roots,sites=site_vertices()
    assert max(abs(np.linalg.norm(sites,axis=1)-1))<1e-13
    # Independent combinatorial construction: 30 icosahedral edge midpoints,
    # with 20 triangular and 12 pentagonal polygon faces.
    hull=ConvexHull(sites)
    face_orbits={}
    for s,e in zip(hull.simplices,hull.equations):
        n=e[:3]/np.linalg.norm(e[:3]);
        key=tuple(np.rint(n*1e9).astype(int))
        face_orbits.setdefault(key,set()).update(map(int,s))
    counts=[len(v) for v in face_orbits.values()]
    assert sorted(counts)==[3]*20+[5]*12,(len(counts),counts)
    print('INDEPENDENT_THIRTY_SITES_TWENTY_TRIANGLES_TWELVE_PENTAGONS_OK')

    # Each spherical nearest-site cell has four corners: two face-center
    # directions from triangular faces, two from pentagonal faces.
    for q in sites:
        incident=[]
        for key,indices in face_orbits.items():
            if any(abs(np.dot(q,sites[i])-1)<1e-12 for i in indices):
                n=np.array(key,dtype=float); n/=np.linalg.norm(n)
                incident.append((len(indices),n))
        assert sorted(k for k,n in incident)==[3,3,5,5]
        tang=[]
        for k,n in incident:
            r=math.acos(np.clip(float(np.dot(q,n)),-1,1))
            assert abs(r-(R1 if k==3 else R2))<1e-9
            tang.append((k,(n-q*np.dot(q,n))/math.sin(r)))
        for k1,d1 in tang:
            for k2,d2 in tang:
                if k1!=k2:
                    assert abs(np.dot(d1,d2))<2e-8
    assert abs(math.tan(RHO)-1/math.hypot(1/A,1/B))<1e-13
    print('FOUR_ORTHOGONAL_FACE_DIRECTIONS_GOLDEN_GNOMONIC_RHOMBUS_OK')

    # Area of the full Voronoi cell = four right triangles = 4pi/30.
    def H(t):return math.asin(math.cos(RHO)*math.sin(t-CENTER))
    assert abs(math.pi/2-H(math.pi/2)+H(0)-math.pi/30)<1e-13
    assert abs(cdf(R2)-1)<1e-13
    assert abs(cdf(RHO)-15*(1-math.cos(RHO)))<1e-13
    for r in [0.025,.12,.3,RHO,.33,R1,.38,.42,.48,.53,R2]:
        a,b=cdf(r),independent_angular_quad(r)
        assert abs(a-b)<2e-10,(r,a,b)
    print('COMPLETE_ELEMENTARY_CDF_MATCHES_INDEPENDENT_SPHERICAL_AREA_QUADRATURE_OK')

    rng=np.random.default_rng(0x20A1)
    normals=rng.normal(size=(420000,3))
    normals/=np.linalg.norm(normals,axis=1)[:,None]
    nearest_angles=np.arccos(np.clip(np.max(normals@sites.T,axis=1),-1,1))
    assert nearest_angles.max()<=R2+1e-12
    for r in [.12,.28,RHO,.345,R1,.42,.48,.52]:
        p=cdf(r); observed=np.mean(nearest_angles<=r)
        se=math.sqrt(max(p*(1-p),1e-9)/len(normals))
        assert abs(observed-p)<6*se+0.001,(r,p,observed,se)
    print('DIRECT_THIRTY_SITE_UNIFORM_ORIENTATION_MONTE_CARLO_CDF_OK_420000')

    # Independent asymptotic normalizations: h^(3/2) onset of overlap,
    # and (R2-r)^2 at closure.
    c_on=(40/math.pi)*math.sqrt(2*math.tan(RHO))
    c_end=(15*A/(math.pi*B))*math.sqrt(1+B*B)
    for eps in [2e-4,8e-5,2e-5]:
        lost=15*(1-math.cos(RHO+eps))-cdf(RHO+eps)
        ratio=lost/eps**1.5
        assert abs(ratio/c_on-1)<0.01,(eps,ratio,c_on)
    for eps in [1e-3,5e-4,2e-4]:
        ratio=(1-cdf(R2-eps))/eps**2
        assert abs(ratio/c_end-1)<0.02,(eps,ratio,c_end)
    print('SHARP_FIRST_OVERLAP_AND_QUADRATIC_COVERAGE_COMPLETION_COEFFICIENTS_OK')
    print('ALL_ICOSIDODECAHEDRAL_SPHERICAL_COVERAGE_CHECKS_OK')

if __name__=='__main__':test()
