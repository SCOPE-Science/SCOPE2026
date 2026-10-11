#!/usr/bin/env python3
import math
import random
import sympy as sp

S,x,t,r=sp.symbols("S x t r", positive=True, real=True)
H2=S**2-x**2

# Regime 2 quadratic and its unconstrained critical point.
d2=(1-x+t*(1+x/S))**2 + H2*(1-t/S)**2
assert sp.simplify(sp.factor(sp.diff(d2,t)) - 2*(S+x)*(-S+2*t+1)/S)==0
t0=(S-1)/2
h2sq=(S-x)*(S+1)**2/(2*S)
assert sp.simplify(d2.subs(t,t0)-h2sq)==0

# Regime 3.
d3=(1+x**2/S)**2 + H2*(1-(x+2*t)/S)**2
tm=(S-x)/2
assert sp.simplify(d3.subs(t,tm)-(1+x**2/S)**2)==0

A2=(S**2-x**2)/(S+1)**2
B2=(S-x)/(2*S)
C=(S+x**2)/(S*(S+1))
assert sp.simplify(sp.factor(A2-B2) - (S-x)*(S**2+2*S*x-2*S-1)/(2*S*(S+1)**2))==0

x0=(2*S+1-S**2)/(2*S)
P=11*S**5-17*S**4+6*S**3-2*S**2-5*S-1
num=sp.factor(sp.together((A2-C**2).subs(x,x0)).as_numer_denom()[0])
assert sp.factor(num-(S+1)**3*P)==0
y=sp.symbols("y", positive=True)
assert sp.expand(P.subs(S,1+y)) == 11*y**5+38*y**4+48*y**3+24*y**2-4*y-8
assert P.subs(S,1)<0 and P.subs(S,2)>0

roots=sp.nroots(P, n=40, maxsteps=200)
real_roots=[complex(z) for z in roots if abs(complex(z).imag)<1e-25]
assert len(real_roots)==1
Sstar=real_roots[0].real
assert 1<Sstar<2
xstar=float(x0.subs(S,Sstar))
mstar=math.sqrt((Sstar-xstar)/(2*Sstar))
dstar=1/mstar

mA=(sp.sqrt(S*(5*S+4))-S)/(2*(S+1))
dmA=sp.factor(sp.diff(mA,S))
expected=(-sp.sqrt(S)*sp.sqrt(5*S+4)+3*S+2)/(2*sp.sqrt(S)*(S+1)**2*sp.sqrt(5*S+4))
assert sp.simplify(dmA-expected)==0

Sofr=(1-r)/(r-(1-2*r**2)**2)
assert sp.simplify(sp.factor(sp.diff(Sofr,r)) + 4*r*(3*r+2)/(4*r**3+4*r**2-1)**2)==0

# Direct boundary sampler.
def formula_h(xx,SS):
    HH=math.sqrt(SS*SS-xx*xx)
    vals=[HH,1+xx*xx/SS]
    if 1 <= SS <= 1+2*xx:
        vals.append(math.sqrt((SS-xx)*(SS+1)**2/(2*SS)))
    return min(vals)

def sampled_h(xx,SS,N=6000):
    HH=math.sqrt(SS*SS-xx*xx)
    b=1-xx
    a=1+xx
    L=2*(1+SS)
    half=1+SS
    V=[(0.0,0.0),(b,0.0),(1.0,HH),(-xx,HH)]
    lens=[b,SS,a,SS]
    cum=[0.0]
    for z in lens:
        cum.append(cum[-1]+z)
    def point(u):
        u%=L
        for i,l in enumerate(lens):
            if u <= cum[i+1]+1e-13:
                q=(u-cum[i])/l
                A=V[i]; B=V[(i+1)%4]
                return (A[0]+q*(B[0]-A[0]), A[1]+q*(B[1]-A[1]))
        raise RuntimeError
    best=1e99
    for k in range(N):
        u=half*k/N
        p=point(u); q=point(u+half)
        best=min(best,math.hypot(p[0]-q[0],p[1]-q[1]))
    return best

random.seed(72)
worst=0.0
for _ in range(35):
    xx=random.uniform(0.0,0.97)
    SS=random.uniform(xx+0.03,3.0)
    exact=formula_h(xx,SS)
    approx=sampled_h(xx,SS)
    err=abs(approx-exact)
    worst=max(worst,err)
    assert err<2e-6,(xx,SS,exact,approx)

# Coarse global search cannot beat the algebraic optimum.
best=0.0
arg=None
for i in range(501):
    SS=0.3+(2.7*i/500)
    for j in range(401):
        xx=min(0.999, (min(0.999,SS-1e-6))*j/400)
        if SS<=xx:
            continue
        q=formula_h(xx,SS)/(1+SS)
        if q>best:
            best=q; arg=(xx,SS)
assert best <= mstar + 2e-4
assert abs(dstar-1.89615765267304)<2e-13

print("VERIFY_OK")
print("S_star = %.15f" % Sstar)
print("x_star = %.15f" % xstar)
print("delta_star = %.15f" % dstar)
print("max_direct_halving_error = %.3e" % worst)
print("coarse_best_inverse_dilation = %.15f" % best)
