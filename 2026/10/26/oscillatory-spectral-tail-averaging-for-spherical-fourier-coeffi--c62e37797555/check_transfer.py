"""Numerical cross-checks for the Bessel-square radial-to-spherical transfer theorem.
Only scientific calculations, not a substitute for the all-degree proof.
"""
import math
from scipy.integrate import quad
from scipy.special import jv, gammaln

def moment(nu,p):
    return math.exp(gammaln(p-1)+gammaln(nu+1-p/2)-(p-1)*math.log(2)-2*gammaln(p/2)-gammaln(nu+p/2))

def ap(p):
    return math.exp(gammaln(p-1)-(p-1)*math.log(2)-2*gammaln(p/2))

def integrate_f(nu,p,amp=.4,omega=.8,logpower=0):
    def f(x):
        return x*jv(nu,x)**2 * (1+x*x)**(-p/2)*(1+amp*math.cos(omega*x))*math.log(2+x)**logpower
    # consecutive segments to handle oscillations at high x
    vmax=max(400., nu*13.)
    bounds=[0.0]
    t=max(0.,nu-30.)
    if t>0:bounds.append(t)
    while bounds[-1]<vmax:
        bounds.append(min(vmax,bounds[-1]+max(10.,nu/6.)))
    z=sum(quad(f,l,h,epsabs=1e-14,epsrel=2e-9,limit=150)[0] for l,h in zip(bounds,bounds[1:]))
    return z

if __name__=='__main__':
    tests=0
    for nu,p in [(3.,4.),(4.,3.),(6.,5.5)]:
        num=quad(lambda x:x**(1-p)*jv(nu,x)**2,0,1500,epsabs=2e-12,epsrel=1e-9,limit=300)[0]
        exact=moment(nu,p)
        err=abs(num-exact)/exact
        print('MOMENT',nu,p,'ratio',num/exact,'relerror',err)
        assert err<1e-5
        tests+=1
    for p,amp,omega,k in [(4.5,0.4,0.8,0),(5.0,0.35,1.4,1)]:
        for nu in [20.,40.,80.]:
            got=integrate_f(nu,p,amp,omega,k)
            lead=ap(p)*nu**(1-p)* (math.log(nu)**k)
            ratio=got/lead
            print('TRANSFER',p,amp,omega,k,nu,'ratio',ratio)
            assert .3<ratio<1.9
            tests+=1
    print('PASS',tests,'checks')
