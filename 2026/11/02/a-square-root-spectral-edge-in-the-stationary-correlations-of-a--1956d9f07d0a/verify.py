"""Independent quadrature checks for stationary order-parameter correlations.
Usage: python verify.py. Requires mpmath >= 1.3.
"""
import mpmath as mp
mp.mp.dps = 55
checks=0

def near(x,y,tol=mp.mpf('5e-7')):
    global checks
    checks+=1
    assert abs(x-y) <= tol*max(1,abs(x),abs(y)), (x,y)

def f(t,K,sigma,initial):
    a=K/2-sigma
    b=K/2
    if abs(a) < mp.mpf('1e-25'):
        return 1/mp.sqrt(1/initial**2+K*t)
    if a<0:
        c=-a
        return initial*mp.exp(-c*t)/mp.sqrt(1+b*initial**2/c*(1-mp.exp(-2*c*t)))
    rinf=mp.sqrt(a/b)
    v=(rinf/initial)**2-1
    return rinf/mp.sqrt(1+v*mp.exp(-2*a*t))

def E(fun,lam):
    return lam*mp.quad(lambda s: mp.exp(-lam*s)*fun(s), [0,1,4,16,mp.inf])

def co(t,K,sigma,initial,lam):
    mean=E(lambda s:f(s,K,sigma,initial),lam)
    return mp.exp(-lam*t)*E(lambda s:(f(s,K,sigma,initial)-mean)*f(s+t,K,sigma,initial),lam)

lam=mp.mpf('0.7'); sig=mp.mpf('1.0'); K=2*sig; init=mp.mpf('0.8')
theta=1/(K*init**2)
mean=E(lambda s:f(s,K,sig,init),lam)
closed=mp.sqrt(mp.pi*lam/K)*mp.exp(lam*theta)*mp.erfc(mp.sqrt(lam*theta))
near(mean,closed,mp.mpf('1e-35'))
muprime=(theta+1/(2*lam))*closed-mp.sqrt(theta/K)
near(muprime,-E(lambda s:(s-1/lam)*f(s,K,sig,init),lam),mp.mpf('1e-35'))
amp=muprime/(2*mp.sqrt(K))
assert amp>0
checks+=1
for t in [30,60,120,250]:
    t=mp.mpf(t)
    scaled=co(t,K,sig,init,lam)*mp.exp(lam*t)*t**mp.mpf('1.5')
    checks+=1
    assert abs(scaled/amp-1)<mp.mpf('0.15')*(mp.mpf('30')/t)
    print('critical t',str(t),'scaled/asymptote',mp.nstr(scaled/amp,12))
for kval,initval in [(mp.mpf('1.6'),mp.mpf('.8')),(mp.mpf('2.4'),mp.mpf('.8')),(mp.mpf('2.4'),mp.mpf('.2'))]:
    a=kval/2-sig; b=kval/2
    mu=E(lambda s:f(s,kval,sig,initval),lam)
    if a<0:
        decay=-a
        const=initval/mp.sqrt(1+b*initval**2/(-a))
    else:
        decay=2*a
        rinf=mp.sqrt(a/b)
        v=(rinf/initval)**2-1
        const=-rinf*v/2
    coef=const*E(lambda s:(f(s,kval,sig,initval)-mu)*mp.exp(-decay*s),lam)
    assert coef>0
    checks+=1
    for t in [30,60,120]:
        raw=co(mp.mpf(t),kval,sig,initval,lam)
        assert raw>0
        checks+=1
        scaled=raw*mp.exp((lam+decay)*t)
        checks+=1
        assert abs(scaled/coef-1)<mp.mpf('0.1')
    print('offcritical',mp.nstr(kval),mp.nstr(initval),'coefficient',mp.nstr(coef,12))
# At a stable resetting value, stationary order parameter is constant, so all covariances vanish.
kval=mp.mpf('2.4'); initval=mp.sqrt((kval/2-sig)/(kval/2))
for t in [0,1,10]:
    near(co(mp.mpf(t),kval,sig,initval,lam),0,mp.mpf('1e-35'))
# Positive Laplace spectral density reproduces the critical time covariance.
mp.mp.dps=30
def rho(v):
    return (lam/(mp.pi*K))*mp.sqrt(v)*mp.exp(-theta*v)/(lam+v)*mp.quad(
        lambda u: mp.sqrt(u)*mp.exp(-theta*u)/((lam+u+v)*(lam+u)),
        [0,1,5,mp.inf])
for vv in [mp.mpf('.1'),mp.mpf('.3'),mp.mpf('1')]:
    assert rho(vv)>0
    checks+=1
spectral=mp.quad(lambda v:mp.exp(-2*v)*rho(v),[0,mp.mpf('.25'),1,5,mp.inf]);
direct=co(mp.mpf('2'),K,sig,init,lam)*mp.exp(2*lam)
near(spectral,direct,mp.mpf('1e-20'))
print('PASS:',checks,'quadrature, spectral, derivative, sign, and asymptotic checks')
