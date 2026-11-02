"""Reproduce finite structural and probability checks for Bernoulli-thinned orthoplexes.
Requires Python 3.10+, numpy and scipy. Analytical limits are proved in RESULT.md,
not by these finite calculations.
"""
from fractions import Fraction
from math import comb, factorial, isclose, log
import numpy as np
from scipy.spatial import ConvexHull


def poly_mul(a, b):
    c = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            c[i+j] += x*y
    return c


def face_poly_coefficients(d, k):
    assert 1 <= k <= d
    a = [comb(k, j)*2**j for j in range(k+1)] + [1]
    for _ in range(d-k):
        a = poly_mul(a, [1, 1])
    return a


def face_counts_from_hull(d, k):
    verts=[]
    for i in range(d):
        e=np.eye(d)[i]
        verts.append(e)
        if i<k:
            verts.append(-e)
    v=np.array(verts)
    h=ConvexHull(v, qhull_options='Qx')
    assert isclose(h.volume, 2**k/factorial(d), rel_tol=1e-9,abs_tol=1e-10)
    facet_sets=[]
    for eq in h.equations:
        faceset=frozenset(i for i, w in enumerate(v) if abs(float(np.dot(eq[:-1],w)+eq[-1])) <1e-7)
        if faceset not in facet_sets:
            facet_sets.append(faceset)
    faces={frozenset(range(len(v)))}
    queue=list(faces)
    while queue:
        face=queue.pop()
        for facet in facet_sets:
            c=face & facet
            if c not in faces:
                faces.add(c)
                queue.append(c)
    counts=[0]*(d+2)
    for f in faces:
        if not f:
            dim=-1
        elif len(f)==1:
            dim=0
        else:
            w=v[list(f)]
            dim=int(np.linalg.matrix_rank(w[1:]-w[0],tol=1e-8))
        counts[dim+1]+=1
    return counts

for d in range(2,6):
    for k in range(1,d+1):
        assert face_counts_from_hull(d,k)==face_poly_coefficients(d,k),(d,k)
print('ALL_FACE_LATTICE_AND_VOLUME_TESTS_PASSED')

for d in range(2,9):
    for p in [Fraction(1,5), Fraction(1,2), Fraction(4,5)]:
        rho=p/(2-p)
        masses=[comb(d,k)*p**(2*k)*(2*p*(1-p))**(d-k) for k in range(1,d+1)]
        full=(p*(2-p))**d-(2*p*(1-p))**d
        assert sum(masses)==full
        volume_sum=sum(m*Fraction(2**k,2**d) for k,m in enumerate([0]+masses) if k)
        face_sum=sum(m*2**(d-k)*(3**k+1) for k,m in enumerate([0]+masses) if k)
        mean_r=((1+rho)**d-(1-rho)**d)/(2**d*(1-(1-rho)**d))
        mean_z=((2+rho)**d+(2-rho)**d-2*(2*(1-rho))**d)/(1-(1-rho)**d)
        assert volume_sum/full==mean_r
        assert face_sum/full==mean_z
        assert volume_sum==p**d*(1-(1-p)**d)
print('ALL_RATIONAL_MOMENT_IDENTITIES_PASSED')

for rho in [0.1,0.33,0.6,0.9]:
    typical_z=log(2)+rho*log(1.5)
    mean_z=log(2+rho)
    typical_r=(rho-1)*log(2)
    mean_r=log((1+rho)/2)
    assert typical_z < mean_z and typical_r < mean_r
print('ANNEALED_VERSUS_TYPICAL_GAPS_PASSED')
print('ALL_CHECKS_PASSED')
