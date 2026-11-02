#!/usr/bin/env python3
"""Independent computational checks for the excentral acute-triangle transport theorem.

Tests are finite diagnostics; the accompanying geometric and affine proofs
establish the statements for the complete continuous distribution.
"""
import itertools
import math
import numpy as np
from scipy.stats import ks_2samp


def excentral(x):
    return (1.0-x)/2.0


def area(x):
    return 2.0*np.prod(np.sin(math.pi*x), axis=-1)


def perimeter(x):
    return 2.0*np.sum(np.sin(math.pi*x), axis=-1)


def inradius(x):
    return 4.0*np.prod(np.sin(math.pi*x/2.0), axis=-1)


def check_symbolic_affine():
    import sympy as s
    M=s.Matrix([[0,s.Rational(1,2),s.Rational(1,2)],
                [s.Rational(1,2),0,s.Rational(1,2)],
                [s.Rational(1,2),s.Rational(1,2),0]])
    assert M*s.ones(3,1)==s.ones(3,1)
    assert M.T*s.ones(3,1)==s.ones(3,1)
    assert M.det()==s.Rational(1,4)
    assert (M*s.Matrix([1,0,0]))==s.Matrix([0,s.Rational(1,2),s.Rational(1,2)])
    assert M*s.Matrix([0,1,0])==s.Matrix([s.Rational(1,2),0,s.Rational(1,2)])
    assert M*s.Matrix([0,0,1])==s.Matrix([s.Rational(1,2),s.Rational(1,2),0])
    return M


def check_finite_grid():
    tested=0
    for n in range(3,49):
        for a in range(1,n-1):
            for b in range(1,n-a):
                c=n-a-b
                x=np.array([a,b,c],dtype=float)/n
                y=excentral(x)
                assert np.isclose(y.sum(),1.0)
                assert np.all((0<y)&(y<0.5))
                sx=np.sort(x)[::-1]; sy=np.sort(y)[::-1]
                assert sy[0] <= sx[0]+1e-14 and sy[:2].sum() <= sx[:2].sum()+1e-14
                for q in (area,perimeter,inradius):
                    assert float(q(y)) >= float(q(x))-2e-14
                    if not np.allclose(x, np.ones(3)/3):
                        assert float(q(y)) > float(q(x))+1e-13
                tested+=1
    return tested


def check_random_law(n=350000):
    rng=np.random.default_rng(20261025)
    x=rng.dirichlet([1.0,1.0,1.0],size=n)
    y=excentral(x)
    z=rng.dirichlet([1.0,1.0,1.0],size=4*n)
    acute=z[np.max(z,axis=1)<0.5]
    prob=acute.shape[0]/float(4*n)
    assert abs(prob-0.25)<0.0013,(prob,acute.shape[0])
    assert np.allclose(y.mean(axis=0),acute.mean(axis=0),atol=0.002)
    assert np.all(np.max(y,axis=1)<0.5)
    for name,fn in [('area',area),('perimeter',perimeter),('inradius',inradius)]:
        assert np.all(fn(y)>fn(x)-1e-12)
        ks=ks_2samp(fn(y),fn(acute),mode='asymp').statistic
        assert ks<0.011,(name,ks)
        print('DIAGNOSTIC',name,'mean_unconditional',float(fn(x).mean()),
              'mean_acute_transport',float(fn(y).mean()),'mean_acute_rejection',
              float(fn(acute).mean()),'KS',float(ks))
    print('DIAGNOSTIC acute_frequency',prob)


if __name__=='__main__':
    print('SYMBOLIC_LINEAR_MAP',check_symbolic_affine())
    print('FINITE_POSITIVE_RATIONAL_TRIPLE_GRID_PASSED',check_finite_grid())
    check_random_law()
    print('ALL_CHECKS_PASSED')
