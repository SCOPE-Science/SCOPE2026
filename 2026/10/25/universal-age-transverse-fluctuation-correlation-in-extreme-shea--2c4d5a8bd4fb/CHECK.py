"""Deterministic verification of the analytic shear-reset excursion theorem.

Requires Python 3, NumPy and SciPy. Numerical quadrature is corroboration,
not a substitute for the asymptotic Laplace-method proof in RESULT.md.
"""
import math
import numpy as np
from scipy.special import log_ndtr
from scipy.stats import norm
from scipy.integrate import simpson, quad

assertions = 0

def check(test, message):
    global assertions
    assertions += 1
    if not bool(test):
        raise AssertionError(message)


def moments(x, D, r, gamma):
    a = (9.0 / (4*D*gamma**2*r))**0.25
    zscale = math.sqrt(a/(4*r))
    t = np.linspace(max(1e-8, a*math.sqrt(x)-12*zscale*x**0.25),
                    a*math.sqrt(x)+12*zscale*x**0.25, 7001)
    V = 2*D*(t+gamma**2*t**3/3)
    C = D*gamma*t**2
    Z = x/np.sqrt(V)
    lw = np.log(r)-r*t+log_ndtr(-Z)
    w = np.exp(lw-lw.max())
    Q = simpson(w, x=t)
    p = w/Q
    tail_log = lw.max()+np.log(Q)
    MX = np.sqrt(V)*np.exp(norm.logpdf(Z)-log_ndtr(-Z))
    t1 = simpson(t*p,x=t)
    t2 = simpson(t**2*p,x=t)
    ym = (C/V)*MX
    y1 = simpson(ym*p,x=t)
    ty = simpson(t*ym*p,x=t)
    y2 = simpson((2*D*t-C**2/V + (C/V)**2*V*(1+Z*np.exp(norm.logpdf(Z)-log_ndtr(-Z))))*p,x=t)
    corr = (ty-t1*y1)/math.sqrt((t2-t1*t1)*(y2-y1*y1))
    conditional_x_path = []
    conditional_y_path = []
    for u in [0.0, 0.2, 0.5, 0.8, 1.0]:
        CX=2*D*u*t+2*D*gamma**2*t**3*(u*u/2-u**3/6)
        CY=2*D*gamma*t*t*(u-u*u/2)
        conditional_x_path.append(simpson((CX/V)*MX*p,x=t)/x)
        conditional_y_path.append(simpson((CY/V)*MX*p,x=t)/math.sqrt(x))
    return dict(a=a,log_tail=tail_log,age_mean=t1,y_mean=y1,corr=corr,
                xpath=conditional_x_path,ypath=conditional_y_path)

for D,r,g in [(1,1,1), (1.5,.6,-2), (.4,1.7,.8)]:
    a=(9/(4*D*g*g*r))**.25
    c=3/(2*g*a)
    rate=4*r*a/3
    check(abs(4*D*g*g*r*a**4/9-1)<1e-12,'saddle equation')
    check(abs((4*r/a)*a/(4*r)-1)<1e-12,'Laplace width')
    check(abs((c*c/(4*r*a))/(D*a/4)-1)<1e-12,'fluctuation decomposition')
    check(abs((c*c/(4*r*a)+D*a/2)/(3*D*a/4)-1)<1e-12,'endpoint variance')
    for x in [10000.,100000.]:
        z=moments(x,D,r,g)
        check(abs(math.exp(z['log_tail']+rate*math.sqrt(x))/(math.sqrt(6)/4)-1)<0.03, 'tail constant')
        check(abs(z['age_mean']/(a*math.sqrt(x))-1)<.025,'age concentration')
        check(abs(z['y_mean']/(c*math.sqrt(x))-1)<.025,'transverse concentration')
        check(abs(z['corr']+math.copysign(1,g)/math.sqrt(3))<.05,'universal correlation')
        for j,u in enumerate([0.,.2,.5,.8,1.]):
            check(abs(z['xpath'][j]-(3*u*u-u**3)/2)<.035,'cubic path')
            check(abs(z['ypath'][j]/c-(2*u-u*u))<.025,'parabolic path')

# Covariance formulas reconstructed by independent kernel integration.
for D,r,g in [(1,1,1), (1.5,.6,-2), (.4,1.7,.8)]:
    for t in [.75, 3.5, 11.0]:
        V=2*D*(t+g*g*t**3/3)
        Vintegral=2*D*t+2*D*g*g*quad(lambda s:(t-s)**2,0,t)[0]
        check(abs(V-Vintegral)<1e-10,'variance kernel')
        for u in [.17,.4,.74,1.]:
            CY=2*D*g*quad(lambda s: min(u*t,s),0,t,epsabs=1e-10,points=[u*t] if u<1 else None)[0]
            CY_closed=2*D*g*t*t*(u-u*u/2)
            check(abs(CY-CY_closed)<1e-9,'vertical path covariance')
            CX=2*D*u*t+2*D*g*g*quad(lambda s:(u*t-s)*(t-s),0,u*t)[0]
            CX_closed=2*D*u*t+2*D*g*g*t**3*(u*u/2-u**3/6)
            check(abs(CX-CX_closed)<1e-9,'horizontal path covariance')

print('PASS:', assertions,'deterministic assertions')
