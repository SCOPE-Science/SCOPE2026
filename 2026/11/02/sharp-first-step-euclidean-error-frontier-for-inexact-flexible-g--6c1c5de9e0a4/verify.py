#!/usr/bin/env python3
"""Self-contained arithmetic checks for the one-step flexible-GMRES error profile.
Requires only Python 3's standard library. Numerical checks supplement the proof.
"""
from fractions import Fraction as F
from math import hypot, sqrt, isclose


def dot(v, w):
    return sum(x*y for x, y in zip(v, w))


def gain(kappa, t):
    d = kappa - 1.0 / kappa
    return 0.5*t*(sqrt(4+d*d*(1-t*t)) + d*sqrt(1-t*t))


def peak_location(kappa):
    d = kappa - 1.0/kappa
    return sqrt((4+d*d)/(4+2*d*d))


def optimum(kappa, mu):
    return gain(kappa, min(mu, peak_location(kappa)))


def top_singular_vector(kappa, t):
    """Right maximizing singular vector of B R B^-1; B=diag(kappa,1)."""
    q = sqrt(1-t*t)
    T00, T01, T10, T11 = t, -kappa*q, q/kappa, t
    a = T00*T00 + T10*T10
    b = T00*T01 + T10*T11
    c = T01*T01 + T11*T11
    ell = (a+c+sqrt((a-c)**2+4*b*b))/2
    y = (b, ell-a)
    if hypot(*y) < 1e-12:
        y = (ell-c, b)
    if hypot(*y) < 1e-12:
        y = (1.0, 0.0)
    scale = hypot(*y)
    return (y[0]/scale, y[1]/scale)


def witness(kappa, t):
    """Two-mode SPD A, unit residual v, preconditioning z, FGMRES alpha and gain."""
    q = sqrt(1-t*t)
    y = top_singular_vector(kappa, t)
    unscaled_v = (y[0]/kappa, y[1])
    c = hypot(*unscaled_v)
    v = (unscaled_v[0]/c, unscaled_v[1]/c)
    u = (t*v[0]-q*v[1], q*v[0]+t*v[1])
    w = (v[0]-t*u[0], v[1]-t*u[1])
    z = (kappa*w[0], w[1])
    alpha = dot(v, w)/dot(w, w)
    residual = (v[0]-alpha*w[0], v[1]-alpha*w[1])
    e0 = (kappa*v[0], v[1])
    e1 = (kappa*residual[0], residual[1])
    inner = hypot(v[0]-w[0], v[1]-w[1])
    return inner, hypot(*residual), hypot(*e1)/hypot(*e0), alpha


def checks():
    exact = 0
    triples = [(F(3,5), F(4,5)), (F(5,13), F(12,13)), (F(8,17), F(15,17))]
    for k in range(1,12):
        B = (F(k), F(1))
        for v in triples:
            for t, q in triples:
                u = (t*v[0]-q*v[1],q*v[0]+t*v[1])
                assert dot(v,v) == dot(u,u) == 1
                assert dot(v,u)==t
                w = (v[0]-t*u[0],v[1]-t*u[1])
                z = (B[0]*w[0],B[1]*w[1])
                # A=diag(1/k,1): its image of z is w
                assert (z[0]/B[0],z[1]/B[1]) == w
                alpha = dot(v,w)/dot(w,w)
                assert alpha == 1
                res = (v[0]-alpha*w[0],v[1]-alpha*w[1])
                assert res == (t*u[0],t*u[1])
                assert dot(res,w) == 0
                assert dot((v[0]-w[0],v[1]-w[1]),(v[0]-w[0],v[1]-w[1])) == t*t
                exact += 1
    floating = 0
    for kappa in (1.1,1.25,2.,3.,5.,10.,100.):
        for t in (0.001,0.05,0.1,0.2,0.4,0.6,0.71,0.85,0.97,0.999):
            inner, resid, ratio, alpha = witness(kappa,t)
            assert isclose(inner,t,rel_tol=1e-9,abs_tol=1e-11)
            assert isclose(resid,t,rel_tol=1e-9,abs_tol=1e-11)
            assert isclose(alpha,1.,rel_tol=1e-9,abs_tol=1e-11)
            assert isclose(ratio,gain(kappa,t),rel_tol=1e-8,abs_tol=1e-10), (kappa,t,ratio,gain(kappa,t))
            floating += 1
        d=kappa-1/kappa
        tc=1/sqrt(1+d*d)
        tp=peak_location(kappa)
        assert isclose(gain(kappa,tc),1.,abs_tol=1e-10)
        assert isclose(gain(kappa,tp),(kappa+1/kappa)/2,abs_tol=1e-10)
        assert gain(kappa,tc/2)<1
        assert gain(kappa,(tc+tp)/2)>1
        for mu in (0.,.01,.04,.1,.15,.2,.35,.5,.6,.7,.8,.9,.99):
            best=optimum(kappa,mu)
            for j in range(301):
                t=mu*j/300
                assert gain(kappa,t)<=best+1e-9, (kappa,mu,t,gain(kappa,t),best)
                floating+=1
    assert optimum(1.,.3)==.3
    print('VERIFY_OK exact_rational_instances=%d floating_witness_and_envelope_instances=%d' % (exact,floating))


if __name__=='__main__':
    checks()
