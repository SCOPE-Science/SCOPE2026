#!/usr/bin/env python3
"""Reproduce Hopf-coefficient algebra and the admissible two-speed example.

The exact coefficient is proved analytically in the accompanying mathematical text.
Numerical return-map checks corroborate signs but do not certify all parameters.
"""
from fractions import Fraction as F
from math import log, sqrt, pi, exp
import sympy as sp
from scipy.integrate import solve_ivp


def exact_symbolic_identity():
    X,Y,q,k,w,t,z,cubic = sp.symbols('X Y q k w t z cubic', real=True, nonzero=True)
    L = (X-w*Y+t*X*Y)/q
    # Taylor polynomial of sigmoid at its equilibrium value.
    f = sp.expand(q*L + (q*k/2)*L**2 + q*(1-6*q)*L**3/6-X+w*Y)
    f = sp.Poly(f, X, Y)
    f = sum(coeff*X**i*Y**j for (i,j),coeff in f.terms() if i+j <=3)
    g = z*X*Y + cubic*X*Y**2
    fd = lambda i,j: sp.diff(f,X,i,Y,j).subs({X:0,Y:0})
    gd = lambda i,j: sp.diff(g,X,i,Y,j).subs({X:0,Y:0})
    l1=(fd(3,0)+fd(1,2)+gd(2,1)+gd(0,3))/16
    l1+=(fd(1,1)*(fd(2,0)+fd(0,2))-gd(1,1)*(gd(2,0)+gd(0,2))
         -fd(2,0)*gd(2,0)+fd(0,2)*gd(0,2))/(16*w)
    # In the exact affine-payoff model t=-a*w/G and chi=k*a/G.
    chi=sp.symbols('chi',real=True)
    l1_with_relation=sp.factor(l1.subs(t,-chi*w/k).subs(q,(1-k*k)/4))
    target= -((2+chi)+(2-chi)*w*w)/(4*(1-k*k))
    assert sp.simplify(l1_with_relation-target)==0
    print('Symbolic cubic normal-form coefficient: PASS')


def rational_log_bracket():
    z=F(9,11)
    N=15
    lo=sum(F(2)*z**(2*j+1)/F(2*j+1) for j in range(N))
    hi=lo+F(2)*z**(2*N+1)/(F(2*N+1)*(1-z*z))
    assert F(23,10)<lo<hi<F(231,100)
    # All ensuing comparisons are rational, not floating-point assertions.
    Llo,Lhi=F(23,10),F(231,100)
    betalo=(22+9*Llo)/21
    nhlo=(209-30*Lhi)/(30*(22+9*Lhi))
    nhhi=(209-30*Llo)/(30*(22+9*Llo))
    assert F(108,1000)<nhlo<nhhi<F(110,1000)
    Klo=betalo*F(10,121)*6*F(108,1000)*F(890,1000)
    betahi=(22+9*Lhi)/21
    Khi=betahi*F(10,121)*6*F(110,1000)
    assert 40*Klo>F(121,41)
    assert Khi<F(121,41)
    print('Exact rational log bracket and 40-speed subcritical test: PASS')


def return_map_sign(eps):
    theta=0.1
    xstar=1/(1+theta)
    q=xstar*(1-xstar)
    beta=(22+9*log(10))/21
    nstar=(209-30*log(10))/(30*(22+9*log(10)))
    a,b,c,d=27,3,-30,-1
    P=beta*q*(a*xstar+c)
    Q=eps*(1+theta)*nstar*(1-nstar)
    w=sqrt(-P*Q)
    chi=81/20
    l1=-((2+chi)+(2-chi)*w*w)/(16*q)
    assert l1>0 if eps==40 else l1<0
    def rhs(t, state):
        x,n=state
        xi=beta*(a*x*n+b*x+c*n+d)
        sg=1/(1+exp(-xi))
        return [sg-x, eps*n*(1-n)*((1+theta)*x-1)]
    def section(t, state):
        return state[1]-nstar
    section.direction=1
    section.terminal=False
    ratios=[]
    for R in [0.004, 0.002]:
        sol=solve_ivp(rhs,[0,2.3*2*pi/w],[xstar+R,nstar],rtol=1e-12,atol=1e-13,
                      max_step=(2*pi/w)/250,events=section)
        crossings=[(t,xy) for t,xy in zip(sol.t_events[0],sol.y_events[0])
                   if t>0.4*(2*pi/w)]
        assert crossings
        T,z=crossings[0]
        estimate=(z[0]-xstar-R)/(T*R**3)
        ratios.append(estimate)
        assert estimate*l1>0, (eps,estimate,l1)
    print(f'epsilon={eps}: l1={l1:.8f}, return-map estimates {ratios}: PASS')


def main():
    exact_symbolic_identity()
    rational_log_bracket()
    return_map_sign(1)
    return_map_sign(40)
    print('ALL CHECKS PASSED')

if __name__=='__main__':
    main()
