"""Checks for covariance-target reachability of a stiffness-controlled active OU trap."""
import math
import numpy as np
from scipy.integrate import solve_ivp, quad
from scipy.optimize import brentq


def setup(ai, af, mu, tau, d, da, slew):
    qi, qf = mu*ai, mu*af
    yi, yf = da/(1+tau*qi), da/(1+tau*qf)
    xi, xf = (yi+d)/qi, (yf+d)/qf
    return dict(ai=ai,af=af,mu=mu,tau=tau,d=d,da=da,slew=slew,
                qi=qi,qf=qf,yi=yi,yf=yf,xi=xi,xf=xf, tr=(af-ai)/slew)


def ramp_quadrature(p,t):
    qi, beta, tau = p['qi'],p['mu']*p['slew'],p['tau']
    H=lambda z:(1/tau+qi)*z+beta*z*z/2
    Q=lambda z:qi*z+beta*z*z/2
    y=lambda z: math.exp(-H(z))*(p['yi']+p['da']/tau*quad(lambda s: math.exp(H(s)),0,z,epsabs=3e-12)[0])
    x=math.exp(-2*Q(t))*(p['xi']+2*quad(lambda s: math.exp(2*Q(s))*(p['d']+y(s)),0,t,epsabs=3e-11)[0])
    return x,y(t)


def best_state(p,t):
    tr=p['tr']
    if t <= tr:
        return ramp_quadrature(p,t)
    xr,yr = ramp_quadrature(p,tr)
    s=t-tr
    lam=1/p['tau']+p['qf']; m=2*p['qf']
    dy=yr-p['yf']; dx=xr-p['xf']
    if abs(lam-m)<1e-12:
        zx=(dx+2*dy*s)*math.exp(-m*s)
    else:
        zx=dx*math.exp(-m*s)+2*dy*(math.exp(-lam*s)-math.exp(-m*s))/(m-lam)
    return p['xf']+zx,p['yf']+dy*math.exp(-lam*s)


def error(p,t):
    if t <= p['tr']:
        x,y=best_state(p,t)
        return math.hypot(x-p['xf'],y-p['yf'])
    xr,yr=ramp_quadrature(p,p['tr'])
    s=t-p['tr']
    lam=1/p['tau']+p['qf']; m=2*p['qf']
    dy=yr-p['yf']; dx=xr-p['xf']
    if abs(lam-m)<1e-12:
        zx=(dx+2*dy*s)*math.exp(-m*s)
    else:
        zx=dx*math.exp(-m*s)+2*dy*(math.exp(-lam*s)-math.exp(-m*s))/(m-lam)
    return math.hypot(zx,dy*math.exp(-lam*s))


def optimum_time(p,eps):
    hi=max(1.,p['tr']+1.)
    while error(p,hi)>eps: hi*=2
    return brentq(lambda t:error(p,t)-eps,0,hi,xtol=1e-12)


def asymptotic_time(p,eps):
    xr,yr=best_state(p,p['tr'])
    dx,dy=xr-p['xf'],yr-p['yf']
    lam=1/p['tau']+p['qf']; m=2*p['qf']
    if m<lam:
        return p['tr']+math.log((dx+2*dy/(lam-m))/eps)/m
    if m>lam:
        return p['tr']+math.log(dy*math.hypot(1,2/(m-lam))/eps)/lam
    l=math.log((2*dy/m)/eps)
    return p['tr']+(l+math.log(l))/m


def check():
    p=setup(1,5,1,1,1,2,4)
    def ode(t,z):
        alpha=min(p['af'],p['ai']+p['slew']*t)
        x,y=z
        return [-2*alpha*p['mu']*x+2*(p['d']+y),p['da']/p['tau']-(1/p['tau']+p['mu']*alpha)*y]
    sol=solve_ivp(ode,[0,4],[p['xi'],p['yi']],rtol=5e-12,atol=5e-13,dense_output=True)
    es=[]
    for t in np.linspace(0,4,61):
        xx,yy=best_state(p,float(t))
        es.append(max(abs(xx-sol.sol(t)[0]),abs(yy-sol.sol(t)[1])))
    assert max(es)<2e-9,(max(es),'ODE mismatch')
    assert all(error(p,float(a))>error(p,float(b)) for a,b in zip(np.linspace(.01,4,40),np.linspace(.01,4,40)[1:]))
    ee=1e-3
    t=optimum_time(p,ee)
    assert abs(error(p,t)-ee)<1e-10
    print('benchmark D=1, Da=2, mu=tau=1, ai=1, af=5, slew=4, tolerance=1e-3: minimum time=',f'{t:.12f}')
    rng=np.random.default_rng(917)
    grid=np.linspace(0,4,2001)
    star=np.stack([best_state(p,float(t)) for t in grid])
    for j in range(60):
        slopes=rng.uniform(-p['slew'],p['slew'],size=len(grid)-1)
        alphas=np.empty(len(grid)); alphas[0]=p['ai']
        dt=grid[1]-grid[0]
        for i,v in enumerate(slopes):
            alphas[i+1]=max(p['ai'],min(p['af'],alphas[i]+v*dt))
        assert np.all(alphas <= np.minimum(p['af'],p['ai']+p['slew']*grid)+1e-12)
        def ode2(t,z):
            a=np.interp(t,grid,alphas)
            x,y=z
            return [-2*p['mu']*a*x+2*(p['d']+y),p['da']/p['tau']-(1/p['tau']+p['mu']*a)*y]
        other=solve_ivp(ode2,[0,4],[p['xi'],p['yi']],t_eval=grid[::100],rtol=2e-8,atol=2e-10)
        assert np.all(other.y.T-star[::100] >=-2e-6),j
    print('60 distinct finite-slew controls dominated componentwise at 21 observation times')
    for af in [.7,1.0,1.8]:
        p=setup(.25,af,1,1,1,2,.9)
        print('terminal stiffness',af,'critical',af==1,'ramp duration',p['tr'])
        for eps in [1e-5,1e-8,1e-12,1e-17]:
            exact=optimum_time(p,eps)
            approx=asymptotic_time(p,eps)
            print(f'  eps={eps:.0e}, time={exact:.9f}, asymptotic_error={exact-approx:.5g}')
        e=abs(optimum_time(p,1e-17)-asymptotic_time(p,1e-17))
        assert e <(0.25 if af==1 else 0.003), (af,e)
    print('ALL CHECKS PASSED')


if __name__=='__main__':check()
