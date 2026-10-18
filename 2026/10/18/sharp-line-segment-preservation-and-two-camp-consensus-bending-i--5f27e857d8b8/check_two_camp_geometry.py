#!/usr/bin/env python3
"""Reproduce algebraic identities and numerical diagnostics for a two-camp
multidimensional opinion system. All calculations use Python's standard library.
This program is a finite diagnostic, not a substitute for the continuum proof.
"""
from fractions import Fraction as F
from math import log, exp


def rates(d, alpha1, eta1, beta, p):
    d1, d2 = d
    a = alpha1 * d1 + (1-alpha1)*d2
    e = eta1 * d1 + (1-eta1)*d2
    fx = [1 - (beta*dj + (1-beta)*a)/2 for dj in d]
    fy = [1 - (beta*dj + (1-beta)*e)/2 for dj in d]
    h = [(1-p)*fx[j]+p*fy[j] for j in range(2)]
    return fx, fy, h


def exact_identities():
    cases = 0
    for d1,d2 in [(F(9,5),F(1,5)),(F(3,5),F(8,5)),(F(7,10),F(7,10))]:
        for a,e in [(F(4,5),F(1,5)), (F(1),F(0)),(F(1,3),F(1,3))]:
            for b in [F(0),F(1,2),F(1)]:
                for p in [F(1,4),F(1,2),F(3,4)]:
                    d=(d1,d2)
                    fx,fy,h=rates(d,a,e,b,p)
                    assert h[1]-h[0] == b*(d1-d2)/2
                    lhs=[p*(1-p)*(fx[j]-fy[j])*d[j] for j in range(2)]
                    rhs=[-p*(1-p)*(1-b)*(a-e)*(d1-d2)*d[j]/2 for j in range(2)]
                    assert lhs==rhs
                    assert (1-p)*fx[0]+p*fy[0]==h[0]
                    assert (1-p)*fx[1]+p*fy[1]==h[1]
                    cases+=1
    return cases


def integrate(beta,p=0.5,alpha1=1.,eta1=0.,d=(1.8,0.2),step=0.01,end=50.):
    start=[-d[0]/2,-d[1]/2,d[0]/2,d[1]/2,0.]
    def f(z):
        x=z[:2];y=z[2:4]
        D=[y[j]-x[j] for j in range(2)]
        fx,fy,_=rates(D,alpha1,eta1,beta,p)
        q=[D[j]/d[j] for j in range(2)]
        j_integrand=(D[0]-D[1])*(q[0]-q[1])
        return [(1-p)*fx[0]*D[0],(1-p)*fx[1]*D[1],
                -p*fy[0]*D[0],-p*fy[1]*D[1],j_integrand]
    z=start[:]
    for _ in range(round(end/step)):
        k1=f(z)
        k2=f([z[j]+step*k1[j]/2 for j in range(5)])
        k3=f([z[j]+step*k2[j]/2 for j in range(5)])
        k4=f([z[j]+step*k3[j] for j in range(5)])
        z=[z[j]+step*(k1[j]+2*k2[j]+2*k3[j]+k4[j])/6 for j in range(5)]
    theta=[(z[j]+d[j]/2)/d[j] for j in range(2)]
    error=max(abs(z[j]-z[j+2]) for j in range(2))
    exact_quad=(p*(1-p)*(1-beta)*(alpha1-eta1)/2)*z[4]
    return theta,theta[1]-theta[0],exact_quad,error


def small_beta_coefficient(p,alpha1,eta1,d):
    a=[alpha1,1-alpha1];e=[eta1,1-eta1]
    bar=[(1-p)*a[j]+p*e[j] for j in range(2)]
    c=sum(bar[j]*d[j] for j in range(2))/2
    assert 0<c<1
    if abs(c)<1.e-6:
        raise ValueError('Use analytic J(0)=1/6 for tiny c')
    J=(c+log(1-c)+0.5*log(1-c)**2)/c**3
    return p*(1-p)*(alpha1-eta1)*(d[0]-d[1])**2*J/4


def main():
    print('Exact rational algebra cases:',exact_identities())
    base=integrate(.5)
    assert 0 < base[0][0] < base[0][1] < 1
    assert abs(base[1]-base[2])<1e-9
    assert base[3]<1e-9
    print('Strict interior topic bend:',base)
    for beta in [0.,1.]:
        v=integrate(beta)
        assert abs(v[1])<1e-9
        print('Degenerate beta:',beta,v)
    for a,e in [(0.2,.8),(.8,.2),(.6,.6)]:
        v=integrate(.5,alpha1=a,eta1=e,d=(1.6,.4))
        if a==e: assert abs(v[1])<1e-9
        else: assert (v[1]>0)==(a>e)
        assert abs(v[1]-v[2])<1e-9
        print('Importance ordering:',a,e,v)
    for d in [(0.2,1.8),(.8,.8)]:
        v=integrate(.5,d=d)
        if d[0]==d[1]: assert abs(v[1])<1e-9
        else: assert v[1]>0
        print('Gap ordering:',d,v)
    B=small_beta_coefficient(.5,1,0,(1.8,.2))
    for beta in [.001,.003]:
        v=integrate(beta)
        assert abs(v[1]/beta-B)/B<.004
        print('Small beta:',beta,'quotient=',v[1]/beta,'limit=',B)
    print('Finite diagnostics passed; continuous-time theorem uses analytical proof.')

if __name__=='__main__':
    main()
