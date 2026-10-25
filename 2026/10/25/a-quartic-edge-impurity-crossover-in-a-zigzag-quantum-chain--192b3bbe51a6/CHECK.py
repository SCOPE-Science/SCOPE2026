"""Reproduce the rank-one resolvent and quartic-edge crossover computations.

Run: python CHECK.py  (requires numpy and scipy).
This is a diagnostic computation, not a replacement for the analytic proof.
"""
import math
import warnings
import numpy as np
from scipy.integrate import IntegrationWarning, quad
from scipy.optimize import brentq
from scipy.sparse import diags
from scipy.sparse.linalg import eigsh


def crossover_y(s):
    lo = max(0.0, 4.0*s)
    hi = max(1.0, lo+1.0)
    root = brentq(lambda t: t*t*(t-4*s)-0.25, lo, hi, xtol=1e-14)
    return root*root


def scaled_green(s, strength, y):
    w = strength**(1.0/3.0)
    end = math.pi/w
    def integrand(x):
        z = 2.0*(math.sin(w*x/2.0)/w)**2
        return 1.0/(math.pi*(y-8.0*s*z+(1.0+4.0*s*w*w)*z*z))
    if s > 0.0:
        split = (2.0/w)*math.asin(w*math.sqrt(2*s/(1+4*s*w*w)))
        return quad(integrand, 0, split, epsabs=3e-9, limit=250)[0] + quad(integrand, split, end, epsabs=3e-9, limit=250)[0]
    return quad(integrand, 0, end, epsabs=3e-9, limit=250)[0]


def exact_scaled_y(s, strength):
    a = 0.25+s*strength**(2/3)
    assert a > 0
    upper = 0.0 if s <= 0 else 16*s*s/(1+4*s*strength**(2/3))
    asymptotic_gap = crossover_y(s) - (16*s*s if s > 0 else 0)
    left = upper + 0.15*asymptotic_gap
    right = upper + max(1.0, 4*crossover_y(s))
    f = lambda y: scaled_green(s, strength, y)-1.0
    assert f(left) > 0.0 and f(right) < 0.0, (s, strength, f(left), f(right))
    return brentq(f, left, right, xtol=2e-12)


def finite_matrix_top(s, strength, N):
    a = 0.25 + s*strength**(2/3)
    d = np.zeros(N)
    d[N//2] = strength
    H = diags([np.full(N-2,-a), np.full(N-1,-1.0), d, np.full(N-1,-1.0), np.full(N-2,-a)], offsets=[-2,-1,0,1,2],format='csr')
    return float(eigsh(H,k=1,which='LA',tol=1e-11,maxiter=80000,return_eigenvectors=False)[0])


def main():
    warnings.simplefilter('error', IntegrationWarning)
    for s in [-2.0,-0.5,0.0,0.5,2.0]:
        limit = crossover_y(s)
        errors=[]
        for strength in [1e-2,1e-3,1e-4]:
            y=exact_scaled_y(s,strength)
            err=abs(y-limit)/limit
            errors.append(err)
            assert y > (16*s*s/(1+4*s*strength**(2/3)) if s>0 else 0)
            assert math.isfinite(y)
            assert err<0.3,(s,strength,err)
        assert errors[0]>errors[1]>errors[2], (s,errors)
        assert errors[2]<0.02, (s,errors)
        print('LIMIT',s,format(limit,'.12g'),'relative errors',*[format(q,'.7g') for q in errors])
    # Independent finite Jacobi-type matrix eigenvalue calculation at moderate coupling.
    # Finite Dirichlet truncation converges to the infinite-lattice bound level from below.
    for s in [-1.0,0.0,1.0,2.0]:
        v=0.025
        a=0.25+s*v**(2/3)
        yy=exact_scaled_y(s,v)
        Eexact=2-2*a+v**(4/3)*yy
        evalN=finite_matrix_top(s,v,1201)
        assert evalN<=Eexact+1e-8,(s,evalN,Eexact)
        assert -1e-8<Eexact-evalN<5e-6,(s,evalN,Eexact)
        print('FINITE',s,'E_exact',format(Eexact,'.12g'),'E_1201',format(evalN,'.12g'),'diff',format(Eexact-evalN,'.7g'))
    assert abs(crossover_y(0)-2**(-4/3))<1e-12
    print('PASS: 15 exact scaled resolvent roots, 4 independent finite-chain checks, critical constant')

if __name__ == '__main__':
    main()
