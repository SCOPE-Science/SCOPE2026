"""Symbolic algebraic checks and reproducible numerical diagnostics for the equal-response two-environment evolutionary game.

Scientific claim is proven in RESULT.md; experiments do not establish the infinite-time conclusions.
"""
from fractions import Fraction
from math import exp, log
import sympy as sp
from scipy.integrate import quad, solve_ivp
from scipy.optimize import brentq

x, z = sp.symbols('x z', real=True)
d0,e0,d1,e1,theta = sp.symbols('d0 e0 d1 e1 theta', positive=True)
A=e0*(1-x)+d0*x
B=(e0+e1)*(1-x)+(d0+d1)*x
xs=1/(1+theta)
Delta=d0*e1-e0*d1
Es=sp.cancel(A.subs(x,xs)/B.subs(x,xs))
assert sp.simplify(sp.diff(A,x)*B-A*sp.diff(B,x)-Delta)==0
assert sp.simplify((x-xs)*(A/B-Es)-Delta*(x-xs)**2/(B*B.subs(x,xs)))==0
assert sp.simplify(A.subs(x,xs)-B.subs(x,xs)*Es)==0
assert sp.simplify(sp.diff(A-B*z,x).subs(z,Es)-Delta/B.subs(x,xs))==0
print('symbolic quotient and dissipation identities: PASS')

def logistic(u):
    if u>=0:
        return 1/(1+exp(-u))
    p=exp(u)
    return p/(1+p)

def example(name,values,theta0,delta,init,duration):
    dd0,ee0,dd1,ee1=values
    det=dd0*ee1-ee0*dd1
    xstar=1/(1+theta0)
    ax=lambda xx: ee0*(1-xx)+dd0*xx
    bx=lambda xx: (ee0+ee1)*(1-xx)+(dd0+dd1)*xx
    estar=ax(xstar)/bx(xstar)
    logit=lambda y: log(y/(1-y))
    k=logit(init[1])-logit(init[2])
    E=lambda u:(1-delta)*logistic(u)+delta*logistic(u-k)
    ustar=brentq(lambda u:E(u)-estar,-40,40)
    target=(xstar,logistic(ustar),logistic(ustar-k))
    def vector(t,state):
        xx,nn,mm=state
        pressure=(1-delta)*nn+delta*mm
        return [xx*(1-xx)*(ax(xx)-bx(xx)*pressure),
                nn*(1-nn)*((1+theta0)*xx-1),
                mm*(1-mm)*((1+theta0)*xx-1)]
    def energy(xx,nn,mm):
        u=logit(nn)
        q1=quad(lambda zz:(zz-xstar)/(zz*(1-zz)*bx(zz)),xstar,xx,epsabs=1e-11)[0]
        q2=quad(lambda zz:(E(zz)-estar)/(1+theta0),ustar,u,epsabs=1e-11)[0]
        return q1+q2
    sol=solve_ivp(vector,(0,duration),init,rtol=2e-11,atol=2e-13,max_step=.06)
    assert sol.success
    isvalid=all(min(a)>0 and max(a)<1 for a in sol.y)
    assert isvalid
    evals=[energy(*sol.y[:,i]) for i in range(0,len(sol.t),max(1,len(sol.t)//10))]
    if det<0:
        assert all(evals[i+1]<evals[i]+1e-7 for i in range(len(evals)-1))
        error=max(abs(sol.y[j,-1]-target[j]) for j in range(3))
        assert error<1e-3, (name,error)
    elif det==0:
        assert max(abs(v-evals[0]) for v in evals)<1e-8,(name,evals)
    else:
        assert all(evals[i+1]>evals[i]-1e-7 for i in range(len(evals)-1))
    kmax=max(abs(logit(sol.y[1,i])-logit(sol.y[2,i])-k) for i in range(0,len(sol.t),max(1,len(sol.t)//30)))
    assert kmax<1e-7,(name,kmax)
    print(f'{name}: determinant={det}, initial H={evals[0]:.9g}, final H={evals[-1]:.9g}, odds-constant max abs error={kmax:.3g}, final x={sol.y[0,-1]:.9g}: PASS')

example('strictly attracting (Betz--Fu--Masuda payoff example)',(2,1,5,2),5,.5,(.7,.4,.1),800)
example('critical neutral (non-mirror payoffs)',(2,1,4,2),2,.35,(.6,.1,.7),90)
example('repelling (opposite payoff cross-ratio)',(1,1,1,2),2,.4,(.4,.3,.7),30)
print('All symbolic and numerical checks completed.')
