#!/usr/bin/env python3
"""Finite-field incidence-metric spectral diagnostics (not an infinite proof)."""
from itertools import product
from math import exp, log, sqrt
import numpy as np
from scipy.optimize import brentq


def projective_vectors(p):
    vectors = set()
    for v in product(range(p), repeat=3):
        if v == (0, 0, 0):
            continue
        lead = next(x for x in v if x)
        normalized = tuple((x * pow(lead, -1, p)) % p for x in v)
        vectors.add(normalized)
    return sorted(vectors)


def incidence(p):
    vectors = projective_vectors(p)
    return np.array([[(sum(x*y for x, y in zip(a, b)) % p == 0)
                      for b in vectors] for a in vectors], dtype=int)


def metric(M):
    n = len(M)
    d = np.full((2*n, 2*n), 2, dtype=int)
    np.fill_diagonal(d, 0)
    d[:n,n:] = np.where(M, 1, 3)
    d[n:,:n] = d[:n,n:].T
    return d


def formula_eigenvalues(q, exponent):
    n = q*q+q+1
    u, v = 2.0**exponent, 3.0**exponent
    return [(n-1)*u + q+1+q*q*v,
            (n-1)*u - q-1-q*q*v,
            -u + sqrt(q)*(v-1),
            -u - sqrt(q)*(v-1)]


def gaussian_eigs(q, z):
    n = q*q+q+1
    return [1+(n-1)*z*z+(q+1)*z+q*q*z**3,
            (1-z)*(1-q*z+q*q*z*z),
            (1-z*z)*(1-sqrt(q)*z),
            (1-z*z)*(1+sqrt(q)*z)]


def main():
    assertions = 0
    for q in (2,3,5):
        M = incidence(q)
        n = q*q+q+1
        assert M.shape == (n,n)
        assert np.array_equal(M@M.T, q*np.eye(n,dtype=int)+np.ones((n,n),dtype=int))
        assert np.all(M.sum(axis=0)==q+1) and np.all(M.sum(axis=1)==q+1)
        assertions += 3
        d = metric(M)
        assert np.array_equal(d,d.T) and np.all(d.diagonal()==0)
        assertions += 1
        critical = brentq(lambda p: sqrt(q)*(3.**p-1)-2.**p,0,2)
        for p in (0.0,critical-0.05,critical+0.05,1.0,1.4):
            D = np.where(d==0,0.0,d.astype(float)**p)
            vals = np.linalg.eigvalsh(D)
            formulas = formula_eigenvalues(q,p)
            reference = sorted([formulas[0],formulas[1]]+
                               [formulas[2]]*(n-1)+[formulas[3]]*(n-1))
            assert np.allclose(vals,reference,atol=2e-11,rtol=1e-11)
            assert ((formulas[2]<0) == (p<critical))
            assertions += 2
        # Exact graph-distance covariance at rational z on both sides of q^-1/2.
        for z in (0.2, 0.5, 0.75, 0.9):
            K = z**d
            vals = np.linalg.eigvalsh(K)
            forms = gaussian_eigs(q,z)
            reference = sorted([forms[0],forms[1]]+
                               [forms[2]]*(n-1)+[forms[3]]*(n-1))
            assert np.allclose(vals,reference,atol=2e-11,rtol=1e-11)
            assert ((np.min(vals)>1e-10) == (z<q**-0.5))
            assertions += 2
        print('q=',q,'N=',n,'critical_p=',round(critical,12),
              'threshold_t=',round(log(q)/2,12),'spectral tests OK')
    print('All',assertions,'diagnostic assertions passed.')

if __name__ == '__main__':
    main()
