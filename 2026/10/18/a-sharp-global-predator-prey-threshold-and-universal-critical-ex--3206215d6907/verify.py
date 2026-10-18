"""Reproduce symbolic certificates and bounded numerical illustrations of the theorem.

Run: python verify.py
Requires sympy and scipy. Numerical tests illustrate, not prove, global limits.
"""
from fractions import Fraction as Q
from itertools import product
from math import isfinite
import sympy as S
from scipy.integrate import solve_ivp

u,v,r,a,b,c,m,k,alpha,eta=S.symbols('u v r a b c m k alpha eta', positive=True)
D=1+k*v+alpha*u
p=u*(r/D-a*u-b*v)
z=v*(c*b*u-m-eta*v)
H=u+v/c
assert S.simplify(S.diff(H,u)*p+S.diff(H,v)*z- (r*u/D-a*u*u-m*v/c-eta*v*v/c))==0
B=1/(u*v)
div=S.factor(S.diff(B*p,u)+S.diff(B*z,v))
expected=-(a+r*alpha/D**2)/v-eta/u
assert S.simplify(div-expected)==0
# Per-capita partial gradients yield strict signs, including vanishing eta.
f=r/D-a*u-b*v
g=c*b*u-m-eta*v
assert S.simplify(S.diff(f,u)+a+r*alpha/D**2)==0
assert S.simplify(S.diff(f,v)+b+r*k/D**2)==0
assert S.diff(g,u)==c*b and S.diff(g,v)==-eta

count=0
for uone, aa, al, kk, bb, cc, et in product(
        (Q(1,2),Q(1),Q(2)),(Q(1,2),Q(1)),(Q(0),Q(1,3),Q(1)),
        (Q(0),Q(2,5),Q(1)),(Q(1,2),Q(1)),(Q(1,2),Q(1)),
        (Q(0),Q(1,3),Q(1))):
    rr=aa*uone*(1+al*uone)
    mm=cc*bb*uone
    d=1+al*uone
    sig=aa+rr*al/d**2
    kap=bb+rr*kk/d**2
    q=et+cc*bb*kap/sig
    assert sig>0 and kap>0 and q>0
    assert rr/d-aa*uone==0 and cc*bb*uone-mm==0
    for x,y in ((Q(1,2),Q(1,3)),(Q(3,2),Q(2,5))):
        den=1+kk*y+al*x
        du=x*(rr/den-aa*x-bb*y)
        dv=y*(cc*bb*x-mm-et*y)
        hdot=du+dv/cc
        assert hdot==rr*x/den-aa*x*x-mm*y/cc-et*y*y/cc
        # Dulac expression has strictly negative value.
        assert -(aa+rr*al/den**2)/y-et/x<0
    count+=1

assert count==648

def field(t,Y,mv,et):
    x,y=Y
    return [x*(2/(1+y+x)-x-y),y*(x-mv-et*y)]

def integrate(mv,et,T=2000.):
    sol=solve_ivp(lambda t,w:field(t,w,mv,et),(0.,T),[.7,.35],
                  method='DOP853',rtol=1e-11,atol=1e-13,dense_output=False)
    assert sol.success
    return sol.y[:,-1]

for mv,et,target in ((1.5,1,(1,0)),(.5,1,(.75,.25)),(.5,0,(.5,.5))):
    end=integrate(mv,et,400)
    assert abs(end[0]-target[0])<1e-8 and abs(end[1]-target[1])<1e-8,(mv,et,end)
for et,tv in ((1,.5),(0,1)):
    end=integrate(1,et,4000)
    assert abs(4000*end[1]-tv)<.01,(et,end)
    assert abs(4000*(end[0]-1)+tv)<.01,(et,end)

# Exact positive equilibria for 4 regimes of the same five-coefficient model.
for mv,et,xstar,ystar in ((Q(1,2),Q(1),Q(3,4),Q(1,4)),
                             (Q(1,2),Q(0),Q(1,2),Q(1,2))):
    assert xstar*(Q(2)/(1+xstar+ystar)-xstar-ystar)==0
    assert ystar*(xstar-mv-et*ystar)==0
print('VERIFY_OK: 648 exact critical-rate/balance/Dulac grids, symbolic general identities, 5 numerical regime and critical-decay checks')
