"""Reproducible quadrature checks for solid angles of coordinate-right simplices.

Numerical quadrature is corroboration; the all-dimensional theorem uses analytic proof.
Run with: python check.py
"""
import itertools
import math
import numpy as np
from numpy.polynomial.legendre import leggauss


def angle_via_simplex(n, i, a, order=36):
    """Exact simplex-gonomonic integral evaluated by tensor Gauss quadrature."""
    assert n == len(a) and n >= 2 and 1 <= i <= n
    x, w = leggauss(order)
    x, w = (x + 1) / 2, w / 2
    pos = [j for j in range(n) if j != i - 1]
    total = 0.0
    for indices in itertools.product(range(order), repeat=n - 1):
        rem, jac, square_sum, weight = 1.0, 1.0, 0.0, 1.0
        for k, index in enumerate(indices):
            u = float(x[index]); t = rem * u
            square_sum += a[pos[k]]**2 * t*t
            jac *= rem; rem *= 1-u
            weight *= float(w[index])
        total += weight * jac * (a[i - 1]**2 + square_sum)**(-n/2)
    return math.prod(a) * total


def tetra_angle_direct(i, a):
    """Independent exact-geometric trihedral solid-angle formula."""
    n = 3; verts = np.vstack((np.zeros(3), np.diag(a)))
    v = verts[i]
    e = [verts[j]-v for j in range(n+1) if j != i]
    nrm = [np.linalg.norm(q) for q in e]
    numerator = abs(float(np.linalg.det(np.column_stack(e))))
    denom = math.prod(nrm) + sum(float(np.dot(e[k],e[(k+1)%3]))*nrm[(k+2)%3] for k in range(3))
    return 2*math.atan2(numerator, denom)


def asymptotic_prediction(n, b, L):
    assert len(b)==n-1
    m=n-1
    prod = math.prod(b)
    ang = prod / (math.factorial(m)*L**m) * (1-sum(x*x for x in b)/((n+1)*L*L))
    vol = L*prod/math.factorial(n)
    delta = math.hypot(L,max(b))
    fullness = vol/delta**n
    correction=n*max(b)**2/2 - sum(x*x for x in b)/(n+1)
    return ang,fullness,correction


def main():
    for a in [(1.,2.,3.),(4.,1.,2.),(1.,1.,1.),(1.,2.,8.)]:
        angles = [angle_via_simplex(3,i,a) for i in (1,2,3)]
        direct = [tetra_angle_direct(i,a) for i in (1,2,3)]
        err = max(abs(x-y) for x,y in zip(angles,direct))
        assert err < 1e-11,(a,err,angles,direct)
        assert int(np.argmin(angles)) == int(np.argmax(a)),(a,angles)
        print('n=3',a,'angles',angles,'direct residual',err)
    for n,b in [(2,[2.]),(3,[1.,2.]),(4,[1.,2.,3.])]:
        for L in (16.,32.):
            a = (L,*b)
            val = angle_via_simplex(n,1,a,order=26)
            leading,mu,coefficient = asymptotic_prediction(n,b,L)
            assert abs(val-leading) <= 6*val/L**4 * (max(b)**4+1), (n,L,val,leading)
            scaled = L**2*(val/(n*mu)-1)
            assert abs(scaled-coefficient)<(0.30 if L==16. else 0.10),(n,L,scaled,coefficient)
            print('n=',n,'L=',L,'ratio-gap rescaled=',scaled,'theory=',coefficient)
    print('PASS numerical quadrature, independent trihedral comparisons, ordering, and asymptotic coefficients')

if __name__=='__main__':
    main()
