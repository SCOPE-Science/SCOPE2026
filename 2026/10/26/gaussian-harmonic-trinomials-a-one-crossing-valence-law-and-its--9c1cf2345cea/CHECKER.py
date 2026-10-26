"""Reproducible independent numerical checks for the Gaussian harmonic-binomial transition theorem.
Requires Python 3 with numpy and scipy. Run: python CHECKER.py.
The numerical tests support but do not replace the analytic proof.
"""
import math
import numpy as np
from scipy.integrate import quad
from scipy.special import gamma

TOL = 2.0e-7

def radial_data(n,u):
    q=n/(n-1)
    r=n**(-1/(n-1))
    h=n*n+2*n*math.cos(u)+1
    rho=r*math.sqrt(h)/n
    jac=n*(n-1)*(1-math.cos(u))/h
    return rho,jac

def angular_avg(n, fn):
    return quad(lambda u: radial_data(n,u)[1]*fn(radial_data(n,u)[0]),
        0, 2*math.pi, epsabs=8e-11, epsrel=8e-11, limit=250)[0]/(2*math.pi)

def area_and_inertia(n):
    r=n**(-1/(n-1))
    A=math.pi*r*r*(1-1/n)
    I=math.pi*r**4/2*(1-2*(n-1)/n**2-1/n**3)
    return A,I

def p_exact(n,s):
    q=n/(n-1)
    # integrate the Rayleigh density over a radially scaled hypocycloid,
    # writing |A|^2=x and B-inclusion probability via the radial function.
    def integrand(x):
        t=s**q*x**(q/2)
        return math.exp(-x)*angular_avg(n,lambda rho: -math.expm1(-(t*rho)**2))
    return quad(integrand, 0, 48, epsabs=4e-9, epsrel=4e-9, limit=130)[0]

def p_alt(n,s):
    q=n/(n-1)
    def integrand(u):
        rho,jac=radial_data(n,u)
        return jac*quad(lambda x: math.exp(-x-(x**(1/q))/(s*s*rho**(2/q))),0,48,
            epsabs=6e-10,epsrel=6e-10,limit=160)[0]
    return quad(integrand,0,2*math.pi,epsabs=5e-9,epsrel=5e-9,limit=150)[0]/(2*math.pi)

def weak_coeff(n):
    q=n/(n-1)
    area,inertia=area_and_inertia(n)
    return area/math.pi*gamma(1+q),inertia/math.pi*gamma(1+2*q)

def strong_coeff(n):
    q=n/(n-1)
    return (gamma(1+1/q)*angular_avg(n,lambda rho:rho**(-2/q)),
            gamma(1+2/q)*angular_avg(n,lambda rho:rho**(-4/q)))

checks=0
for n in (2,3,4,7,18):
    q=n/(n-1)
    r=n**(-1/(n-1))
    assert abs(angular_avg(n,lambda rho: 1)-1)<TOL; checks+=1
    assert abs(angular_avg(n,lambda rho:rho*rho)-area_and_inertia(n)[0]/math.pi)<TOL; checks+=1
    assert abs(angular_avg(n,lambda rho:rho**4)/2-area_and_inertia(n)[1]/math.pi)<TOL; checks+=1
    # A positively oriented star-shaped disk obeys area = (1/2) int rho(theta)^2 dtheta.
    assert abs(angular_avg(n,lambda rho:rho*rho)-area_and_inertia(n)[0]/math.pi)<TOL; checks+=1
    for s in (0.75, 1.3):
        p1=p_exact(n,s)
        p2=p_alt(n,s)
        assert abs(p1-p2)<3e-7,(n,s,p1,p2)
        assert 0<p1<1
        checks+=2
    c,d=strong_coeff(n)
    a,b=weak_coeff(n)
    assert min(a,b,c,d)>0
    checks+=1
    print('n=',n,'p(.75)=',round(p_exact(n,.75),9),'p(1.3)=',round(p_exact(n,1.3),9),
          'weak=',tuple(round(x,8) for x in (a,b)),
          'strong=',tuple(round(x,8) for x in (c,d)))

# For n=2: coefficients (1/4,9/32) are closed form.
a,b=weak_coeff(2)
assert abs(a-1/4)<1e-12 and abs(b-9/32)<1e-12
checks+=1
for n in (20,60,150):
    val=p_alt(n,1.0)
    print('degree',n,'p(1)=',val,'target 1/2')
    assert abs(val-0.5)<0.12
    checks+=1
print('Passed',checks,'quadrature, coefficient and asymptotic consistency checks.')

# The refined large-degree correction is independent of which hypocycloid
# cusp is used to parameterize the boundary.
EULER_GAMMA = 0.5772156649015328606
for n in (40,100,250):
    for s in (0.7,1.0,1.4):
        value=p_alt(n,s)
        first=s*s/(1+s*s)
        second=first-s*s/(n*(1+s*s)**2)*(2*math.log(n)+EULER_GAMMA+math.log1p(1/(s*s)))
        delta=value-second
        assert abs(delta)<0.0035,(n,s,value,second,delta)
        checks+=1
        print('asymptotic',n,s,'observed',round(value,9),'two-term',round(second,9),'residual',round(delta,9))
print('Total passed assertions:',checks)

# Actual nonlinear-zero checks for regular targets on both sides of the caustic.
# The root finder is corroborative only; the analytic degree argument is the proof.
from scipy.optimize import root

def numerical_zero_count(n, coeff, target):
    roots=[]
    def f(v):
        z=complex(v[0],v[1])
        w=z**n+coeff*z.conjugate()+target
        return [w.real,w.imag]
    seeds=np.linspace(-1.8,1.8,13)
    for u in seeds:
        for v in seeds:
            sol=root(f,[u,v],tol=1e-11)
            if sol.success and np.linalg.norm(f(sol.x))<1e-8:
                z=complex(*sol.x)
                if all(abs(z-r)>1e-5 for r in roots):
                    roots.append(z)
    return len(roots)
for n in (2,3,4):
    for coeff,target,expected in [
        (complex(0.8,0.6), complex(0.15,0.08), n+2),
        (0.1*complex(0.8,0.6), complex(0.4,0.2), n)]:
        observed=numerical_zero_count(n,coeff,target)
        assert observed==expected,(n,coeff,target,observed,expected)
        checks+=1
print('Total passed assertions including direct zero counts:',checks)
