"""Reproduce the occupation-fraction variance identity for threshold-restarted
natural-scale diffusion with generator |x|^(-alpha) d^2/dx^2.
Requires Python 3 and SymPy. This is a consistency checker, not an
independent proof or an exhaustive numerical verification.
"""
from fractions import Fraction
from math import isclose
import sympy as sp

q, s = sp.symbols('q s', positive=True)
eta = (1-s)/(2*(1-s**(q+1)))
theta = 1-eta
b = 1/(2*q*(q+1))

# Integrals of (1+sign*t)*(b-h*t**q/q)^2 over [lo, hi].
def antiderivative_interval(h, lo, hi, sign):
    terms = [(b*b, 0), (sign*b*b, 1),
             (-2*b*h/q, q), (-2*sign*b*h/q, q+1),
             (h*h/q**2, 2*q), (sign*h*h/q**2, 2*q+1)]
    return sum(c*(hi**(power+1)-lo**(power+1))/(power+1)
               for c, power in terms)

# 2 times killed Green integral of the squared Poisson-potential gradient.
cycle_moment = ((1-s) * (antiderivative_interval(theta, 0, 1, -1)
                       + antiderivative_interval(eta, 0, s, 1))
                + (1+s) * antiderivative_interval(eta, s, 1, -1))
claimed_cycle = 3*(1-s*s)/(4*(q+1)**2*(q+2)*(2*q+1))
assert sp.factor(cycle_moment-claimed_cycle) == 0
print('general symbolic identity: PASS')

# Check the normalization independently: u(s)=0 by centering.
D = q*(q+1)
u_at_restart = (2*eta-1+s-2*eta*s**(q+1))/(2*D)
assert sp.factor(u_at_restart) == 0
print('regenerative centering identity: PASS')

# Evaluate a second Poisson-potential representation
# 2 integral Green(x,y) g(y)u(y)|y|^(q-1)dy in exact rational arithmetic.
def integral_monomial_terms(lo, hi, terms):
    return sum(c*(hi**(power+1)-lo**(power+1))/Fraction(power+1)
               for c, power in terms)

def exact_rational_case(Q, R):
    E = (1-R)/(2*(1-R**(Q+1)))
    T = 1-E
    D0 = Fraction(Q*(Q+1))
    A0 = (2*E-1)/(2*D0)
    B0 = 1/(2*D0)
    # Negative half: t=-x from 0 to 1; g=-T and u(-t)=A0-B0*t+T*t^(Q+1)/D0.
    neg = integral_monomial_terms(Fraction(0),Fraction(1),[
        (-T*A0,Q-1), (T*(A0+B0),Q), (-T*B0,Q+1),
        (-T*T/D0,2*Q), (T*T/D0,2*Q+1)])
    # Positive half below reset level.
    lower = integral_monomial_terms(Fraction(0),R,[
        (E*A0,Q-1),(E*(A0+B0),Q),(E*B0,Q+1),
        (-E*E/D0,2*Q),(-E*E/D0,2*Q+1)])
    # Positive half above reset level.
    upper = integral_monomial_terms(R,Fraction(1),[
        (E*A0,Q-1),(E*(B0-A0),Q),(-E*B0,Q+1),
        (-E*E/D0,2*Q),(E*E/D0,2*Q+1)])
    observed = (1-R)*(neg+lower)+(1+R)*upper
    predicted = 3*(1-R*R)/Fraction(4*(Q+1)**2*(Q+2)*(2*Q+1))
    assert observed == predicted, (Q, R, observed, predicted)
    mean_tau = (1-R**(Q+1))/D0
    predicted_clt = 3*Q*(1-R*R)/(
        4*(Q+1)*(Q+2)*(2*Q+1)*(1-R**(Q+1)))
    assert observed/mean_tau == predicted_clt

count=0
for integer_q in range(1,19):
    for r in (Fraction(1,10),Fraction(1,3),Fraction(1,2),
              Fraction(2,3),Fraction(3,4),Fraction(9,10)):
        exact_rational_case(integer_q,r)
        count += 1
print(f'second-formula exact rational Green-moment cases: {count} PASS')

# For fractional exponents, numerical quadrature is supplementary, not a proof.
def simpson(fun, a, z, n=4096):
    h=(z-a)/n
    val=fun(a)+fun(z)
    for i in range(1,n):
        val+=(4 if i&1 else 2)*fun(a+i*h)
    return h*val/3

checks=0
for Q in (1.15,1.4,1.75,2.3,3.7,7.25):
    for R in (0.1,0.35,0.73,0.96):
        E=(1-R)/(2*(1-R**(Q+1)))
        T=1-E
        B=1/(2*Q*(Q+1))
        fn=lambda z,h: (B-h*z**Q/Q)**2
        v=(1-R)*(simpson(lambda z:(1-z)*fn(z,T),0,1)
                 +simpson(lambda z:(1+z)*fn(z,E),0,R))\
                +(1+R)*simpson(lambda z:(1-z)*fn(z,E),R,1)
        predicted=3*(1-R*R)/(4*(Q+1)**2*(Q+2)*(2*Q+1))
        assert isclose(v,predicted,rel_tol=5e-8,abs_tol=3e-9),(Q,R,v,predicted)
        checks+=1
print(f'fractional-exponent numerical quadratures: {checks} PASS')
print('All verification assertions passed.')
