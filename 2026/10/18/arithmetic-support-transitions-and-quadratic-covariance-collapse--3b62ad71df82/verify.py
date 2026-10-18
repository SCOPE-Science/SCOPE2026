#!/usr/bin/env python3
"""Reproduce covariance and resonance checks for two-kick stochastic exponential quadrature.
Standard library only. Tests are finite numerical cross-checks, not proofs of universal statements.
"""
from math import exp, sin, cos, pi, sqrt
from fractions import Fraction

GAMMA = 0.2
OMEGA = 1.3
LAMBDA = OMEGA**2 + GAMMA**2
SIGMA = 1.17


def e_matrix(t):
    c = cos(OMEGA*t)
    s = sin(OMEGA*t)/OMEGA
    d = exp(-GAMMA*t)
    return (d*(c+GAMMA*s), d*s, -d*LAMBDA*s, d*(c-GAMMA*s))


def kicked_b(t):
    a, b, c, d = e_matrix(t)
    return b, d


def solve3(mat, rhs):
    a = [list(row)+[float(v)] for row, v in zip(mat, rhs)]
    for k in range(3):
        p = max(range(k, 3), key=lambda i: abs(a[i][k]))
        a[p], a[k] = a[k], a[p]
        assert abs(a[k][k]) > 1e-15
        a[k] = [x/a[k][k] for x in a[k]]
        for i in range(3):
            if i != k:
                f = a[i][k]
                a[i] = [a[i][j]-f*a[k][j] for j in range(4)]
    return tuple(a[i][3] for i in range(3))


def stationarity(h, alpha):
    # Right-endpoint approximation of the stochastic convolution on two Brownian subintervals.
    assert h > 0 and 0 < alpha < 1
    a,b,c,d = e_matrix(h)
    u,v = kicked_b(alpha*h)
    q00 = h*SIGMA**2*(1-alpha)*u*u
    q01 = h*SIGMA**2*(1-alpha)*u*v
    q11 = h*SIGMA**2*(alpha+(1-alpha)*v*v)
    mat = ((1-a*a,-2*a*b,-b*b),
           (-a*c,1-a*d-b*c,-b*d),
           (-c*c,-2*c*d,1-d*d))
    return solve3(mat, (q00,q01,q11))


def det(p):
    return p[0]*p[2]-p[1]*p[1]


def lambda_min(p):
    tr=p[0]+p[2]
    largest=(tr+sqrt((p[0]-p[2])**2+4*p[1]**2))/2
    return det(p)/largest


def resonant_determinant(h, alpha, m):
    r=exp(-2*GAMMA*h)
    return (h*SIGMA**2/(1-r))**2*alpha*(1-alpha)*exp(-2*GAMMA*alpha*h)*sin(m*pi*alpha)**2/OMEGA**2


def near_resonance_coefficient(h_star,alpha):
    r=exp(-2*GAMMA*h_star)
    w0=alpha
    wa=(1-alpha)*r**alpha
    total=(w0+wa)/(1-r)
    variance=r/(1-r)**2 + w0*wa*alpha**2/(w0+wa)**2
    return h_star*SIGMA**2*total*variance


def main():
    checks=0
    for alpha in [0.5,1/3,sqrt(2)-1,0.7]:
        for m in range(1,7):
            h=m*pi/OMEGA
            p=stationarity(h,alpha)
            predicted=resonant_determinant(h,alpha,m)
            assert abs(det(p)-predicted) < 5e-9*(1+abs(predicted)), (alpha,m,p,predicted)
            checks+=1
            if alpha == 0.5 and m%2==0:
                assert abs(p[0])<2e-13 and abs(p[1])<2e-13
                checks+=2
            if alpha == 1/3 and m%3==0:
                assert abs(p[0])<2e-13
                checks+=1
            if alpha == sqrt(2)-1:
                assert predicted>0 and det(p)>0
                checks+=2
    for alpha,m in [(.5,2),(1/3,3),(.25,4)]:
        h0=m*pi/OMEGA
        C=near_resonance_coefficient(h0,alpha)
        for eps in [0.01,0.003,0.001]:
            observed=lambda_min(stationarity(h0+eps,alpha))/eps**2
            assert abs(observed/C-1) < .02, (alpha,m,eps,C,observed)
            checks+=1
    for alpha in [0.13,.37,.75]:
        p=stationarity(.001,alpha)
        reference=(SIGMA**2/(4*GAMMA*LAMBDA),0,SIGMA**2/(4*GAMMA))
        assert max(abs(x-y) for x,y in zip(p,reference)) < 2e-3
        checks+=1
    # In reduced form a rational offset a/b creates singularities exactly at m multiple of b.
    for q in range(2,16):
        for a in range(1,q):
            if Fraction(a,q).denominator != q:continue
            alpha=a/q
            for m in range(1,5*q):
                exact_zero=(m%q)==0
                exactly_resonant=((m*a)%q)==0
                assert exact_zero==exactly_resonant
                checks+=1
    print('VERIFIED',checks,'deterministic checks')
    h=2*pi/OMEGA
    print('example: gamma=',GAMMA,'omega=',OMEGA,'alpha=1/2','h=',h)
    print('covariance at resonant h:',stationarity(h,0.5))
    print('quadratic least eigenvalue coefficient:',near_resonance_coefficient(h,.5))


if __name__=='__main__':
    main()
