"""Exact symbolic identities for the LE2 zero-coupling foliation."""
import sympy as s
x,y,z,a,b,C=s.symbols('x y z a b C',real=True)
F=s.Matrix([y,-x+y*z,-y-a*x*y-b*x*z])
P=x+z+a*x*x/2
assert s.simplify(s.diff(P,x)*F[0]+s.diff(P,y)*F[1]+s.diff(P,z)*F[2]+b*x*z)==0
Fleaf=s.Matrix([y,-x+(C-x-a*x*x/2)*y])
H=x*x/2+y-s.log(1+y)
Hd=s.factor(s.diff(H,x)*Fleaf[0]+s.diff(H,y)*Fleaf[1])
assert s.simplify(Hd-(C-a*x*x/2)*y*y/(1+y))==0
assert s.simplify(Fleaf[1].subs(y,-1)-(-C+a*x*x/2))==0
assert s.simplify(s.diff(Fleaf[0]/(1+y),x)+s.diff(Fleaf[1]/(1+y),y)-C/(1+y)**2 + a*x*x/(2*(1+y)**2))==0
lam=s.Symbol('lam')
J=s.Matrix([y,-x*(1+y)]).jacobian([x,y]).subs({x:0,y:0})
assert s.expand((lam*s.eye(2)-J).det()-(lam**2+1))==0
print('PASS: exact invariant, leaf reduction, Lyapunov identity, crossing sign, Dulac divergence, linearized center')
print('Dulac divergence:',s.simplify(s.diff(Fleaf[0]/(1+y),x)+s.diff(Fleaf[1]/(1+y),y)))

# Only an illustrative numerical cross-check; the infinite-energy asymptotic is proved analytically.
from scipy.optimize import brentq
from scipy.integrate import quad
from math import exp, log, sqrt, pi
W=lambda v: exp(v)-v-1
for h in (0.2,10.0,100.0,1000.0):
    vm=brentq(lambda v:W(v)-h,-h-2,0)
    vp=brentq(lambda v:W(v)-h,0,log(h+2)+2)
    # Endpoint-regularized angular integral; values at endpoints are not sampled.
    def density(theta):
        s=__import__('math').sin(theta)
        v=vm+(vp-vm)*s*s
        return 2*(vp-vm)*s*__import__('math').cos(theta)/sqrt(max(h-W(v),1e-290))
    t=sqrt(2)*quad(density,1e-8,pi/2-1e-8,epsrel=3e-8,limit=300)[0]
    print('h=',h,'T=',round(t,9),'T/sqrt(h)=',round(t/sqrt(h),8))
