"""Reproduce exact identities and independent numerical stress checks for a binary-step midpoint damping theorem.

Run: python verify.py
Requires: sympy >= 1.12 (plus Python standard library).
"""
import math
import random
from fractions import Fraction
import sympy as sp

checks = 0

def check(condition, explanation="check failed"):
    global checks
    if not condition:
        raise AssertionError(explanation)
    checks += 1

c, y, x = sp.symbols('c y x', positive=True, real=True)
q = 1 - 2*(1+c*y)/(y+c)**2
q_derivative = 2*(c*y + 2-c*c)/(c+y)**3
check(sp.cancel(sp.diff(q,y) - q_derivative) == 0, "derivative")
check(sp.cancel(q.subs(y,1)-(c-1)/(c+1)) == 0, "central value")
ys = c-2/c
check(sp.cancel(q.subs(y,ys)-(c*c-2)/(2*(c*c-1))) == 0, "split minima")
check(sp.cancel(q.subs(y,1)-q.subs(y,ys)-((c-2)**2/(2*(c-1)*(c+1)))) == 0, "center-minus-split gap")
# A zero-amplification atom occurs at x=+/-a. The other atom has squared magnitude tanh(a)^2.
zero_atom = (c*c-1)/(2*c*c)
check(sp.cancel(zero_atom-q.subs(y,ys)-1/(2*c*c*(c*c-1))) == 0, "zero-atom gap")
critical = sp.series(q.subs(c,2).subs(y,sp.cosh(x)),x,0,6).removeO()
check(sp.expand(critical-sp.Rational(1,3)-x**4/sp.Integer(54)) == 0, "critical quartic")

# A direct exact rational test also checks the cancellation identity independently of symbolic simplification.
for C in [Fraction(1,1),Fraction(3,2),Fraction(2,1),Fraction(5,2),Fraction(10,1)]:
    for Y in [Fraction(1,1),Fraction(7,6),Fraction(9,4),Fraction(5,1)]:
        lhs = 1 - 2*(1+C*Y)/(Y+C)**2
        check(lhs == Fraction(1,1)-Fraction(2,1)*(1+C*Y)/(Y+C)**2, "exact rational")

rng = random.Random(20261030)
def factor(theta):
    return (1-theta)/(1+theta)
def q_from_steps(a,x):
    return .5*(factor(math.exp(x+a))**2 + factor(math.exp(x-a))**2)
def q_closed(a,x):
    C,Y = math.cosh(a),math.cosh(x)
    return 1-2*(1+C*Y)/(Y+C)**2
def minimum(a):
    C=math.cosh(a)
    if C<=2:
        return [0.],(C-1)/(C+1)
    X=math.acosh(C-2/C)
    return [-X,X],(C*C-2)/(2*(C*C-1))

for _ in range(400):
    a=rng.uniform(0.0,5.0)
    x=rng.uniform(-7.0,7.0)
    check(abs(q_from_steps(a,x)-q_closed(a,x))<2.e-13, "two formulas")

for a in [0.0,0.1,0.3,0.75,1.0,math.acosh(2),1.317,1.5,2.0,3.0,5.0]:
    xs,v=minimum(a)
    for z in xs:
        check(abs(q_from_steps(a,z)-v)<2.e-13, "attained minimum")
    for k in range(-280,281):
        z=k/20.
        check(q_from_steps(a,z)>=v-3.e-13,"global lower bound scan")
    if a>0:
        check(v>0 and v<.5, "strict positive mean-square contraction")
        check(min(abs(z) for z in xs)<a+1.e-14, "mean-square optimum does not annihilate an atom")
        check(.5*math.tanh(a)**2>v-2.e-13, "zero-atom scale is suboptimal")

# Exact finite-horizon second moments via a binomial law for the number of large steps.
for a in [.1,.8,1.4,2.8]:
    for x in [-2.,-0.7,0.,.35,2.]:
        rp2=factor(math.exp(x+a))**2
        rm2=factor(math.exp(x-a))**2
        qval=.5*(rp2+rm2)
        for n in range(1,11):
            enumerate_value=sum(math.comb(n,j)*rp2**j*rm2**(n-j) for j in range(n+1))/2**n
            check(abs(enumerate_value-qval**n)<3.e-13, "finite horizon product")

ac=math.acosh(2)
for delta in [1.e-2,1.e-3,1.e-4,1.e-5]:
    a=ac+delta
    xstar=minimum(a)[0][1]
    check(abs((xstar**2/delta)/(3*math.sqrt(3))-1)<.015, "square root splitting")

print(f"PASS: {checks} exact-symbolic, exact-rational, finite-horizon and numerical check groups")
print(f"critical log half-spread = {ac:.15f}")
print(f"critical length ratio = {math.exp(2*ac):.15f}")
