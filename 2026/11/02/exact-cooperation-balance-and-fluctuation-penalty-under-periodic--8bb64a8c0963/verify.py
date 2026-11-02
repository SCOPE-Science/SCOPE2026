#!/usr/bin/env python3
"""Reproduce algebraic and periodic-orbit checks for an eco-evolutionary game.

Scientific input: Jiang et al. (2022 preprint; 2023 journal), Eq. (9), with
its continuous extension at w=1. This checker is supplementary to the proof.
"""
from math import cos, pi
from fractions import Fraction
import numpy as np
import sympy as sp
from scipy.integrate import solve_ivp
from scipy.optimize import root


def algebra():
    x, theta, A, B = sp.symbols('x theta A B', real=True)
    assert sp.expand(x*(A-B) + (-x*A+theta*(1-x)*B)
                     - B*(theta-(theta+1)*x)) == 0
    J=sp.Matrix([[sp.Rational(1,12), sp.Rational(3,16)],
                 [-sp.Rational(8,45),-sp.Rational(1,10)]])
    f=sp.Matrix([sp.Rational(5,48),-sp.Rational(1,18)])
    assert sp.trace(J)==-sp.Rational(1,60)
    assert J.det()==sp.Rational(1,40)
    z=(sp.I*sp.eye(2)-J).inv()*f
    amplitude=sp.simplify(sp.re(z[0])**2+sp.im(z[0])**2)
    assert amplitude==sp.Rational(625,54772)
    assert sp.simplify(z[0]-(sp.Rational(25,13693)-sp.I*sp.Rational(2925,27386)))==0
    print('PASS exact algebra, Jacobian, forcing and quadratic coefficient', amplitude)


def direct_rhs(t, z, eta):
    x,r=z
    w=1+eta*cos(t)
    A=r*(1+w*x)/2-1
    B=x/2
    return [x*(1-x)*(A-B), 12*(r-1.5)*(1.8-r)*(-x*A+(1-x)*B)]


def quotient_payoff(w, x, r, rd, N):
    S=1+(w-1)*x
    if w==1:
        return r*(1+(N-1)*x)/N-1, rd*(N-1)*x/N
    return r*(w*S**(N-1)-1)/(N*(w-1))-1,rd*(S**(N-1)-1)/(N*(w-1))


def reconstruct_source_equations():
    for N in (2,3,4,6):
        for w in (.53,.77,1.,1.27,1.75):
            for x in (.15,.46,.83):
                A,B=quotient_payoff(w,x,1.67,1.,N)
                assert B>0
                if N==2:
                    assert abs(A-(1.67*(1+w*x)/2-1))<2e-14
                    assert abs(B-x/2)<2e-14
    print('PASS source quotient/continuous extension for N=2,3,4,6')


def orbit(eta):
    T=2*pi
    def period_map(z, dense=False):
        return solve_ivp(lambda t,y:direct_rhs(t,y,eta),(0,T),z,
                         rtol=3e-11,atol=1e-13,dense_output=dense,method='DOP853')
    fit=root(lambda z:period_map(z).y[:,-1]-z, [0.5,5/3], tol=1e-10)
    assert np.linalg.norm(period_map(fit.x).y[:,-1]-fit.x,np.inf)<1e-9
    sol=period_map(fit.x,True)
    assert sol.success
    times=np.linspace(0,T,20001)
    x,r=sol.sol(times)
    assert x.min()>0 and x.max()<1
    assert r.min()>1.5 and r.max()<1.8
    avg=np.trapezoid(x,times)/T
    avg2=np.trapezoid(x*x,times)/T
    var=avg2-avg*avg
    assert abs(avg2-avg/2)<2e-9
    assert 0<avg<0.5 and var>0
    gap=0.5-avg
    assert abs(gap-var/avg)<3e-9
    print(f'PASS eta={eta:.3f} mean={avg:.12f} var={var:.12g} ' 
          f'gap/eta^2={gap/eta**2:.12f}')
    return avg

if __name__=='__main__':
    algebra()
    reconstruct_source_equations()
    vals=[orbit(t) for t in (.03,.08,.16)]
    c=625/54772
    assert abs((.5-vals[0])/.03**2-c)<1e-5
    assert abs((.5-vals[1])/.08**2-c)<1e-5
    assert abs((.5-vals[2])/.16**2-c)<2e-5
    print('PASS finite-amplitude shooting and leading asymptotic coefficient')
