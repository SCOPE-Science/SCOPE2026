"""Reproduce algebraic and certified numerical checks for symmetric cubic interpolation.

Requirements: Python 3.10+ and SymPy. This script is a supporting check;
its finite numerical tests do not replace the theorem's analytic proof.
"""
from fractions import Fraction
from math import isqrt
import sympy as sp

x, a = sp.symbols('x a', real=True)
nodes = [-1, -a, a, 1]
L = []
for i in range(4):
    top = sp.prod(x - nodes[j] for j in range(4) if j != i)
    bottom = sp.prod(nodes[i] - nodes[j] for j in range(4) if j != i)
    L.append(sp.factor(top / bottom))
assert sp.simplify(sum(L)-1) == 0
step = [sp.expand(sum(L[j] for j in range(k, 4))) for k in range(1,4)]
assert sp.simplify(step[2] - (x+1)*(x*x-a*a)/(2*(1-a*a))) == 0
q = 1+a+a*a
assert sp.simplify(step[1] - (sp.Rational(1,2) + x*(q-x*x)/(2*a*(1+a)))) == 0
assert sp.simplify(step[0] - (1-step[2].subs(x,-x))) == 0
assert sp.simplify(step[1].subs(x,-x) + step[1] - 1) == 0
assert sp.simplify(sp.diff(step[2],x) - (3*x*x+2*x-a*a)/(2*(1-a*a))) == 0
assert sp.simplify(sp.diff(step[1],x) - (q-3*x*x)/(2*a*(1+a))) == 0

# For any rational v>0, enclose sqrt(v) using exact integer arithmetic.
def sqrt_interval(v: Fraction, scale: int = 10**32):
    k = isqrt((v.numerator*scale*scale)//v.denominator)
    low, high = Fraction(k,scale), Fraction(k+1,scale)
    assert low*low <= v < high*high
    return low,high

def envelope_interval(t: Fraction):
    # m(t)=q*sqrt(q/3)/(3*t*(1+t))-1/2
    qv = 1+t+t*t
    sl,sh = sqrt_interval(qv/3)
    ml = qv*sl/(3*t*(1+t))-Fraction(1,2)
    mh = qv*sh/(3*t*(1+t))-Fraction(1,2)
    # e(t)=(s-1)(s+2)/(9*(2-s)), s=sqrt(1+3*t^2)
    el,eh = sqrt_interval(1+3*t*t)
    def e_from_s(s):return (s-1)*(s+2)/(9*(2-s))
    return (ml,mh),(e_from_s(el),e_from_s(eh))

left, right = Fraction(4458209224,10**10), Fraction(4458209226,10**10)
(mlo,mhi),(elo,ehi) = envelope_interval(left)
assert mlo > ehi, 'At lower endpoint middle defect must be larger'
(mlo,mhi),(elo,ehi) = envelope_interval(right)
assert mhi < elo, 'At upper endpoint endpoint defect must be larger'

for t in (Fraction(1,3), Fraction(1,2), Fraction(2,5), Fraction(3,5)):
    (ml,mh),(el,eh) = envelope_interval(t)
    print('a=',str(t),'mid~',float((ml+mh)/2),'end~',float((el+eh)/2))

# Explicit witnesses: middle-step interpolant at x=sqrt(q/3) and
# terminal-step interpolant at x=(sqrt(1+3a^2)-1)/3.
def defect_values(t):
    (ml,mh),(el,eh)=envelope_interval(t)
    return float((ml+mh)/2),float((el+eh)/2)
print('root a in',float(left),float(right))
print('sharp defect near',defect_values(Fraction(4458209225,10**10)))

# Independent sampled, non-proof sanity check of the universal envelope.
import random
rng=random.Random(271828)
for t in (Fraction(1,5),Fraction(1,3),Fraction(2,5),Fraction(1,2),Fraction(4,5)):
    m,e=defect_values(t)
    bound=max(m,e)
    for _ in range(300):
        ys=sorted(rng.random() for _ in range(4))
        z=rng.uniform(-1,1)
        nodes_f=(-1.0,-float(t),float(t),1.0)
        basis=[]
        for i in range(4):
            value=1.0
            for j in range(4):
                if i!=j:value*=(z-nodes_f[j])/(nodes_f[i]-nodes_f[j])
            basis.append(value)
        p=sum(v*y for v,y in zip(basis,ys))
        assert -bound-1e-11 <= p <= 1+bound+1e-11
print('PASS: exact Lagrange identities, exact isolating bracket, and sample checks')
