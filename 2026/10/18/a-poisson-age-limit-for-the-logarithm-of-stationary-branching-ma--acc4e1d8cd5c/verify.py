"""Numerical consistency checks for a rare-immigration CBI logarithmic limit."""
import math
from scipy.integrate import quad

def csbp_laplace_u(alpha, age, theta):
    # Stable calculation for the parameter ranges used here.
    z = math.expm1((1-alpha)*math.log1p(theta))
    return (1+math.exp(-age)*z)**(1/(1-alpha)) - 1

def laplace_youngest(alpha, age, theta):
    return 1/(1+math.exp(-age)*math.expm1((1-alpha)*math.log1p(theta)))

def laplace_conditional(alpha, age, theta):
    return laplace_youngest(alpha, age, theta)**(1/(1-alpha))

checks=0
for alpha in [.03,.07,.16,.3,.5,.8,.94]:
    lam=alpha/(1-alpha)
    for theta in [.025,.25,1,3,12,50]:
        val,err =quad(lambda y: lam*(y**(lam-1))*(1+y*((1+theta)**(1-alpha)-1))**(-1/(1-alpha)), 0,1, epsabs=3e-11, epsrel=3e-11, limit=500)
        expected=(1+theta)**(-alpha)
        assert abs(val-expected)<max(1e-8,30*err),(alpha,theta,val,expected,err)
        checks+=1
    for age in [.0,.25,1,2,4]:
        for theta in [.01,.1,.5,2,15]:
            u=csbp_laplace_u(alpha,age,theta)
            calc=(1+u)**(-(1-alpha))
            assert abs(calc-laplace_youngest(alpha,age,theta))<3e-13
            checks+=1
    # Independent finite-difference approximations of the conditional first moment.
    for h in [2e-5,5e-5,1e-4,2e-4]:
        for age in [.0,.5,2]:
            derivative=(laplace_conditional(alpha,age,h/2) - laplace_conditional(alpha,age,2*h))/(1.5*h)
            assert abs(derivative-math.exp(-age))<6e-4, (alpha,age,derivative)
            checks+=1
    assert abs(lam/(lam+1)-alpha)<1e-14
    checks+=1
print('PASS',checks,'numerical consistency assertions')
