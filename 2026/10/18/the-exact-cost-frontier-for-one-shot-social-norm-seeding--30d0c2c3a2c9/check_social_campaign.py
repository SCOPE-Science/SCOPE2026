"""Numerical spot checks for the one-shot social-norm seeding frontier.
These checks supplement, but do not replace, the analytic proof.
"""
import math
from scipy.optimize import brentq, minimize_scalar
from scipy.integrate import solve_ivp


def boundary(beta,r,x):
    u=1-x
    s=1-r
    if abs(beta-1)<1e-13:
        return 1-r+u*(math.log(u/s)-1)
    return 1-r+beta*u/(1-beta)-s**(1-beta)*u**beta/(1-beta)


def boundary_deriv(beta,r,x):
    t=(1-x)/(1-r)
    if abs(beta-1)<1e-13:
        return -math.log(t)
    return beta*math.expm1((beta-1)*math.log(t))/(1-beta)


def optimum(beta,r,ratio):
    a=brentq(lambda x: boundary(beta,r,x)-x,0,r,xtol=2e-15)
    lc=-boundary_deriv(beta,r,a)
    if ratio>=lc:
        x=a
    elif abs(beta-1)<1e-13:
        x=1-(1-r)*math.exp(ratio)
    else:
        t=(1+(beta-1)*ratio/beta)**(1/(beta-1))
        x=1-(1-r)*t
    y=boundary(beta,r,x)
    return x,y,ratio*x+y,lc,a


def flow(beta,r,x0,y0,T=400):
    def rhs(t,state):
        x,y=state
        return ((1-x)*y,beta*y*(x-y-r))
    sol=solve_ivp(rhs,(0,T),(x0,y0),rtol=1e-10,atol=1e-12,method='DOP853')
    return sol.y[:,-1]


def run():
    for beta,r in [(0.25,0.3),(0.6,0.1),(1,0.5),(1,0.8),(1.5,0.25),(2,0.5),(3,0.95),(8,0.15)]:
        for ratio in [0.01,0.1,0.5,1,3,8]:
            x,y,c,lc,a=optimum(beta,r,ratio)
            assert a<=x<r+1e-10, (beta,r,ratio,x,a)
            assert 0<y<=x+1e-11 or (abs(y)<1e-12 and abs(x-r)<1e-10)
            assert abs(boundary(beta,r,x)-y)<2e-12
            def cost(x):return ratio*x+boundary(beta,r,x)
            direct=minimize_scalar(cost,bounds=(a,r),method='bounded',options={'xatol':1e-13})
            assert c<=direct.fun+1e-9,(beta,r,ratio,c,direct.fun)
            assert abs(c-min(cost(a),cost(r),direct.fun))<2e-9,(beta,r,ratio,c)
            if 0.02 < ratio < lc-0.02:
                assert abs(boundary_deriv(beta,r,x)+ratio)<2e-10
            if ratio>=lc:
                assert abs(y-x)<2e-10
    # Numerical trajectories on either side of the separatrix.
    for beta,r in [(1.,.5),(.6,.35),(2.,.4)]:
        a=optimum(beta,r,.1)[4]
        x=(r+a)/2
        h=boundary(beta,r,x)
        for mult,ought in [(.7,'quiet'),(1.3,'outbreak')]:
            y=h*mult
            assert y<x
            xx,yy=flow(beta,r,x,y,700)
            if ought=='quiet':
                assert yy<1e-5 and xx<r,(beta,r,xx,yy)
            else:
                assert xx>.999 and abs(yy-(1-r))<5e-4,(beta,r,xx,yy)
    # Omega constant closed form.
    beta,r=1.,.5
    x,y,c,lc,a=optimum(beta,r,0.2)
    from scipy.special import lambertw
    omega=lambertw(1).real
    assert abs(lc-omega)<1e-12
    assert abs(a-(1-.5/omega))<1e-12
    assert abs(c-(.2+.5*(1-math.exp(.2))))<1e-12
    print('PASS: 48 exact-form/numeric minimizer comparisons; 6 trajectory outcomes; omega-constant check')
    print('Example beta=1, gamma=1/2, c_s/c_v=1/5: x,y,normalised_cost,lambda_c,a=',x,y,c,lc,a)
    x2,y2,c2,_,_=optimum(1,.5,1.)
    print('Example c_s/c_v=1: x,y,normalised_cost=',x2,y2,c2)

if __name__=='__main__':run()
