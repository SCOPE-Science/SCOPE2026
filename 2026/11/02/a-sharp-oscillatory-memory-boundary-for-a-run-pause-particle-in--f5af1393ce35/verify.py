#!/usr/bin/env python3
"""Reproducible independent algebra/ODE checks for a four-state active particle.
Only Python standard library is required. Finite tests complement, not prove,
the all-parameter theorem in RESULT.md.
"""
from fractions import Fraction as F
from math import cos, sin, cosh, sqrt, exp, pi, isclose, atan
import cmath

checks = 0

def check(test, reason):
    global checks
    checks += 1
    if not test:
        raise AssertionError(reason)


def generator(g, eta):
    plus = g*(1+eta)/2
    minus = g*(1-eta)/2
    return [
        [-g, g, F(0), F(0)],
        [plus, -g, minus, F(0)],
        [F(0), F(0), -g, g],
        [minus, F(0), plus, -g],
    ]


def mv(a, x):
    return [sum(a[i][j]*x[j] for j in range(len(x))) for i in range(len(x))]


def moments(b, g, v, eta):
    den=(b+g)**2-g**2*eta
    kr=v*(b+g)/(2*den)
    kt=g*kr/(b+g)
    c0=v*kr/b
    return kr, kt, c0


def ode_cov(t,b,g,v,eta):
    # Direct Taylor solution of the 3x3 moment ODE, independent of its spectral form.
    kr,kt,c0=moments(b,g,v,eta)
    z=[float(c0),float(kr),float(kt)]
    M=[[-float(b),float(v),0.0],[0.0,-float(g),float(g*eta)],[0.0,float(g),-float(g)]]
    steps=max(1,int(t/0.04)+1)
    h=t/steps
    for _ in range(steps):
        term=z[:]
        nxt=z[:]
        for k in range(1,28):
            term=[h*x/k for x in mv(M,term)]
            nxt=[x+y for x,y in zip(nxt,term)]
        z=nxt
    return z[0]


def analytical_cov(t,b,g,v,eta):
    b=float(b);g=float(g);v=float(v);eta=float(eta)
    den=(b+g)**2-g*g*eta
    kr=v*(b+g)/(2*den)
    if eta<0:
        w=g*sqrt(-eta)
        R=(1+1j*w/(b+g))/(b-g+1j*w)
        return v*kr*(exp(-b*t)/b+(R*(cmath.exp((-g+1j*w)*t)-exp(-b*t))).real)
    if eta==0:
        if isclose(b,g):
            return v*kr*exp(-b*t)*(1/b+t)
        return v*kr*(exp(-b*t)/b+(exp(-g*t)-exp(-b*t))/(b-g))
    w=g*sqrt(eta)
    # integrate two real decays analytically via elementary convolution
    roots=[g-w,g+w]
    weights=[(1+w/(b+g))/2,(1-w/(b+g))/2]
    out=exp(-b*t)/b
    for decay,weight in zip(roots,weights):
        diff=b-decay
        out+=weight*(t*exp(-b*t) if abs(diff)<1e-13 else (exp(-decay*t)-exp(-b*t))/diff)
    return v*kr*out


for g in [F(1,3),F(1),F(3,2),F(3)]:
    for eta in [F(-1),F(-3,4),F(-1,16),F(0),F(1,4),F(3,4)]:
        Q=generator(g,eta)
        qr=[F(1),F(0),F(-1),F(0)]
        qt=[F(0),F(1),F(0),F(-1)]
        for row in Q:
            check(sum(row)==0,'generator row sum')
            check(all(q>=0 for j,q in enumerate(row) if j!=Q.index(row)), 'off-diagonal rate')
        for j in range(4):
            check(sum(Q[i][j] for i in range(4))==0,'uniform stationarity')
        lqr=mv(Q,qr)
        lqt=mv(Q,qt)
        for j in range(4):
            check(lqr[j]==-g*qr[j]+g*eta*qt[j], 'odd block q_R')
            check(lqt[j]==g*qr[j]-g*qt[j], 'odd block q_T')
        for b in [F(1,4)*g,F(3,4)*g,g,F(5,4)*g,F(2)*g]:
            for v in [F(1,3),F(2)]:
                kr,kt,c0=moments(b,g,v,eta)
                check(-(b+g)*kr+g*eta*kt+v/2==0, 'stationary run moment')
                check(g*kr-(b+g)*kt==0, 'stationary tumble moment')
                check(-2*b*c0+2*v*kr==0, 'stationary squared position')
                check(c0>0, 'positive variance')
                for t in [0.0,0.1,0.4,1.,2.7,5.0]:
                    actual=ode_cov(t,b,g,v,eta)
                    expected=analytical_cov(t,b,g,v,eta)
                    check(abs(actual-expected)<=2e-9*max(1,abs(float(c0))),
                          f'ODE/spectral mismatch b={b} g={g} v={v} eta={eta} t={t}: {actual} {expected}')

# The coefficient of the real trap pole is strictly positive in the slow-trap regime.
for eta in [F(-1),F(-1,2),F(-1,25)]:
    for g in [F(1),F(5,2)]:
        w2=-g*g*eta
        for ratio in [F(1,5),F(1,2),F(9,10)]:
            b=ratio*g
            den=b*b-2*b*g+g*g+w2
            coeff=g*(-b*b+g*g+w2)/(b*(b+g)*den)
            check(coeff>0,'positive dominant real pole')

# Critical cases have exact alternating sign intervals.
for eta in [-1.,-0.25,-0.01]:
    g=1.;b=g;w=g*sqrt(-eta)
    C=lambda t: exp(-g*t)*((1+cos(w*t))/2+g*sin(w*t)/w)
    check(abs(C(pi/w))<1e-13,'critical first zero')
    check(C(0)>0,'critical zero lag')
    for n in range(4):
        a=(2*n+1.25)*pi/w
        z=(2*pi*(n+1)-atan(w/(2*g)))/w
        check(C(a)<0,'strict negative band')
        check(C(z)>0,'strict later positive band')

# For the fast trap, the nonzero complex residue has both oscillation signs.
for b in [1.25,2.,4.]:
    for eta in [-1.,-0.1]:
        g=1.;w=sqrt(-eta)
        R=(1+1j*w/(b+g))/(b-g+1j*w)
        check(abs(R)>1e-8,'nonvanishing oscillatory residue')
        for n in [4,8,12]:
            t_plus=(2*pi*n-cmath.phase(R))/w
            t_minus=t_plus+pi/w
            # Recompute after dividing by the positive factor e^{-gamma t}.
            def scaled(t):
                return (1/b-R.real)*exp(-(b-g)*t)+(R*cmath.exp(1j*w*t)).real
            check(scaled(t_plus)>0,'asymptotic positive sequence')
            check(scaled(t_minus)<0,'asymptotic negative sequence')

print(f'PASS {checks} exact-rational and numerical assertions')
