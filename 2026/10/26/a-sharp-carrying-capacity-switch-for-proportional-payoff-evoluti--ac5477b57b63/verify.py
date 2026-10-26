"""Exact and numerical checks for a proportional-payoff eco-evolutionary game."""
from fractions import Fraction
from math import atan, exp, log, sqrt
import sympy as sp
from scipy.integrate import solve_ivp
from scipy.optimize import brentq

x,R,S,T,P=sp.symbols('x R S T P', real=True)
a=T-R
b=P-S
d=b+(a-b)*x
W=sp.expand(R*x**2+(S+T)*x*(1-x)+P*(1-x)**2)
A=P/b
B=R/a
E=1+B-A
integrand=A/x+B/(1-x)+E*(a-b)/d
assert sp.factor(integrand-W/(x*(1-x)*d))==0
print('general_partial_fraction_identity: OK')

m={R:3,S:1,T:4,P:2}
assert sp.expand(W.subs(m))==x+2
assert sp.expand(d.subs(m))==1
Phi=lambda z:z*z/(1-z)**3
x0=0.75
N0=1.0
xc=0.5
Kc=Phi(x0)/Phi(xc)*N0
assert Kc==18
assert sp.simplify(sp.Rational(3,4)**2/(1-sp.Rational(3,4))**3)==36
print('critical_capacity: Kc=18')

# Critical resource change follows a convergent integral after cancellation.
XX=sp.symbols('XX', real=True)
Nofx=36*(1-XX)**3/XX**2
G=sp.factor((2*XX-1)/(XX*(1-XX)*(1-Nofx/18)))
assert sp.simplify(G-XX/((1-XX)*(XX**2-2*XX+2)))==0
J=log(2)+.5*log(17/20)-atan(2/9)
quad=sp.simplify(sp.integrate(G,(XX,sp.Rational(1,2),sp.Rational(3,4))))
assert abs(float(quad)-J)<1e-13
L=exp(J)
nstar=(4*L+1-sqrt(8*L+1))/(4*L)
assert 0.5<nstar<1
assert abs(.5*log(nstar)-log(1-nstar)-(.5*log(.5)-log(.5))-.5*J)<1e-12
print(f'critical_resource: integral={J:.12f}, n_infty={nstar:.12f}')

def rhs(t,z,K):
    N,xx,n=z
    h=.5+.5*n
    q=1-N/K
    W=2+xx
    return (N*q*h*W, -q*h*xx*(1-xx), .5*(2*xx-1)*n*(1-n))

for K in [12,18,30]:
    sol=solve_ivp(lambda t,z:rhs(t,z,K),(0,600),[1,.75,.5],rtol=1e-11,atol=1e-13)
    assert sol.success
    N,xx,n=sol.y[:,-1]
    target=brentq(lambda t:K*Phi(t)-36, .0001,.9999,xtol=1e-14)
    assert abs(N-K)<2e-7
    assert abs(xx-target)<2e-8
    assert abs(N*Phi(xx)-36)<3e-7
    if K<Kc:
        assert n>1-1e-9
    elif K>Kc:
        assert n<1e-9
    else:
        assert abs(n-nstar)<2e-8
    print(f'ODE K={K}: x={xx:.12f}, n={n:.12f}, invariant={N*Phi(xx):.10f}')
print('VERIFICATION_OK')
