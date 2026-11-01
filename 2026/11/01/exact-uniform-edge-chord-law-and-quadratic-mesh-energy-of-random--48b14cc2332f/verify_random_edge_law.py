#!/usr/bin/env python3
"""Reproduce the exact chord-law integrals and independently sample convex-hull edges.

Scientific reference: Akopyan, Edelsbrunner and Nikitenko, arXiv:2007.07783,
whose spherical Blaschke-Petkantschin decomposition is the starting point.
"""
import math
import numpy as np
from scipy import integrate
from scipy.special import beta, betainc
from scipy.spatial import ConvexHull

PI = math.pi

def angle_density(theta):
    s, c = math.sin(theta), math.cos(theta)
    return (8*s*s+4*s*c*(PI-2*theta))/(3*PI)

def shape_moment(k):
    return integrate.quad(lambda theta: angle_density(theta)*(2*math.sin(theta))**k,
                          0.0, PI/2, epsabs=1e-11, epsrel=1e-11)[0]

def edge_moment(n,k):
    return (2.0**k*beta(n-1+k/2,2+k/2)/beta(n-1,2))*shape_moment(k)

def cdf_edge(n, x):
    if x<=0: return 0.0
    if x>=2: return 1.0
    a,b=n-1,2
    def integrand(theta):
        u=2*math.sin(theta)
        if u<=x: return angle_density(theta)
        d=math.sqrt(max(0.0,1-(x/u)**2))
        p0=(1-d)/2
        p1=(1+d)/2
        return angle_density(theta)*(betainc(a,b,p0)+1-betainc(a,b,p1))
    th=math.asin(x/2)
    res=integrate.quad(integrand,0,th,epsabs=1e-10)[0]
    res+=integrate.quad(integrand,th,PI/2,epsabs=1e-10,points=[th],limit=100)[0]
    return res

def simulation(n, n_hulls, rng):
    all_lengths=[]
    energies=[]
    for _ in range(n_hulls):
        xyz=rng.standard_normal((n,3)); xyz/=np.linalg.norm(xyz,axis=1)[:,None]
        hull=ConvexHull(xyz)
        edges=set()
        for a,b,c in hull.simplices:
            edges.add(tuple(sorted((int(a),int(b)))))
            edges.add(tuple(sorted((int(a),int(c)))))
            edges.add(tuple(sorted((int(b),int(c)))))
        assert len(edges)==3*n-6
        ls=np.array([np.linalg.norm(xyz[a]-xyz[b]) for a,b in edges])
        all_lengths.extend(ls)
        energies.append(np.dot(ls,ls))
    return np.asarray(all_lengths),float(np.mean(energies))

def main():
    for k,target in [(0,1),(1,128/(27*PI)),(2,2.5),(4,70/9)]:
        observed=shape_moment(k)
        print(f'shape moment {k}: quadrature={observed:.12g}, predicted={target:.12g}')
        assert abs(observed-target)<2e-9
    for x in (0.25,0.5,1.0,1.5,1.9):
        observed=cdf_edge(4,x)
        print(f'n=4 CDF({x}): computed={observed:.10f}, independent chord CDF={x*x/4:.10f}')
        assert abs(observed-x*x/4)<2e-7
    rng=np.random.default_rng(20261031)
    for n,rep in [(4,450),(6,400),(12,350),(30,300)]:
        analytic=60*(n-1)*(n-2)/((n+1)*(n+2))
        assert abs((3*n-6)*edge_moment(n,2)-analytic)<1e-9
        observed,mean_energy=simulation(n,rep,rng)
        theo_cdf=np.array([cdf_edge(n,x) for x in (0.3,0.6,1.0,1.5)])
        emp_cdf=np.array([(observed<=x).mean() for x in (0.3,0.6,1.0,1.5)])
        discrepancy=float(np.max(np.abs(theo_cdf-emp_cdf)))
        relative_err=abs(mean_energy/analytic-1)
        print(f'n={n}: expected energy {analytic:.8f}; hull mean {mean_energy:.8f}; '
              f'CDF max error={discrepancy:.5f}, relative energy error={relative_err:.5f}')
        assert discrepancy<0.07 and relative_err<0.07
    print('ALL_SHAPE_DENSITY_CDF_AND_HULL_CHECKS_PASSED')

if __name__=='__main__': main()
