#!/usr/bin/env python3
"""Cross-method numerical checks of two-rate first-passage formulas.

Requires NumPy and SciPy. A numerical check is not a proof of the asymptotics.
"""
import math
import numpy as np
from scipy.optimize import brentq
from scipy.sparse import lil_matrix
from scipy.sparse.linalg import spsolve

COUNTS = 0

def check(truth, message):
    global COUNTS
    COUNTS += 1
    if not truth:
        raise AssertionError(message)


def f(r, a=1., D=1.):
    return math.expm1(a * math.sqrt(r / D)) / r


def fp(r, a=1., D=1.):
    z = a * math.sqrt(r / D)
    return (math.exp(z) * (z / 2 - 1) + 1) / r**2


def exact_T(m, d, nu, a=1., D=1.):
    """Return stationary-environment mean and conditional means from the BVP."""
    R = np.diag([m-d, m+d])
    Q = np.array([[nu, -nu], [-nu, nu]], dtype=float)
    A = Q + R
    vals, vec = np.linalg.eigh(A)
    E = (vec * np.exp(-a*np.sqrt(vals / D))) @ vec.T
    v = np.linalg.solve(Q+R@E, np.ones(2))
    out = (np.eye(2)-E)@v
    L = np.linalg.solve(A, np.eye(2) - E)
    independent = np.linalg.solve(np.eye(2)-L@R, L@np.ones(2))
    check(np.max(np.abs(independent-out))<5e-9,'independent renewal kernel')
    return float(out.mean()), out


def discrete_T(m, d, nu, a=1., D=1., h=.04, upper=8.):
    """Independent absorbing/reflecting birth-death lattice generator."""
    n = int(round(upper/h))
    k = int(round(a/h))
    assert 0 < k < n
    M = lil_matrix((2*n, 2*n), dtype=float)
    rhs = np.ones(2*n)
    def ix(i, phase): return phase*n+i-1
    for phase,r in enumerate((m-d,m+d)):
        for i in range(1,n+1):
            ix0 = ix(i,phase)
            rates=[]
            if i>1: rates.append((ix(i-1,phase), D/h**2))
            else: rates.append((None, D/h**2))
            if i<n: rates.append((ix(i+1,phase), D/h**2))
            rates.append((ix(i,1-phase), nu))
            if i!=k: rates.append((ix(k,phase), r))
            M[ix0,ix0] += sum(rate for _,rate in rates)
            for dest,rate in rates:
                if dest is not None: M[ix0,dest] -= rate
    x = spsolve(M.tocsr(),rhs)
    return (x[ix(k,0)]+x[ix(k,1)])/2


def run():
    root = brentq(lambda z:math.exp(z)*(z-2)+2, 1., 2.)
    check(abs(root-1.593624260040012)<1e-12,'critical root')
    check(abs(root*root-2.5396382821880756)<1e-11,'critical rate')
    for m,d,a,D in [(1,.5,1,1),(5,2,1,1),(10,5,1,1),
                    (2.6,1,1,1),(4,1,2,3),(7,3,.7,2),(.6,.2,1,1)]:
        zero,_=exact_T(m,d,0.,a,D)
        check(abs(zero-(f(m-d,a,D)+f(m+d,a,D))/2)<1e-11,'quenched limit')
        check(zero>f(m,a,D),'slow disorder penalty')
        for nu in [0.05,0.5,3.,20.]:
            t, conditional=exact_T(m,d,nu,a,D)
            check(np.all(conditional>0),'positive conditional MFPT')
            check(t>0,'positive mean MFPT')
        for nu in [1e3,1e4]:
            t,_=exact_T(m,d,nu,a,D)
            expected=-d*d*fp(m,a,D)/2
            check(abs(nu*(t-f(m,a,D))-expected)<max(.05,abs(expected)*.035),
                  'fast switching coefficient')
        all_equal,_=exact_T(m,0.,17.,a,D)
        check(abs(all_equal-f(m,a,D))<1e-11,'constant rate invariant')
    for m,d,nu in [(5,2,.2),(5,2,1.),(1,.4,.8),(7,3,4.)]:
        exact,_=exact_T(m,d,nu)
        disc=discrete_T(m,d,nu)
        check(abs(exact-disc)<.035,'independent lattice-generator comparison')
    m,d=5.,2.
    slow,_=exact_T(m,d,.01)
    fast,_=exact_T(m,d,100.)
    check(slow>f(m)>fast,'sign-changing search benefit')
    cross=brentq(lambda nu:exact_T(m,d,nu)[0]-f(m),.01,100.)
    check(.1<cross<100,'finite crossover')
    print(f'PASSED {COUNTS} deterministic assertions; finite crossover {cross:.8g}; z_* {root:.12g}')

if __name__=='__main__':
    run()
