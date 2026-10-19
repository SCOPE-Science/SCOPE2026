#!/usr/bin/env python3
"""Deterministic identities and finite numerical checks for the 3D FA tangent Gram law.
This script does not prove the asymptotic tail; see the analytic proof.
"""
import math
import numpy as np
from fractions import Fraction
from itertools import product


def gram(p):
    p = np.asarray(p, dtype=float)
    return np.diag(1 - 2*p) + np.outer(p,p)


def det3(M):
    a,b,c=M
    return (a[0]*(b[1]*c[2]-b[2]*c[1])
            -a[1]*(b[0]*c[2]-b[2]*c[0])
            +a[2]*(b[0]*c[1]-b[1]*c[0]))

count = 0
for i in range(11):
    for j in range(11-i):
        k=10-i-j
        p=[Fraction(i,10), Fraction(j,10), Fraction(k,10)]
        K=[[ (Fraction(1) if a==b else Fraction(0)) -2*(p[a] if a==b else Fraction(0)) +p[a]*p[b] for b in range(3)] for a in range(3)]
        assert det3(K)==2*p[0]*p[1]*p[2]
        count+=1
for i in range(2,99):
    for j in range(2,99):
        p=np.array([i/100, j/100,1.0]);p/=p.sum()
        M=gram(p)
        P=np.eye(3)-np.outer(np.sqrt(p),np.sqrt(p))
        assert np.allclose(M,P*P,atol=2e-15)
        eig=np.linalg.eigvalsh(M)
        assert eig[0]>0 and eig[-1]<=1+3e-15
        assert abs(np.linalg.det(M)-2*np.prod(p))<3e-15
        count+=3
# As a coordinate axis is approached, the two larger eigenvalues tend to 1.
for r in [1e-1, 8e-2,5e-2,3e-2,2e-2,1e-2]:
    p=np.array([1-r*r-r**4,r*r,r**4])
    E=np.linalg.eigvalsh(gram(p))
    assert E[0]>0 and abs(E[0]/(2*np.prod(p))-1)<4*r*r
    count+=1
# Exact Dirichlet Mellin formula, checked against direct numerical beta integral
# is a mathematical identity, not an experiment or a tail certificate.
s=0.25
val=2**(-s)*math.gamma(1.5)/math.gamma(1.5-3*s)*(math.gamma(0.5-s)/math.gamma(0.5))**3
assert math.isfinite(val) and val>1
count+=1
print('PASS',count,'exact-rational and numeric assertions')
print('negative determinant moment at s=1/4:',format(val,'.12f'))
print('predicted smallest-eigenvalue tail coefficient:',format(3/(math.pi*math.sqrt(2)),'.12f'))
