import numpy as np
from scipy.special import betainc, gammaln, expit
from scipy.integrate import quad
from scipy.special import loggamma
rng=np.random.default_rng(62701)

def cdf(alpha,m,r):
    def f(t):
        p=expit(t)
        logdensity=gammaln(2*alpha)-2*gammaln(alpha)+alpha*t-2*alpha*np.logaddexp(0,t)
        w=betainc(alpha,alpha,expit(t+r))-betainc(alpha,alpha,p)
        return np.exp(logdensity)*w**(m-1)
    return m*quad(f,-80,80,epsabs=2e-10,limit=600)[0]

for m in [2,3,6]:
 for r in [0.5,1.,2.,4.]:
    arr=[cdf(a,m,r) for a in [0.3,0.6,1.,2.,5.]]
    assert all(arr[i] < arr[i+1] for i in range(len(arr)-1)),(m,r,arr)
    print('ORDER',m,r,[round(z,8) for z in arr])
for alpha,m,r in [(0.4,3,1.5),(1.,2,1.),(1.,6,3.),(2.5,4,1.5),(6.,5,1.)]:
    n=160000
    e=rng.gamma(alpha,1,size=(n,m)); f=rng.gamma(alpha,1,size=(n,m))
    w=np.log(e)-np.log(f); D=w.max(axis=1)-w.min(axis=1)
    theoretical=cdf(alpha,m,r); emp=float(np.mean(D<=r))
    se=np.sqrt(theoretical*(1-theoretical)/n)
    assert abs(emp-theoretical) <6*se+0.0008,(alpha,m,r,emp,theoretical,se)
    print('MC',alpha,m,r,'cdf',theoretical,'empirical',emp,'se',se)
for alpha,beta in [(0.3,0.9),(0.7,1.8),(1.,2.),(2.3,3.6)]:
 for t in [0.2,1.,3.]:
    k=np.arange(40000,dtype=float)
    prod=np.sum(np.log1p(t*t/(beta+k)**2)-np.log1p(t*t/(alpha+k)**2))
    true=2*(np.real(loggamma(alpha+1j*t))-gammaln(alpha)-np.real(loggamma(beta+1j*t))+gammaln(beta))
    assert abs(prod-true)<1e-7,(alpha,beta,t,prod,true)
    print('COUPLING-CHAR',alpha,beta,t,'abs_error',abs(prod-true))
print('CHECKS PASSED')
