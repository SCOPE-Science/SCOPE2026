#!/usr/bin/env python3
"""Reproducible checks for two-atom biased Gaussian opinion transport.

Requires Python 3, SymPy, mpmath, and SciPy. The analytical theorem and its
quantifiers are in RESULT.md; sampled checks alone do not prove them.
"""
import math
import sympy as s
import mpmath as mp

D, b, p, c = s.symbols('D b p c', real=True)

def g(z):
    return s.exp(-(z-1)**2) + (b-1)*s.exp(-(z+1)**2)

q = 1-p
left = c*(p*g(0)+q*g(D))
right = c*(p*g(-D)+q*g(0))
sep = (c/s.E)*((2*p-1)*b*(s.exp(-D**2)*s.cosh(2*D)-1)
                 -(2-b)*s.exp(-D**2)*s.sinh(2*D))
mean = (c*b/s.E)*(p**2+q**2+2*p*q*s.exp(-D**2)*s.cosh(2*D))
assert s.simplify(s.expand((right-left-sep).rewrite(s.exp))) == 0
assert s.simplify(s.expand((p*left+q*right-mean).rewrite(s.exp))) == 0
print('symbolic two-atom velocity and barycenter identities: PASS')

r = (s.cosh(2*D)-s.exp(D**2))/s.sinh(2*D)
F = s.exp(D**2)*(s.cosh(2*D)-D*s.sinh(2*D))
rprime = 2*(F-1)/s.sinh(2*D)**2
Fprime = s.exp(D**2)*(1-2*D**2)*s.sinh(2*D)
assert s.simplify(s.expand((s.diff(r, D)-rprime).rewrite(s.exp))) == 0
assert s.simplify(s.expand((s.diff(F,D)-Fprime).rewrite(s.exp))) == 0
print('critical-ratio derivative and unique-peak certificate identities: PASS')

mp.mp.dps=45
R=lambda d:(mp.cosh(2*d)-mp.exp(d*d))/mp.sinh(2*d)
Ft=lambda d:mp.exp(d*d)*(mp.cosh(2*d)-d*mp.sinh(2*d))-1
dstar=mp.findroot(Ft,(mp.mpf('.75'),mp.mpf('1.1')))
rmax=R(dstar)
dzero=mp.findroot(lambda d:mp.log(mp.cosh(2*d))-d*d,(mp.mpf('1.3'),mp.mpf('1.8')))
assert 1/mp.sqrt(2)<dstar<dzero and rmax>0
assert abs(Ft(dstar))<mp.mpf('1e-40')
assert abs(R(dzero))<mp.mpf('1e-40')

# Positive-gap equilibria are the crossings of this scalar function.
def level(d,delta,bias):
    return delta*bias*R(d)-(2-bias)

def roots(delta,bias):
    x=[mp.mpf('0.000001')+mp.mpf(i)*mp.mpf('.005') for i in range(2000)]
    v=[level(y,delta,bias) for y in x]
    out=[]
    for i in range(len(x)-1):
        if v[i]*v[i+1]<0:
            z=mp.findroot(lambda y:level(y,delta,bias),(x[i],x[i+1]),solver='anderson')
            if z>0 and not any(abs(z-w)<mp.mpf('1e-20') for w in out):out.append(z)
    return sorted(out)

bc=lambda delta:2/(1+delta*rmax)
assert len(roots(mp.mpf('.5'),mp.mpf('1.7')))==0
rpos=roots(mp.mpf('.5'),mp.mpf('1.95'))
assert len(rpos)==2 and 0<rpos[0]<dstar<rpos[1]<dzero
rneg=roots(mp.mpf('-.5'),mp.mpf('1.95'))
assert len(rneg)==1 and rneg[0]>dzero
assert len(roots(mp.mpf('0'),mp.mpf('1.95')))==0
print('root classification: PASS')
print('d_star =',mp.nstr(dstar,17),'r_max =',mp.nstr(rmax,17))
print('d_zero =',mp.nstr(dzero,17),'b_crit(delta=1/2) =',mp.nstr(bc(mp.mpf('.5')),17))
print('delta=+1/2, b=1.95 roots:',*[mp.nstr(z,17) for z in rpos])
print('delta=-1/2, b=1.95 escape threshold:',mp.nstr(rneg[0],17))

# Check the derived saddle-node square-root opening, not a numerical proof.
rpp=2*mp.exp(dstar*dstar)*(1-2*dstar*dstar)/mp.sinh(2*dstar)
A=mp.sqrt(-4/(mp.mpf('.5')*bc(mp.mpf('.5'))**2*rpp))
for eps in [mp.mpf('1e-4'),mp.mpf('1e-6')]:
    beta=bc(mp.mpf('.5'))+eps
    f=lambda d:level(d,mp.mpf('.5'),beta)
    dl=mp.findroot(f,(dstar-2*A*mp.sqrt(eps),dstar-A*mp.sqrt(eps)/2))
    dh=mp.findroot(f,(dstar+A*mp.sqrt(eps)/2,dstar+2*A*mp.sqrt(eps)))
    ratio=(dh-dl)/(2*A*mp.sqrt(eps))
    assert abs(ratio-1)<mp.mpf('.003')
    print('square-root opening eps',mp.nstr(eps,3),'ratio',mp.nstr(ratio,17))

# Independent direct ODE integration checks for the phase portrait.
from scipy.integrate import solve_ivp

def physical(d,pt,bias):
    delta=2*pt-1
    z=delta*bias*(math.exp(-d*d)*math.cosh(2*d)-1)
    z-=(2-bias)*math.exp(-d*d)*math.sinh(2*d)
    return z/math.e

def direct_rhs(t,ys,pt,bias):
    xl,xr=ys; dist=xr-xl
    def kernel(z):return math.exp(-(z-1)**2)+(bias-1)*math.exp(-(z+1)**2)
    return [pt*kernel(0)+(1-pt)*kernel(dist),pt*kernel(-dist)+(1-pt)*kernel(0)]

for pt,bias,dinit,tend,kind in [
    (.75,1.95,.04,250,'collapse'),
    (.75,1.95,.3,200,'finite'),
    (.75,1.95,3,200,'finite'),
    (.25,1.95,1,200,'collapse'),
    (.25,1.95,2,200,'escape'),
    (.5,1.95,2,300,'collapse'),
    (.75,2,1,200,'finite'),
    (.25,2,2,200,'escape'),
    (.5,2,1,200,'frozen'),
]:
    sol=solve_ivp(lambda t,y:direct_rhs(t,y,pt,bias),[0,tend],[0,dinit],
                  rtol=2e-10,atol=2e-11,max_step=.1)
    final=sol.y[1,-1]-sol.y[0,-1]
    assert sol.success
    if kind=='collapse': assert final<0.001,(pt,bias,dinit,final)
    if kind=='finite':
        ref=float(dzero) if bias==2 else float(rpos[1])
        assert abs(final-ref)<0.003,(pt,bias,final,ref)
    if kind=='escape':assert final>dinit+2,(pt,bias,final)
    if kind=='frozen':assert abs(final-dinit)<1e-7
    assert abs(direct_rhs(0,[0,dinit],pt,bias)[1]-direct_rhs(0,[0,dinit],pt,bias)[0]-physical(dinit,pt,bias))<1e-12
print('direct two-coordinate ODE phase samples and gap identities: PASS')

print('all checks: PASS')
