import math
from scipy.optimize import brentq
from scipy.integrate import quad

def lamperti_pdf(y,mu):
    yp=y**mu; zm=(1-y)**mu
    return (math.sin(math.pi*mu)/math.pi)*(y*(1-y))**(mu-1)/(yp*yp+zm*zm+2*yp*zm*math.cos(math.pi*mu))

def tilde_free(mu,s,k):
    a=s-k
    if a<=0 or s<=0:raise ValueError
    return (a**(mu-1)+s**(mu-1))/(a**mu+s**mu)

def psi(mu,r,k):
    if k==0:return 0.
    if k>0:
        lo=max(k-r,0)
        hi=k
    else:
        lo=-r
        hi=0
    def E(s):
        q=r+s
        a=q-k
        return r*tilde_free(mu,q,k)-1
    return brentq(E,lo+1e-12,hi,xtol=1e-13,rtol=1e-14)

def rate_param(mu,r,z):
    if z==1:return .5,0,0
    a=z**(mu-1)
    d=(1+z*a)
    Q=(1-z)/d
    ap=(mu-1)*a/z
    Qp=-(1+mu*a+(1-mu)*z*a)/d**2
    s=r*a*Q
    k=r*(1+a)*Q
    x=(ap*Q+a*Qp)/(ap*Q+(1+a)*Qp)
    return x,k,s

num=0
for mu in (0.2,1/3,0.5):
    for r in (0.3,1.,2.):
        for k in (-5,-2,-0.4,0,0.3,1.3,5):
            s=psi(mu,r,k)
            if k==0: continue
            num+=1
            assert abs(s - (k+psi(mu,r,-k)))<2e-10,(mu,r,k,s,psi(mu,r,-k))
            assert abs(r*tilde_free(mu,s+r,k)-1)<3e-10
            if mu==.5:
                target=(k-2*r+math.sqrt(k*k+4*r*r))/2
                assert abs(s-target)<1e-11
    for z in (0.001,.01,.07,.2,.5,.8,1.2,2.,7.,60.,1000.):
        x,k,s=rate_param(mu,1.,z)
        num+=1
        assert 0<x<1,(mu,z,x)
        assert abs(s-psi(mu,1.,k))<1e-9,(mu,z,x,k,s,psi(mu,1.,k))
        I=k*x-s
        assert -1e-10<I<1.00000001,(mu,z,I)
        if mu==.5:
            assert abs(I-(1-2*math.sqrt(x*(1-x))))<1e-10,(mu,z,I)
    for s,k in ((1.1,0.3),(3.4,-0.7),(0.8,0.3)):
        num+=1
        def regularized(t):
            y=t**(1/mu)
            den=y**(2*mu)+(1-y)**(2*mu)+2*(y*(1-y))**mu*math.cos(math.pi*mu)
            return math.sin(math.pi*mu)/(math.pi*mu)*(1-y)**(mu-1)/den*(1/(s-k*y)+1/(s-k*(1-y)))
        val,err=quad(regularized,0,2**(-mu),epsabs=1e-11,epsrel=1e-11,limit=400)
        assert abs(val-tilde_free(mu,s,k))<2e-8,(mu,s,k,val)
    coeff=mu**(-mu)*(1-mu)**(mu-1)
    for z in (1e-3,1e-5,1e-8,1e-12):
        x,k,s=rate_param(mu,1,z)
        I=k*x-s
        delta=1-x
        ratio=(1-I)/(coeff*delta**mu)
        print('EDGE',mu,z,'delta',delta,'ratio',ratio)
        if z<=1e-12:
            assert abs(ratio-1)<.045,(mu,z,ratio)
print('PASS',num)
