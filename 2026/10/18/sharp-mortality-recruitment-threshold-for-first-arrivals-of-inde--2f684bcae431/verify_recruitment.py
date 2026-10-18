"""Deterministic numerical consistency checks for killed Brownian immigration.

Requires Python 3, numpy, scipy. Run: python verify_recruitment.py.
Finite checks corroborate, but do not establish, the limiting theorem.
"""
import math
from scipy.integrate import quad
from scipy.special import erfc

checks=0
def verify(condition, message):
    global checks
    if not condition:
        raise AssertionError(message)
    checks+=1

def f(t):
    return 0.0 if t<=0.0 else math.exp(-1/(4*t))/(2*math.sqrt(math.pi)*t**1.5)

def cumulative(t, b):
    v=math.sqrt(b)
    return (math.exp(-v)*erfc(1/(2*math.sqrt(t))-math.sqrt(b*t))+
            math.exp(v)*erfc(1/(2*math.sqrt(t))+math.sqrt(b*t)))/2

def A(t,b):
    return quad(lambda u:(t-u)*math.exp(-b*u)*f(u),0,t,
                epsabs=2e-13,epsrel=2e-12,limit=400)[0]

def HA(L,c,x):
    """R*A_b(x/L), b=c^2 L^2, L=log R, with exponent cancellation."""
    F=lambda y:1/(4*y)+c*c*y
    fx=F(x)
    def integrand(z):
        y=x-z/L
        return z*y**(-1.5)*math.exp(-L*(F(y)-fx)) if y>0 else 0.0
    limit=min(L*x,120.0)
    integral=quad(integrand,0,limit,epsrel=5e-12,epsabs=2e-12,limit=400)[0]
    return math.exp(L*(1-fx))*integral/(2*math.sqrt(math.pi)*L**2.5)

def h(c):return 1/(2*(1+math.sqrt(1-c*c)))
def slope(c):
    t=h(c)
    return 1/(4*t*t)-c*c

def constant(c):
    return 1/(2*math.sqrt(math.pi)*h(c)**1.5*slope(c)**2)

# Independent Fubini evaluations of the same Poisson arrival exponent.
for b in [0,0.5,1,4]:
    for t in [.1,.3,1.,2.]:
        lhs=A(t,b)
        rhs=quad(lambda z:cumulative(z,b),0,t,epsabs=1e-12,epsrel=1e-11)[0]
        verify(abs(lhs-rhs)<1e-10*(1+lhs),f'Fubini {b},{t}')
        verify(-1e-12<=lhs<=t*math.exp(-math.sqrt(b))+1e-12,f'bound {b},{t}')
        verify(0<=cumulative(t,b)<=math.exp(-math.sqrt(b))+1e-12,f'CDF {b},{t}')

# Laplace-transform identities and conditional mean length.
for b in [.25,1.,4.,9.]:
    q=quad(lambda z:math.exp(-b*z)*f(z),0,math.inf,epsabs=1e-12)[0]
    m=quad(lambda z:z*math.exp(-b*z)*f(z),0,math.inf,epsabs=1e-12)[0]
    verify(abs(q-math.exp(-math.sqrt(b)))<2e-10,f'Laplace {b}')
    verify(abs(m/q-1/(2*math.sqrt(b)))<2e-10,f'conditional mean {b}')

# Exact threshold root, simple saddle and explicit Gumbel normalization.
for c in [0.,.5,.9]:
    t=h(c); a=slope(c);C=constant(c)
    verify(abs(1/(4*t)+c*c*t-1)<1e-12,f'root {c}')
    verify(a>0 and C>0,f'positive scale {c}')
    errors=[]
    for L in [100.,300.,1000.]:
        x=t+(2.5*math.log(L)-math.log(C))/(a*L)
        hazard=HA(L,c,x)
        verify(0<hazard<1, f'Gumbel-centering hazard {c},{L}: {hazard}')
        errors.append(abs(math.log(hazard)))
    verify(errors[2]<errors[1]<errors[0],f'centering convergence {c}')
    verify(HA(1000,c,.8*t)<1e-3,f'below cutoff {c}')
    verify(HA(1000,c,1.4*t)>100,f'above cutoff {c}')

# Shifted high-mortality success arrivals: exact delay inequality.
for b in [4.,9.,16.,25.]:
    q=math.exp(-math.sqrt(b)); conditional_mean=1/(2*math.sqrt(b))
    for t in [.5,1.,3.]:
        arrival=A(t,b)/q
        verify(t-conditional_mean-1e-10<=arrival<=t+1e-10,
               f'finite delay bound {b},{t}')

print(f'PASS: {checks} deterministic checks (not an infinite proof)')
