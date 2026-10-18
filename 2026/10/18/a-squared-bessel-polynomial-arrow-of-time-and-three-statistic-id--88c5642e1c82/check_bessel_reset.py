"""Independent symbolic, quadrature and Monte Carlo checks for a reset radial BESQ law."""
import math
import numpy as np
from scipy.integrate import quad
from scipy.special import kv, gamma
from numpy.random import default_rng
from sympy import symbols, diff, simplify

a, d, R = symbols('a d R', positive=True)
b = (1-2*a)*d/R**3
D = d/R**2
q = R**4/(8*d)
gen = lambda f: simplify(b*diff(f,R) + D*diff(f,R,2))
assert simplify(gen(q)-(2-a))==0
assert simplify(gen(q*q)-(2*(2-a)+4)*q)==0

rng=default_rng(220641)
checks=2
for alpha in (0.0,0.5,1.0):
    delta=2-alpha
    nu=delta/2
    for rate,t,u,v in ((1.7,.65,.4,.75),(.7,1.2,.25,.33)):
        n=250000
        age=rng.exponential(1/rate,n)
        q0=2*age*rng.gamma(nu,1,n)
        noreset=rng.random(n)<math.exp(-rate*t)
        qt=np.empty(n)
        idx=np.flatnonzero(noreset)
        qt[idx]=t*rng.noncentral_chisquare(df=delta,nonc=q0[idx]/t)
        other=np.flatnonzero(~noreset)
        # last-reset age conditioned on at least one reset in (0,t)
        aa=-np.log(1-rng.random(len(other))*(1-math.exp(-rate*t)))/rate
        qt[other]=2*aa*rng.gamma(nu,1,len(other))
        phi=lambda s: quad(lambda age: rate*math.exp(-rate*age)/(1+2*s*age)**nu,0,np.inf,epsabs=5e-12)[0]
        joint=math.exp(-rate*t)*(1+2*v*t)**(-nu)*phi(u+v/(1+2*v*t)) + phi(u)*quad(lambda a:rate*math.exp(-rate*a)/(1+2*v*a)**nu,0,t,epsabs=5e-12)[0]
        sampled=np.mean(np.exp(-u*q0-v*qt))
        assert abs(joint-sampled)<0.004,(alpha,rate,joint,sampled)
        checks+=1
        m=delta/rate
        var=delta*(delta+4)/rate**2
        assert abs(np.mean(q0)-m)/m<0.025
        assert abs(np.var(q0)-var)/var<0.06
        checks+=2
        # Inference on the exact population statistics, independent of simulation noise
        chi=var/m**2
        recovered_delta=4/(chi-1)
        recovered_rate=-math.log(math.exp(-rate*t))/t
        recovered_alpha=2-recovered_delta
        assert abs(recovered_delta-delta)<1e-12
        assert abs(recovered_rate-rate)<1e-12
        assert abs(recovered_alpha-alpha)<1e-12
        checks+=3
# Cross-check transformed stationary Bessel-K density against independent
# reset-age/Gamma mixture integral for all three conventions.
for alpha in (0.0,0.5,1.0):
    nu=(2-alpha)/2
    rate=1.9
    for qq in (0.09,0.6,3.0):
        # Integrate age mixture of fixed-age BESQ densities.
        mixture=quad(lambda a:rate*math.exp(-rate*a)*qq**(nu-1)*math.exp(-qq/(2*a))/(gamma(nu)*(2*a)**nu),0,np.inf,epsabs=1e-12)[0]
        z=math.sqrt(2*rate*qq)
        # The product-of-gamma density via Bessel K.
        density=2**((1-nu)/2)*rate**((1+nu)/2)*qq**((nu-1)/2)*kv(1-nu,z)/gamma(nu)
        assert abs(mixture-density)<1e-9,(alpha,qq,mixture,density)
        checks+=1
# Exact polynomial correlation directionality and triangularity in stationary law.
from sympy import exp, factor
rate, delta, lag, x = symbols('rate delta lag x', positive=True)
def moment(n):
    from sympy import rf, factorial
    return 2**n*factorial(n)*rf(delta/2,n)/rate**n
mu=moment(1)
var=simplify(moment(2)-mu**2)
a2=simplify((moment(3)-moment(2)*mu)/var)
b2=simplify(moment(2)-a2*mu)
P1=x-mu
P2=x**2-a2*x-b2
E=lambda f: simplify(sum(coef*moment((power[0])) for power,coef in __import__('sympy').Poly(f,x).terms()))
assert simplify(E(P1))==0
assert simplify(E(P2))==0
assert simplify(E(P1*P2))==0
assert simplify(E(P1**2)-var)==0
checks+=4
# A BESQ delta transition gives q -> q+delta*lag and
# q^2 -> q^2+ (2delta+4)lag*q + delta(delta+2)lag^2.
P0P1=x+delta*lag-mu
P0P2=x**2+(2*delta+4)*lag*x+delta*(delta+2)*lag**2-a2*(x+delta*lag)-b2
forward=simplify(E(P1*P0P2))
reverse=simplify(E(P2*P0P1))
assert simplify(reverse)==0
assert simplify(forward - 2*delta*(delta+2)*(delta+4)*lag/rate**2)==0
assert simplify(E(P2*P0P2)-E(P2**2))==0
checks+=3
print('CHECKS_PASS',checks)
