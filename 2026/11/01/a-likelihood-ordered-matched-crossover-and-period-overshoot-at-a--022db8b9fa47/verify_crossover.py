"""Reproducibility checks for a matched quintic global-center period limit.

Run: python verify_crossover.py (requires scipy and sympy).
The tests supplement, but do not replace, the proof in RESULT.md.
"""
import math
from scipy.integrate import quad
from scipy.special import beta
from sympy import symbols, exp, diff, simplify

x, y, alpha, b = symbols('x y alpha b', real=True)
p2 = exp(alpha*x**4/2)
# H = (p2*y*y)/2 + integral(p2*(x+b*x**5),x)
H_x = diff(p2, x)*y**2/2 + p2*(x+b*x**5)
H_y = p2*y
assert simplify(H_x*y+H_y*(-x-alpha*x**3*y**2-b*x**5)) == 0

def J(q,t,delta=0):
    return 2*quad(lambda s:math.exp(q*s**4/2)*(s**5+delta*s),t,1,
                  epsabs=3.e-12)[0]

def C(q,delta=0):
    # t=sin(theta) regularizes the endpoint square-root singularity.
    def integrand(theta):
        t=math.sin(theta)
        d=1-t
        if d<1.e-7:
            denom=2*math.exp(q/2)*(1+delta)*d
        else:
            denom=J(q,t,delta)
        return math.cos(theta)*math.exp(q*t**4/4)/math.sqrt(denom)
    return 4*quad(integrand,0,math.pi/2,epsabs=2.e-7,limit=150)[0]

C0=2*math.sqrt(3)*beta(1/6,1/2)/3
assert abs(C(0)-C0)<4.e-6
qs=[0,0.5,1,2,4]
cs=[C(q) for q in qs]
assert all(cs[i]>cs[i+1] for i in range(len(cs)-1))
# Sample *unnormalized* likelihood-ratio increases: normalization is constant.
for q1,q2 in [(0,1),(0,2),(1,4)]:
    ratios=[]
    for t in [0,0.2,0.4,0.6,0.8,0.95]:
        w1=math.exp(q1*t**4/4)/math.sqrt(J(q1,t))
        w2=math.exp(q2*t**4/4)/math.sqrt(J(q2,t))
        ratios.append(w2/w1)
    assert all(a<b for a,b in zip(ratios,ratios[1:]))
assert math.sqrt(2)*C(2)>2*math.pi
from fractions import Fraction
r=Fraction(21,25)*4*Fraction(17,10)*(1+Fraction(1,14)+Fraction(3,104)+Fraction(5,304))
assert r==Fraction(1575543,247000)>Fraction(44,7)
q=2.3
err=[abs(C(q,1/A**4)/C(q)-1) for A in [3,5,9]]
assert err[0]>err[1]>err[2]
print('CHECK_OK', 'C(0)=',C(0),'C(2)=',C(2),'normalized-overlap=',r)
