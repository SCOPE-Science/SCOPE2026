"""Standalone exact and numerical checks for the critical cost-face cycles.

Requires Python 3.10+, sympy, scipy. Tests supplement—not replace—the proof.
"""
import math
from fractions import Fraction
from math import comb

import sympy as sp
from scipy.integrate import solve_ivp, quad


def test_identity(N, M, B, mu, c0):
    x, r = sp.symbols('x r', positive=True)
    B, mu, c0 = [sp.Rational(q) for q in (B, mu, c0)]
    p = sp.Rational(M - 1, N - 1)
    Q = comb(N - 1, M - 1) * x**(M - 1) * (1 - x)**(N - M)
    kappa = (N - 1) * c0 / mu
    R = ((1-r) / r)**kappa
    C = (N-1)*B/mu
    # These are the exact derivatives of H defined by its one-dimensional integral.
    Hx = -R * sp.diff(Q, x) / Q**2
    Hr = R / (1-r) * (C - kappa / (r * Q))
    fx = x*(1-x)*(B*r*Q-c0)
    gr = mu*r*(1-r)*(p-x)
    identity = sp.factor(Hx*fx+Hr*gr)
    assert identity == 0, (N, M, identity)
    qstar = Q.subs(x, p)
    rstar = c0 / (B * qstar)
    assert 0 < rstar < 1
    A = sp.factor((x*(1-x)*B*Q).subs(x,p))
    D = mu*rstar*(1-rstar)
    frequency_sq = sp.factor(A*D)
    assert sp.simplify(frequency_sq - mu*c0*p*(1-p)*(1-rstar)) == 0
    hxx = sp.simplify((-R*sp.diff(Q,x,2)/Q**2).subs({x:p,r:rstar}))
    hrr = sp.simplify((R*kappa/(Q*r**2*(1-r))).subs({x:p,r:rstar}))
    assert hxx > 0 and hrr > 0
    return float(rstar),float(frequency_sq)


def test_cycles(c0):
    N,M,B,mu,alpha,beta=3,2,10.,2.,2.,1.
    p=.5
    q=lambda x:2*x*(1-x)
    rstar=c0/(B*q(p))
    kappa=(N-1)*c0/mu
    C=(N-1)*B/mu
    theta1,theta2,theta3,theta4=2.,1.,1.,7./8.
    G=lambda x,r:theta1-theta4-(theta1+theta2)*x+(theta3+theta4)*r
    def flow(t,y):
        x,r,ix,ir,irq,ig=y
        return [x*(1-x)*(B*r*q(x)-c0),mu*r*(1-r)*(p-x),x,r,r*q(x),G(x,r)]
    def event(t,y): return y[0]-p
    event.direction=1
    event.terminal=False
    omega2=mu*c0*p*(1-p)*(1-rstar)
    T0=2*math.pi/math.sqrt(omega2)
    y0=[p,rstar+.03,0.,0.,0.,0.]
    sol=solve_ivp(flow,(0,2.5*T0),y0,events=event,rtol=2e-12,atol=2e-14,dense_output=True,max_step=.025)
    roots=sol.t_events[0]
    full=[t for t in roots if t>1.0]
    assert full, (c0,roots)
    T=full[0]
    y=sol.sol(T)
    assert abs(y[0]-p)<1e-9 and abs(y[1]-y0[1])<1e-9
    xbar=y[2]/T; rbar=y[3]/T; rqbar=y[4]/T; gbar=y[5]/T
    assert abs(xbar-p)<1e-10
    assert abs(rqbar-c0/B)<1e-10
    assert rbar-rstar>0
    assert abs(gbar-G(p,rstar)-(theta3+theta4)*(rbar-rstar))<1e-10
    sigma=1 if c0==beta else -1
    exponent=sigma*(alpha-beta)*gbar
    assert (exponent>0 if sigma==1 else exponent<0)
    # For integer kappa, the integral defining the first integral is elementary:
    # kappa=1: log(r/r*); kappa=2: -1/r-2log(r)+r terms? compute numerically safely.
    def invariant(x,r):
        J=quad(lambda s:s**(-kappa)*(1-s)**(kappa-1),rstar,r,epsabs=1e-12)[0]
        return ((1-r)/r)**kappa/q(x)+C*J
    H0=invariant(y0[0],y0[1]); Ht=invariant(y[0],y[1]);
    assert abs(Ht-H0)<1e-8
    print(f'face_cost={c0:g} period={T:.9f} linear_period={T0:.9f} mean_x={xbar:.12f} '
          f'mean_r={rbar:.12f} equilibrium_r={rstar:.12f} avg_G={gbar:.10f} '
          f'log_Floquet_over_T={exponent:.10f} conserved_H_error={abs(Ht-H0):.3g}')


def main():
    for args in [(3,2,10,2,1),(3,2,10,2,2),(5,3,12,4,1),(8,5,20,3,1)]:
        print('exact',args,test_identity(*args))
    test_cycles(1.)
    test_cycles(2.)
    print('ALL VERIFICATION CHECKS PASS')

if __name__=='__main__': main()
