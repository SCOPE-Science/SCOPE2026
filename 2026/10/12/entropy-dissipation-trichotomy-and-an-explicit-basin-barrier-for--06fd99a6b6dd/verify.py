#!/usr/bin/env python3
"""Reproducible arithmetic checks for a finite-state mean-field opinion model.

Requires only Python 3 standard library. Finite checks supplement an analytical proof.
"""
from fractions import Fraction as Q
from math import log, isclose


def ode(q):
    L = len(q) - 1
    m = sum(j*q[j] for j in range(L+1))
    r, s = m / L, 1 - m / L
    J = [r*q[j]-s*q[j+1] for j in range(L)]
    return [(-J[0])] + [J[j-1]-J[j] for j in range(1, L)] + [J[-1]]


def energy(q):
    L = len(q)-1
    m = sum(j*x for j,x in enumerate(q))
    def xlogx(x):
        return x*log(x) if x else 0.0
    return sum(xlogx(float(x)) for x in q) - xlogx(float(m)) - xlogx(float(L-m)) + L*log(L)


def hessian_form(L,h):
    assert len(h)==L+1 and sum(h)==0
    return (L+1)*sum(x*x for x in h)-Q(4,L)*sum(j*x for j,x in enumerate(h))**2


def delta_flux(L,j,a,q):
    # Direction h=e_a-e_0 in independent simplex coordinate q_a.
    m=sum(b*q[b] for b in range(L+1))
    r,s=m/Q(L),Q(1)-m/Q(L)
    def h(b): return int(b==a)-int(b==0)
    return Q(a,L)*(q[j]+q[j+1])+r*h(j)-s*h(j+1)


def test():
    for L in (2,4,6,10):
        u=[Q(1,L+1)]*(L+1)
        assert ode(u)==[Q(0)]*(L+1)
        for endpoint in (0,L):
            e=[Q(0)]*(L+1);e[endpoint]=1
            assert ode(e)==[Q(0)]*(L+1)
        # Exact Jacobian in reduced coordinates, checked by exact perturbation differences.
        for a in range(1,L+1):
            eps=Q(1,100000)
            qp=[x for x in u];qp[0]-=eps;qp[a]+=eps
            fm=ode(qp);f0=ode(u)
            # ODE is quadratic; symmetric differences give exact directional linearization.
            qm=[x for x in u];qm[0]+=eps;qm[a]-=eps
            fminus=ode(qm)
            for j in range(L+1):
                direct=(fm[j]-fminus[j])/(2*eps)
                jd=(delta_flux(L,j-1,a,u) if j>=1 else 0) -(delta_flux(L,j,a,u) if j<L else 0)
                assert direct==jd
        # Negative Hessian direction and positive transverse direction, exactly.
        center=[Q(2*j-L,2) for j in range(L+1)]
        assert sum(center)==0 and hessian_form(L,center)<0
        h=[Q(0)]*(L+1);h[0]=1;h[1]=-2;h[2]=1
        assert hessian_form(L,h)>0
        # Geometric-distribution stationarity polynomial is strictly positive above 1.
        for z in (Q(1,2),Q(4,5),Q(5,4),Q(2)):
            f=(L-1)*z**(L+1)-(L+1)*z**L+(L+1)*z-(L-1)
            assert (f<0)==(z<1)
            assert (f>0)==(z>1)
        for eta in (Q(1,3),Q(3,5),Q(7,9)):
            powers=[eta**j for j in range(L+1)]
            q=[x/sum(powers) for x in powers]
            d=ode(q)
            m=sum(j*x for j,x in enumerate(q))
            r,s=m/L,1-m/L
            flux=[float(r*q[j]-s*q[j+1]) for j in range(L)]
            diss=-sum(x*log(float(r*q[j]/(s*q[j+1]))) for j,x in enumerate(flux))
            assert diss<-1e-10
            eps=1e-6
            qplus=[float(q[j])+eps*float(d[j]) for j in range(L+1)]
            qminus=[float(q[j])-eps*float(d[j]) for j in range(L+1)]
            dnum=(energy(qplus)-energy(qminus))/(2*eps)
            assert isclose(dnum,diss,rel_tol=2e-5,abs_tol=5e-7)
            if m>0 and m<L:
                kl_u=sum(float(x)*log((L+1)*float(x)) for x in q)
                bern= float(m/L)*log(2*float(m/L))+(1-float(m/L))*log(2*(1-float(m/L)))
                assert isclose(energy(q)-(L*log(2)-log(L+1)),kl_u-L*bern,abs_tol=1e-12)
    q=[Q(x,1441) for x in (625,375,225,135,81)]
    assert sum(q)==1
    assert sum(j*x for j,x in enumerate(q))==Q(1554,1441)>1
    assert energy(q)<4*log(2)-log(5)
    print('VERIFY_OK: exact rational flux/Jacobians, Hessian signs, entropy identities and extended basin')


if __name__=='__main__':
    test()
