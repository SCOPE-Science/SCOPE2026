"""Exact checks for the normalized random-triangle-area variance on trapezoids.

Reproducible with Python 3.10+ and SymPy. Standard-library Monte Carlo checks
are independent of the symbolic integration and covariance identities.
"""
import math
import random
import sympy as s

t, y, u, v = s.symbols('t y u v', real=True)
r = lambda z: 1-(1-t)*z
area=1+t
# Direct ordered-height integration of the absolute area determinant.
kernel=s.expand((v-u)**2*(4*r(u)**3*r(v)+3*r(u)**2*r(v)**2+4*r(u)*r(v)**3))
I=s.integrate(s.integrate(kernel,(u,0,v)),(v,0,1))
assert s.factor(I-(3*t**4+12*t**3+14*t**2+12*t+3)/48)==0
mean=s.factor(4*I/(3*area**3))
assert mean==(3*t**4+12*t**3+14*t**2+12*t+3)/(36*(t+1)**3) or s.simplify(mean-(3*t**4+12*t**3+14*t**2+12*t+3)/(36*(t+1)**3))==0
# Independent centered covariance computation, E(area^2)=3 det(Sigma)/2.
EX=s.integrate(2*r(y)**3/3,(y,0,1))/area
EY=s.integrate(2*y*r(y),(y,0,1))/area
EY2=s.integrate(2*y*y*r(y),(y,0,1))/area
varY=s.factor(EY2-EY**2)
assert s.factor(EX-(1+t**2)/6)==0
assert s.factor(varY-(1+4*t+t**2)/(18*(t+1)**2))==0
mean_square=s.factor(s.Rational(3,2)*EX*varY)
assert s.factor(mean_square-(1+t*t)*(1+4*t+t*t)/(72*(1+t)**2))==0
C=s.factor(mean_square/mean**2-1)
P=3*t**4+12*t**3+14*t**2+12*t+3
N=9*t**8+72*t**7+204*t**6+312*t**5+326*t**4+312*t**3+204*t**2+72*t+9
assert s.factor(C-N/P**2)==0
derivative=144*t*(t-1)*(t+1)**3*(t**4+4*t**3+10*t**2+4*t+1)/P**3
assert s.factor(s.diff(C,t)-derivative)==0
assert C.subs(t,0)==1
assert C.subs(t,1)==s.Rational(95,121)
assert s.limit((1-C)/t**2,t,0)==s.Rational(8,3)
assert s.limit((C-s.Rational(95,121))/(1-t)**2,t,1)==s.Rational(180,1331)
print('EXACT_AREA_MOMENTS_AND_MONOTONE_VARIANCE_PROFILE_PASSED')

# Simulate actual uniform-area points independently; compare raw sample C.
rng=random.Random(1162026)
def random_point(ratio,shear):
    z=rng.random()
    h=z if ratio==1 else (1-math.sqrt(1-(1-ratio**2)*z))/(1-ratio)
    return ((2*rng.random()-1)*(1-(1-ratio)*h)+shear*h,h)
def triangle_area(a,b,c):
    return abs((b[0]-a[0])*(c[1]-a[1])-(c[0]-a[0])*(b[1]-a[1]))/2
for ratio,shear in [(0.0,0),(0.23,0),(0.65,0),(0.65,0.81),(1.0,0)]:
    n=120000
    sum1=sum2=0.0
    for _ in range(n):
        z=triangle_area(*[random_point(ratio,shear) for _ in range(3)])
        sum1+=z;sum2+=z*z
    estimated=sum2/n/(sum1/n)**2-1
    target=float(C.subs(t,ratio))
    assert abs(estimated-target)<0.045,(ratio,shear,estimated,target)
    print(f'DIRECT_UNIFORM_TRIANGLE_SIMULATION_PASSED ratio={ratio} shear={shear} observed={estimated:.5f} exact={target:.5f}')
print('ALL_CHECKS_PASSED')
