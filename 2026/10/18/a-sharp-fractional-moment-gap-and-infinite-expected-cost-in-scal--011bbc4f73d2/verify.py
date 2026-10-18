"""Exact-rational interval certificate for a scalar sampled-model MPC benchmark."""
from fractions import Fraction as F
from math import isqrt, log, exp, cosh as fcosh, sinh as fsinh

N=65
class I:
    def __init__(self,a,b=None):
        self.l = a if isinstance(a,F) else F(a)
        self.u = self.l if b is None else (b if isinstance(b,F) else F(b))
        assert self.l<=self.u
    def __add__(self,x):
        x=as_i(x);return I(self.l+x.l,self.u+x.u)
    __radd__=__add__
    def __neg__(self):return I(-self.u,-self.l)
    def __sub__(self,x):return self+-as_i(x)
    def __rsub__(self,x):return as_i(x)+-self
    def __mul__(self,x):
        x=as_i(x); xs=[a*b for a in (self.l,self.u) for b in (x.l,x.u)];return I(min(xs),max(xs))
    __rmul__=__mul__
    def __truediv__(self,x):
        x=as_i(x);assert x.l*x.u>0
        return self*I(1/x.u,1/x.l)
    def __rtruediv__(self,x):return as_i(x)/self
    def __repr__(self):return '[%.17g, %.17g]'%(float(self.l),float(self.u))
def as_i(x):return x if isinstance(x,I) else I(x)
def exppoint(x):
    if x<0:
        a=exppoint(-x);return I(1/a.u,1/a.l)
    term=F(1);s=F(1)
    for j in range(1,N+1):
        term=term*x/j;s+=term
    t=term*x/F(N+1)
    assert x<F(N+2)
    return I(s,s+t/(1-x/F(N+2)))
def exi(x):
    x=as_i(x);return I(exppoint(x.l).l,exppoint(x.u).u)
def sinh(x):return (exi(x)-exi(-as_i(x)))/2
def cosh(x):return (exi(x)+exi(-as_i(x)))/2

a=F(147,145); T=2
bmin=F(3,4);qmin=I(F(5,4))
bplus=F(741,580);qplus=I(F(941,580))
rootnum=42634;scale=10**22;lo=isqrt(rootnum*scale*scale); qactual=I(F(lo,145*scale),F(lo+1,145*scale))
assert qactual.l*qactual.l<=a*a+1<=qactual.u*qactual.u

def transition(b,q):
    d=q*cosh(q*T)-b*sinh(q*T)
    assert d.l>0
    H=(((exi((a+q)*T)-1)/(a+q))-((exi((a-q)*T)-1)/(a-q)))/2
    return exi(a*T)-H/d
u=transition(bmin,qmin);v=transition(bplus,qplus);normal=transition(a,qactual)
assert F(138,100)<u.l and u.u<F(140,100), u
assert -F(50,100)<v.l and v.u<-F(47,100),v
assert F(39,100)<normal.l and normal.u<F(40,100),normal
A=u;B=-v
meanabs=(A+B)/2;meansq=(A*A+B*B)/2
assert meanabs.u<1,meanabs
assert meansq.l>1,meansq
assert (A*B).u<1
print('a=',a,'b_-=',bmin,'b_+=',bplus)
print('q_-=5/4 q_+=941/580 q_0 in',qactual)
print('m_minus=',u,'m_plus=',v,'m_nominal=',normal)
print('rho_1=',meanabs,'rho_2=',meansq,'product_abs=',A*B)
mm=float((u.l+u.u)/2);mp=float((v.l+v.u)/2)
rho=lambda p:(abs(mm)**p+abs(mp)**p)/2
left,right=1.,2.
for _ in range(80):
    mid=(left+right)/2
    if rho(mid)>1:right=mid
    else:left=mid
pp=(left+right)/2
print('p_star approximately',format(pp,'.14f'))
print('sample Lyapunov exponent approximately',format(.5*log(abs(mm*mp)),'.14f'))
print('All rigorous inequalities proven with exact Fraction Taylor intervals; decimal p_star illustrative.')

# Independent time-stepped verification of the exact controlled-plant transition.
def rk4(b,dt=F(2,4000)):
    q=(1+float(b)**2)**.5
    d=q*fcosh(2*q)-float(b)*fsinh(2*q)
    def f(t,x):return float(a)*x-fsinh(q*(2-t))/d
    x=1.0; n=4000;h=2.0/n
    for j in range(n):
        t=j*h
        k1=f(t,x);k2=f(t+h/2,x+h*k1/2);k3=f(t+h/2,x+h*k2/2);k4=f(t+h,x+h*k3)
        x+=h*(k1+2*k2+2*k3+k4)/6
    return x
assert abs(rk4(bmin)-float((u.l+u.u)/2))<2e-10
assert abs(rk4(bplus)-float((v.l+v.u)/2))<2e-10
print('Independent RK4 plant-vs-prediction controls matched both certified multipliers.')
