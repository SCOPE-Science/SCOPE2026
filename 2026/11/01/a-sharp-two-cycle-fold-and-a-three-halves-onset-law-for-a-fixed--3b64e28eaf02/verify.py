"""Exact algebra and numerical independent branch checks for the two-cycle census.

Requires Python 3 and SymPy. Does not substitute finite testing for the proof.
"""
import math
from math import comb
import sympy as s

x, z, beta, alpha, C, A, u, t = s.symbols(
    'x z beta alpha C A u t', real=True)
R2 = 1 - 1 / beta

# Start at (x,z-x/2), pass through (-x,z+x/2).
x_after = alpha*C + beta*((z-x/2)**2 - 1)*x
x_back = alpha*C - beta*((z+x/2)**2 - 1)*x
# Work modulo the two defining equations without assuming a floating-point root.
for numerator in (x_after + x, x_back - x):
    reduced = s.expand(numerator.subs(alpha*C, beta*z*x*x))
    quotient = s.factor(reduced / (z*z + x*x/4 - R2))
    assert s.simplify(reduced - quotient*(z*z + x*x/4 - R2)) == 0

# The derivative of log[beta*x^2*sqrt((A-x^2)/4)/cos(x)].
log_derivative = 2/x + s.tan(x) - x/(A-x*x)
assert s.simplify(s.diff(log_derivative,x) -
     (-2/x**2 + 1/s.cos(x)**2 -(A+x*x)/(A-x*x)**2)) == 0

# For 0<x^2<A<=2, the strictly decreasing-in-A rational term
# is bounded below by its A=2 value. Taylor's alternating bound
# cos(x) > c(x^2) reduces strict log concavity to P(u)>0 on 0<u<2.
c = 1-u/2+u*u/24-u**3/720
r = 2/u + (2+u)/(2-u)**2
P = s.cancel((r-1/c**2)*u*(2-u)**2*c**2)
expected = (3*u**8-186*u**7+5228*u**6-79320*u**5+669600*u**4-
            3294720*u**3+8121600*u**2-9331200*u+4147200)/s.Integer(518400)
assert s.simplify(P-expected)==0
poly=s.Poly(s.expand(P.subs(u,2*t)),t)
coeff=[poly.nth(k) for k in range(9)]
bern=[s.factor(sum(coeff[k]*s.Rational(comb(j,k),comb(8,k))
                   for k in range(j+1))) for j in range(9)]
assert bern == [s.Integer(8),s.Rational(7,2),s.Rational(26,21),
                s.Rational(193,630),s.Rational(29,315),
                s.Rational(1439,7560),s.Rational(9631,28350),
                s.Rational(1519,4050),s.Rational(392,2025)]
assert all(v>0 for v in bern)
assert s.simplify(P.subs(u,2*t)-sum(
    bern[j]*comb(8,j)*t**j*(1-t)**(8-j) for j in range(9)))==0

# Leading fold exponent from the maximizer of s^2 sqrt(1-s^2).
v=s.symbols('v', positive=True)
f=v*s.sqrt(1-v)  # v=(x/(2R))^2, so v=2/3 at the maximum
assert s.simplify(s.diff(f,v).subs(v,s.Rational(2,3)))==0
assert s.simplify(4*f.subs(v,s.Rational(2,3))-
                  8/(3*s.sqrt(3)))==0

# Independent forward-map checks using two distinct scalar roots.
def bisect(fun,low,high):
    f0=fun(low)
    for _ in range(100):
        mid=(low+high)/2
        if fun(mid)*f0>0: low,f0=mid,fun(mid)
        else: high=mid
    return (low+high)/2

def orbit(alpha_val,beta_val,x_val):
    rr=1-1/beta_val
    z_val=math.sqrt(rr-x_val*x_val/4)
    y_val=z_val-x_val/2
    def step(x,y):
        return alpha_val*math.cos(x)+beta_val*(y*y-1)*x, y+x
    x1,y1=step(x_val,y_val)
    x2,y2=step(x1,y1)
    return (x1,y1),(x2,y2),(z_val+x_val/2)

for beta_val,alpha_val in [(1.35,.1),(1.7,.1),(1.85,.1)]:
    rr=1-1/beta_val; xmax=2*math.sqrt(rr)
    def curve(w):return beta_val*w*w*math.sqrt(max(0,rr-w*w/4))/math.cos(w)
    # Find the unique maximum by a golden-section search (independent of formula).
    l,h=0.,xmax
    for _ in range(100):
        p=l+(h-l)*.3819660112501051
        q=h-(h-l)*.3819660112501051
        if curve(p)<curve(q):l=p
        else:h=q
    xm=(l+h)/2
    assert curve(xm)>alpha_val
    roots=(bisect(lambda w:curve(w)-alpha_val,0,xm),
           bisect(lambda w:curve(w)-alpha_val,xm,xmax))
    assert roots[0]<xm<roots[1]
    for root in roots:
        (xx,yy),(xxx,yyy),target_y=orbit(alpha_val,beta_val,root)
        assert max(abs(xx+root),abs(yy-target_y),
                   abs(xxx-root),abs(yyy-(target_y-root))) < 1e-12
    print(f'beta={beta_val}: two distinct two-cycles; x={roots[0]:.12f}, {roots[1]:.12f}')
print('Exact period equations, strict-concavity Bernstein certificate, and fold scaling verified.')
