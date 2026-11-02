"""Reproducible checks for the equal-pulse four-reservoir Nash hydrograph theorem.

Only the Python standard library is required. This is finite validation, not a
replacement for the analytic proof given in RESULT.md.
"""
from decimal import Decimal, localcontext
from fractions import Fraction
import math
import random

N = 0

def check(c, description):
    global N
    N += 1
    if not c:
        raise AssertionError(description)

def cubic_disc(a,b,c,d):
    return b*b*c*c - 4*a*c*c*c - 4*b*b*b*d - 27*a*a*d*d + 18*a*b*c*d

def coeff(t,e):
    return -(1+e), 3+e*(3+3*t), -e*(6*t+3*t*t), e*(3*t*t+t*t*t)

def predicted_disc(t,e):
    return -27*e*t*t*(-4*e*e*t + 12*e*e + e*t**4 -12*e*t*t+24*e+4*t+12)

for t in (Fraction(1,6),Fraction(1,2),Fraction(3,4),Fraction(1),Fraction(2),Fraction(5,2),Fraction(3),Fraction(7,2),Fraction(5)):
    for e in (Fraction(1,2),Fraction(1),Fraction(5,4),Fraction(2),Fraction(3),Fraction(7)):
        check(cubic_disc(*coeff(t,e)) == predicted_disc(t,e), 'cubic discriminant identity')

# Independent high-precision enclosure for the unique positive critical root.
def Fdec(t):
    ep=t.exp()
    em=(-t).exp()
    return 3*(ep+em) - t*(ep-em) + Decimal(6) - 3*t*t + t**4/4

with localcontext() as ctx:
    ctx.prec=80
    lo=Decimal(2)
    hi=Decimal(3)
    for _ in range(300):
        mid=(lo+hi)/2
        if Fdec(mid)>0: lo=mid
        else: hi=mid
    alpha_dec=(lo+hi)/2
    check(Fdec(Decimal(2))>0 and Fdec(Decimal(3))<0,'endpoint signs')
    check(Decimal('2.9588081482438789725439156947')<alpha_dec<Decimal('2.9588081482438789725439156950'), 'high precision alpha enclosure')
    print('alpha=',alpha_dec)
alpha=float(alpha_dec)

# Direct derivative from the sum of the two hydrographs versus cubic expression.
def h(x):
    return 0.0 if x<0 else x**3 * math.exp(-x)
def hd(x):
    return 0.0 if x<0 else x*x*(3-x)*math.exp(-x)
def derivative(x,t):
    return hd(x)+hd(x-t)
def poly(x,t):
    E=math.exp(t)
    return x*x*(3-x)+E*(x-t)**2*(3-x+t)

rng=random.Random(1719)
for _ in range(3000):
    t=rng.uniform(.01,8)
    x=t+rng.uniform(.0,10)
    lhs=derivative(x,t)
    rhs=math.exp(-x)*poly(x,t)
    check(abs(lhs-rhs)<1.e-10*(1+abs(lhs)),'direct derivative comparison')

def roots_post(t):
    # Roots of the cubic on t >= pulse lag; partition at its two exact stationary abscissas.
    a,b,c,d=coeff(t,math.exp(t))
    D=(2*b)**2-4*(3*a)*c
    check(D>0,'two critical points of cubic')
    extrema=sorted(((-2*b-math.sqrt(D))/(6*a),(-2*b+math.sqrt(D))/(6*a)))
    low=t
    high=t+3
    knots=[low]+[v for v in extrema if low<v<high]+[high]
    def val(x):return ((a*x+b)*x+c)*x+d
    roots=[]
    for l,r in zip(knots[:-1],knots[1:]):
        vl,vr=val(l),val(r)
        if vl*vr<0:
            for _ in range(85):
                m=(l+r)/2
                if val(l)*val(m)>0:l=m
                else:r=m
            roots.append((l+r)/2)
    return roots

for t in [0.5,1.0,2.0,2.8,2.90,2.950,2.958,alpha-0.0001,alpha+0.0001,2.96,2.99,3.001,3.1,3.5,5,7,12]:
    roots=roots_post(t)
    expected= (1 if t<alpha else 3) if t<3 else 2
    check(len(roots)==expected, 'physical roots on post-pulse domain')
    if t>3:
        check(derivative(t,t)<0 and derivative(t+2,t)>0 and derivative(t+3,t)<0,'post-pulse sign triplet')

for _ in range(180):
    t=rng.uniform(.25,11)
    if abs(t-alpha)<.005 or abs(t-3)<.005:
        continue
    roots=roots_post(t)
    expected=(1 if t<alpha else 3) if t<3 else 2
    check(len(roots)==expected,'random mode classification')

for t in [0.2,1,2,2.9,3,4,7]:
    for x in [t, t+0.2, t+1.5,t+2.5, t+3.1]:
        check(abs(h(x)+h(x-t) - (x**3*math.exp(-x)+(x-t)**3*math.exp(-(x-t))))<1e-12,'positive-part hydrograph')

print('VERIFY_OK assertions=',N)
