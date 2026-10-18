#!/usr/bin/env python3
"""Reproduce finite-matrix and quadrature checks for rational Volterra kernels.

Dependencies: numpy and scipy. Run: python check.py
Checks support, but do not replace, the infinite-dimensional proof.
"""
import math
import numpy as np
from numpy.testing import assert_allclose
from scipy.integrate import quad
from scipy.linalg import expm, eigh, solve_continuous_lyapunov


def check_case(label, a, b, c):
    a = np.asarray(a, dtype=float)
    b = np.asarray(b, dtype=float)
    c = np.asarray(c, dtype=float)
    d = a.shape[0]
    assert np.max(np.real(np.linalg.eigvals(a))) < -1.0e-9
    controllability = np.column_stack([np.linalg.matrix_power(a, j) @ b for j in range(d)])
    observability = np.vstack([c @ np.linalg.matrix_power(a, j) for j in range(d)])
    assert np.linalg.matrix_rank(controllability) == d
    assert np.linalg.matrix_rank(observability) == d
    p = solve_continuous_lyapunov(a, -np.outer(b, b))
    assert np.linalg.eigvalsh(p)[0] > 0
    assert_allclose(a @ p + p @ a.T + np.outer(b, b), 0, rtol=1e-10, atol=1e-12)

    def response(t):
        return float(c @ expm(a*t) @ b)

    def vec(t):
        return expm(a*t).T @ c

    for x,y in [(0.13,0.43),(0.87,0.23),(0.31,0.31),(0.97,0.82),(0.4,0.79)]:
        tt = quad(lambda z: response(x-z)*response(y-z),0,min(x,y),epsabs=1e-12)[0]
        ts = quad(lambda z: response(z-x)*response(z-y),max(x,y),1,epsabs=1e-12)[0]
        exact = float(vec(1-x)@p@vec(1-y)-vec(x)@p@vec(y))
        assert_allclose(tt-ts, exact, atol=3e-11, rtol=2e-10)

    # The two normalized parity Gramians. They are positive because stable
    # exponentials of opposite signs share no nonzero finite-dimensional mode.
    n = 601
    xx = np.linspace(0,1,n)
    h = 1/(n-1)
    w = np.ones(n)*h
    w[0]=w[-1]=h/2
    u = np.array([vec(t) for t in xx])
    ur = np.array([vec(1-t) for t in xx])
    g = u.T @ (w[:,None]*u)
    hmat = u.T @ (w[:,None]*ur)
    gp = (g+hmat+g.T+hmat.T)/2
    gm = (g-hmat+g.T-hmat.T)/2
    assert np.linalg.eigvalsh(gp)[0] > 0
    assert np.linalg.eigvalsh(gm)[0] > 0
    vals_p, vp = eigh(gp)
    rootp = (vp*np.sqrt(vals_p))@vp.T
    reduced = rootp @ p @ gm @ p @ rootp
    exact_ev = np.sqrt(np.maximum(np.linalg.eigvalsh(reduced),0))
    assert exact_ev[0] > 0

    # A direct Nyström discretization of the self-commutator kernel, rather
    # than the reduced Gram formula, has d positive and d negative modes.
    nk=151
    xm=(np.arange(nk)+0.5)/nk
    um=np.array([vec(t) for t in xm])
    urm=np.array([vec(1-t) for t in xm])
    kh=(urm@p@urm.T-um@p@um.T)/nk
    eig=np.linalg.eigvalsh(kh)
    pos=eig[-d:]
    neg=eig[:d]
    assert_allclose(pos,exact_ev,atol=4e-6,rtol=8e-4)
    assert_allclose(neg,-exact_ev[::-1],atol=4e-6,rtol=8e-4)
    assert np.max(abs(eig[d:-d])) < 2e-12
    assert_allclose(np.sum(eig),0,atol=1e-11)
    assert_allclose(np.prod(pos),np.linalg.det(p)*math.sqrt(np.linalg.det(gp)*np.linalg.det(gm)),atol=1e-6,rtol=3e-3)

    # Independently approximate the original lower-triangular integration
    # operator. The discretized matrix commutator converges to the kernel.
    n2=101
    ym=(np.arange(n2)+.5)/n2
    mat=np.zeros((n2,n2))
    for i in range(n2):
        for j in range(i):
            mat[i,j]=response(ym[i]-ym[j])/n2
    original=mat@mat.T-mat.T@mat
    uv=np.array([vec(z) for z in ym]);rv=np.array([vec(1-z) for z in ym])
    analytical=(rv@p@rv.T-uv@p@uv.T)/n2
    assert np.linalg.norm(original-analytical) < 2.0e-4
    print(label+': OK', 'degree',d,'positive eigenvalues',np.array2string(pos,precision=8))
    return 1


def main():
    checks=0
    checks+=check_case('one real pole',[[-1.3]],[1.2],[0.7])
    checks+=check_case('two distinct real poles',[[-1,0],[0,-2]],[1,1],[1,0.6])
    checks+=check_case('double real pole',[[-2,1],[0,-2]],[0,1],[1,0])
    checks+=check_case('conjugate complex poles',[[-0.8,-2.5],[2.5,-0.8]],[1,0],[1,0])
    z=1.3
    single=(1.2*0.7)**2*math.exp(-z)/(2*z)*math.sqrt((math.sinh(z)/z)**2-1)
    assert single>0
    # In the classical zero-decay limit the unscaled Volterra commutator
    # has two nonzero eigenvalues, +/-1/(2sqrt(3)).
    for a in [0.1,0.03,0.01]:
        val=math.exp(-a)/(2*a)*math.sqrt((math.sinh(a)/a)**2-1)
        assert abs(val-1/(2*math.sqrt(3)))<0.35*a
    print('All',checks,'families passed (with independent quadrature, spectral and classical limits).')

if __name__=='__main__':
    main()
