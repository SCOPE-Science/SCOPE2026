"""Check identities and sample trajectories for a three-state neutral-consensus ODE.

Requires Python 3, SymPy and SciPy.  The symbolic checks are exact.
Numerical trajectories are illustrative only; the accompanying proof handles all
positive parameters and all interior initial states.
"""
import sympy as sp
from scipy.integrate import solve_ivp

x,y,w,a,b,g,r,q,c,ws = sp.symbols('x y w a b g r q c ws', positive=True)
z=sp.symbols('z', real=True)
fx=b*(1-x-y-g*x*y)+r*x*(1-x-y-a)
fy=b*(1-x-y-g*x*y)+r*y*(1-x-y-a)
sub={x:(1-w+z)/2,y:(1-w-z)/2}
G=c*(1-w)**2-2*b*w-r*(1-w)*(w-a)
qdot=2*r*q*(w-a)
wdot=G-c*q
assert sp.simplify(((fx-fy).subs(sub))-r*z*(w-a))==0
assert sp.simplify((-(fx+fy)).subs(sub)-wdot.subs({c:b*g/2,q:z**2}))==0
qstar=(1-a)**2-4*a/g
assert sp.simplify(G.subs(w,a)-c*qstar.subs(g,2*c/b))==0
polar_dV=sp.expand(c*(q-qstar.subs(g,2*c/b))*(w-a)+(w-a)*wdot)
assert sp.factor(polar_dV+(w-a)**2*(c*(2-w-a)+2*b+r*(1-w)))==0
Wdot=sp.expand(c*q*(w-a)+(w-ws)*wdot)
assert sp.factor(Wdot-((w-ws)*G+c*q*(ws-a)))==0
B=2*c*(1-a)+2*b+r*(1-a)
u=sp.symbols('u',real=True)
assert sp.expand(wdot.subs(w,a+u)-(G.subs(w,a)-B*u+(c+r)*u**2-c*q))==0
assert sp.simplify(G.subs({w:sp.Rational(1,2),a:sp.Rational(1,2),b:1,r:1,c:4}))==0
s=sp.symbols('s', positive=True)
# s = -u/q; differentiating along the exact two-variable flow
sdot=sp.simplify((-(-B*u+(c+r)*u**2-c*q)*q+u*qdot.subs(w,a+u))/q**2)
assert sp.factor(sdot.subs(u,-s*q)-(c-B*s-(c-r)*q*s**2))==0
# Exact critical parameter example a=1/2,b=r=1,g=8.
example={a:sp.Rational(1,2),b:1,r:1,g:8,c:4}
assert sp.simplify(B.subs(example))==sp.Rational(13,2)
assert sp.simplify((B/(2*r*c)).subs(example))==sp.Rational(13,16)
# Strictly polarized equilibrium for a=1/4,b=r=1,g=8.
assert sp.simplify(qstar.subs({a:sp.Rational(1,4),g:8})-sp.Rational(7,16))==0

def field(tt,state,alpha,beta=1.,gamma=8.,rho=1.):
    xx, yy=state
    ww=1-xx-yy
    F=beta*(ww-gamma*xx*yy)
    return [F+rho*xx*(ww-alpha),F+rho*yy*(ww-alpha)]

for alpha,expected in [(0.25,'polar'),(0.5,'critical'),(0.75,'neutral')]:
    for initial in [(0.61,0.12),(0.12,0.61),(0.28,0.28)]:
        sol=solve_ivp(field,(0,100000 if alpha==0.5 else 180),initial,
                      args=(alpha,),rtol=5e-11,atol=1e-13,method='DOP853')
        assert sol.success, sol.message
        xx,yy=sol.y[:,-1]
        if expected=='polar' and initial[0]!=initial[1]:
            expectedz=(7/16)**0.5 * (1 if initial[0]>initial[1] else -1)
            assert abs(xx-yy-expectedz)<3e-7
        if expected=='polar' and initial[0]==initial[1]:
            assert abs(xx-yy)<1e-10
        if expected=='neutral':
            assert abs(xx-yy)<1e-8
        if expected=='critical' and initial[0]!=initial[1]:
            # Only an asymptotic consistency check, not the mathematical proof.
            assert abs(100000*(xx-yy)**2-13/16)<0.01
print('PASS: seven exact symbolic identities, two exact examples, nine trajectories')
