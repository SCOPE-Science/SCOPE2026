#!/usr/bin/env python3
"""Independent exact moment and Fourier checks of a two-state intermittent harmonic diffusion."""
from fractions import Fraction as F
from math import factorial, exp, cos, log, sqrt, pi
from scipy.integrate import quad


def phi(k, alpha, beta, mu, diffusion):
    power = alpha/(2*mu)
    return exp(-diffusion*k*k/(2*mu)) * (1+diffusion*k*k/(alpha+beta)) / (1+diffusion*k*k/beta)**(1+power)


def generator_moments(alpha,beta,mu,diffusion,nmax):
    on = beta/(alpha+beta)
    off = alpha/(alpha+beta)
    moments=[on+off]
    for n in range(1,nmax+1):
        new_on=(2*n-1)*diffusion*(on+off)/mu
        new_off=(alpha*new_on+2*n*(2*n-1)*diffusion*off)/beta
        on,off=new_on,new_off
        moments.append(on+off)
    return moments


def fourier_moments(alpha,beta,mu,diffusion,nmax):
    a=alpha/(2*mu)
    l=[F(0)]*(nmax+1)
    for j in range(1,nmax+1):
        l[j]=((-1)**j)*((1+a)*(diffusion/beta)**j-(diffusion/(alpha+beta))**j)/j
    l[1]-=diffusion/(2*mu)
    coefficients=[F(1)]+[F(0)]*nmax
    for n in range(1,nmax+1):
        coefficients[n]=sum(j*l[j]*coefficients[n-j] for j in range(1,n+1))/n
    return [(-1)**n*factorial(2*n)*coefficients[n] for n in range(nmax+1)]

assertions=0
for alpha,beta,mu,diffusion in [(F(1),F(1),F(1),F(1)),(F(1),F(1,2),F(1),F(3,2)),(F(1),F(4,5),F(1),F(1)),(F(2,3),F(5,2),F(4,3),F(3,4)),(F(3),F(1,5),F(1,2),F(2))]:
    from_generator=generator_moments(alpha,beta,mu,diffusion,8)
    from_fourier=fourier_moments(alpha,beta,mu,diffusion,8)
    for n,(g,f) in enumerate(zip(from_generator,from_fourier)):
        assert g==f,(alpha,beta,mu,diffusion,n,g,f)
        assertions+=1

for alpha,beta,mu,diffusion in [(1.,1.,1.,1.),(1.,.5,1.,1.),(1.,.8,1.,1.),(2.,2.5,.75,1.25)]:
    a=alpha/(2*mu)
    c=sqrt(beta/diffusion)
    d=sqrt((alpha+beta)/diffusion)
    sigma2=diffusion/mu
    threshold=beta*(4*mu+alpha)-4*mu*mu
    for k in [.2,.7,1.5,2.4]:
        integral=quad(lambda x: 2*(cos(k*x)-1)*((a+1)*exp(-c*x)-exp(-d*x))/x if x else 0.0,0,80,maxp1=400,epsabs=2e-12)[0]
        calc=-sigma2*k*k/2+integral
        assert abs(log(phi(k,alpha,beta,mu,diffusion))-calc)<2e-10,(alpha,beta,mu,diffusion,k,calc)
        assertions+=1
        # direct transformed background-driving exponent equals the characteristic logarithm.
        chi=lambda z: -sigma2*z*z -2*(a+1)*z*z/(c*c+z*z)+2*z*z/(d*d+z*z)
        ou=quad(lambda t: chi(k*exp(-t)),0,40,epsabs=3e-12)[0]
        assert abs(ou-log(phi(k,alpha,beta,mu,diffusion)))<1e-10
        assertions+=1
    q0=(a+1)*c-d
    assert (q0>=-1e-12)==(threshold>=-1e-12)
    assertions+=1
    if threshold>=0:
        for x in [0,.001,.01,.1,.5,1,3,6,10]:
            q=(a+1)*c*exp(-c*x)-d*exp(-d*x)
            assert q>=-3e-13,(alpha,beta,mu,x,q)
            assertions+=1
    else:
        assert q0<0
        assertions+=1

# Published equal-switching formula is recovered exactly by the general expression.
for gamma,mu,diffusion,k in [(0.25,1,1,.7),(2,1.5,3,2),(1.5,.5,2,.6)]:
    published=exp(-diffusion*k*k/(2*mu))*(1+diffusion*k*k/gamma)**(-gamma/(2*mu)-1)*(1+diffusion*k*k/(2*gamma))
    assert abs(phi(k,gamma,gamma,mu,diffusion)-published)<1e-14
    assertions+=1
print(f'PASS: {assertions} exact rational moments / spectral quadrature / background-driving / boundary assertions')
