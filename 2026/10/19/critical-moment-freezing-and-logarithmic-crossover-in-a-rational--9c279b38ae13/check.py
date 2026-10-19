"""Exact identities and high-precision spot checks for stationary endpoint scaling.
This is a finite consistency checker, not a substitute for the proof in RESULT.md.
"""
from fractions import Fraction
from math import comb
import sympy as sp
import mpmath as mp
mp.mp.dps = 45

def alpha_sym(N):
    t=sp.symbols('t')
    numerator=sum(sp.binomial(N,2*k+1)*t**k for k in range((N-1)//2+1))
    denominator=sum(sp.binomial(N,2*k)*t**k for k in range(N//2+1))
    return sp.factor(numerator/denominator)

for N in range(2,13):
    t=sp.symbols('t')
    expr=alpha_sym(N)
    K=sp.Rational(N*(N*N-1),3)
    assert sp.limit(expr,t,0)==N
    assert sp.limit((N-expr)/t,t,0)==K


def aN(N,beta):
    b=mp.mpf(beta)
    top=mp.fsum(mp.mpf(comb(N,2*k+1))*b**(-k) for k in range((N-1)//2+1))
    bot=mp.fsum(mp.mpf(comb(N,2*k))*b**(-k) for k in range(N//2+1))
    return top/bot

def moment(q,beta):
    B=mp.mpf(beta);q=mp.mpf(q)
    # U=tan(theta) is standard positive half-Cauchy
    f=lambda theta:(mp.tan(theta)**2/(B+mp.tan(theta)**2))**q
    return (mp.mpf(2)/mp.pi)*mp.quad(f,[0,mp.pi/4,mp.pi/2])

for B in (mp.mpf('10000'),mp.mpf('1000000')):
    assert mp.almosteq(moment(1,B),1/(1+mp.sqrt(B)),rel_eps=mp.mpf('1e-27'))
    for q in (mp.mpf('0.20'),mp.mpf('0.50'),mp.mpf('0.80')):
        v=moment(q,B)
        if q < mp.mpf('.5'): target=B**(-q)/mp.cos(mp.pi*q)
        elif q==mp.mpf('.5'): target=mp.log(B)/(mp.pi*mp.sqrt(B))
        else: target=mp.gamma(q-mp.mpf('.5'))/(mp.sqrt(mp.pi)*mp.gamma(q)*mp.sqrt(B))
        assert mp.mpf('.75')<v/target<mp.mpf('1.25'),(B,q,v/target)
    for s in (-2,0,2):
        L=mp.log(B)
        q=mp.mpf('.5')+mp.mpf(s)/L
        target=(1-mp.exp(-s))/s if s else 1
        ratio=mp.pi*mp.sqrt(B)*moment(q,B)/L
        assert abs(ratio-target)<mp.mpf('.60'),(B,s,ratio,target)

# Direct deterministic integrals of the published invariant density against
# two polynomial observables, before and after one iteration.
def f_N(N,b,x):
    a=aN(N,b)
    v=mp.chebyt(N,mp.sqrt(x))**2
    return a*a*v/(1+(a*a-1)*v)
for N in (2,3,5):
    b=mp.mpf(3)
    for degree in (1,2):
        value=mp.quad(lambda theta: (b/(b+mp.tan(theta)**2))**degree,[0,mp.pi/2])*2/mp.pi
        image=mp.quad(lambda theta: f_N(N,b,b/(b+mp.tan(theta)**2))**degree,[0,mp.pi/2])*2/mp.pi
        assert abs(value-image)<mp.mpf('1e-20'),(N,degree,value,image)
print('VERIFY_OK')
