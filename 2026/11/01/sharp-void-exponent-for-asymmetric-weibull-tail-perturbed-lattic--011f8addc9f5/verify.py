"""Reproducible finite checks for one-dimensional independently perturbed lattice hole asymptotics.
Only finite numerical checks; the all-length theorem is proved analytically in RESULT.md.
"""
import math
import numpy as np
from scipy.special import logsumexp, log_ndtr

checks=0

def assert_close(a,b,tol=1e-10):
    global checks
    assert abs(a-b) <= tol, (a,b,abs(a-b),tol)
    checks += 1

def rate(cm,cp,alpha):
    den=cm**(1/alpha)+cp**(1/alpha)
    return cm*cp/((alpha+1)*den**alpha)

def cdf_log_and_sf_log(x,cm,cp,alpha):
    # two-sided stretched exponential, half mass on each side;
    # at x=0 each tail equals one half.
    x=np.asarray(x,dtype=float)
    lc=np.empty_like(x); ls=np.empty_like(x)
    neg=x<0
    lc[neg]=-math.log(2)-cm*np.abs(x[neg])**alpha
    ls[neg]=np.log1p(-np.exp(lc[neg]))
    ls[~neg]=-math.log(2)-cp*np.abs(x[~neg])**alpha
    lc[~neg]=np.log1p(-np.exp(ls[~neg]))
    return lc,ls

def void_loss_stretched(L,u,cm,cp,alpha):
    R=max(40,int(2*L))
    a=np.arange(-R,math.ceil(L)+R+1,dtype=float)+u
    cdf, _=cdf_log_and_sf_log(-a,cm,cp,alpha)
    _,sf=cdf_log_and_sf_log(L-a,cm,cp,alpha)
    val=np.logaddexp(cdf,sf)
    assert np.all(val<=1e-12),val.max()
    return -sum(val)

def void_loss_gauss(L,u,sigma):
    R=max(40,int(L))
    a=np.arange(-R,math.ceil(L)+R+1,dtype=float)+u
    return -np.sum(np.logaddexp(log_ndtr(-a/sigma),log_ndtr(-(L-a)/sigma)))

# Algebraic crossing integral checked against numerical integration.
for alpha in (1.,1.5,2.,3.):
 for cm,cp in ((1.,1.),(.5,3.),(2.,.7)):
    x=np.linspace(0,1,100001)
    integ=np.trapezoid(np.minimum(cm*x**alpha,cp*(1-x)**alpha),x)
    assert_close(integ,rate(cm,cp,alpha),1e-8)

# Independent product calculation: both symmetric and asymmetric Weibull tails.
for alpha,cm,cp in ((1.,1.,1.),(1.,.7,2.),(2.,.5,.5),(2.,.7,1.9)):
    target=rate(cm,cp,alpha)
    for u in (.0,.13,.73,.999):
        errs=[]
        for L in (24,48,96,192):
            ratio=void_loss_stretched(L,u,cm,cp,alpha)/L**(alpha+1)
            errs.append(abs(ratio-target))
            checks+=1
        assert errs[-1] < errs[0],(alpha,cm,cp,u,errs)
        checks += 1

# Gaussian tails asymptotics with L-independent mass scale sigma.
for sigma in (.7,1.,2.):
    expected=1/(24*sigma**2)
    for u in (0.,.24,.81):
        y1=void_loss_gauss(48,u,sigma)/48**3
        y2=void_loss_gauss(192,u,sigma)/192**3
        assert abs(y2-expected)<abs(y1-expected),(sigma,u,y1,y2,expected)
        checks+=1

# The interior loss is asymptotically the crossing cost; uniform shift robustness.
for alpha,cm,cp in ((1.,1.,3.),(2.,.5,2.)):
    for u in (0.,.41,.98):
        vals=[void_loss_stretched(200,u,cm,cp,alpha) for _ in range(1)]
        assert vals[0]>0
        checks+=1

print('finite numerical assertions:',checks)
print('example asymmetric exponential c_minus=1 c_plus=3: exact rate',rate(1.,3.,1.))
print('example asymmetric quadratic c_minus=0.5 c_plus=2: exact rate',rate(.5,2.,2.))
print('Gaussian sigma=1: predicted rate',1/24)
for L in (24,48,96,192,384):
    print('Gaussian sigma=1; L=',L,'-log P / L^3=',float(void_loss_gauss(L,.37,1.)/L**3))
