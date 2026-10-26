"""Independent numerical checks for drifted Brownian local-time killing with Poisson restart."""
import math
from scipy.optimize import brentq, minimize_scalar
from scipy.integrate import quad

def H(rho,a,kappa):
    u=math.sqrt(a*a+rho)
    z=a+u
    return math.expm1(z)+u*math.exp(z)/kappa

def m(rho,a,kappa):
    return H(rho,a,kappa)/rho

def J(rho,a,kappa):
    u=math.sqrt(a*a+rho)
    return rho*math.exp(a+u)*(1+(u+1)/kappa)/(2*u)-H(rho,a,kappa)

def root(a,k):
    lo=1e-12
    hi=100.0
    while J(hi,a,k)<0:hi*=2
    return brentq(lambda x:J(x,a,k),lo,hi,xtol=1e-14,rtol=8.9e-15)

def check():
    count=0
    for a in [-5,-2,-1,-.5,0,.5,2,5]:
        for k in [.02,.2,2,20,2e4]:
            r=root(a,k)
            assert J(r*.9,a,k)<0 and J(r*1.1,a,k)>0
            assert m(r*.9,a,k)>m(r,a,k) and m(r*1.1,a,k)>m(r,a,k)
            assert abs((m(r*(1+1e-5),a,k)-m(r*(1-1e-5),a,k))/(2e-5*r)) < 1e-3*max(1,m(r,a,k))
            count+=3
    for b in [1.2,1.5,2.0,3.0]:
        for k in [1e5,1e7,1e9]:
            rr=root(-b,k)
            pred=math.sqrt(8*b**4/((b-1)*k))
            rel=abs(rr/pred-1)
            assert rel<.14,(b,k,rr,pred,rel)
            count+=1
    for k in [1e4,1e6,1e8]:
        rr=root(-1,k)
        pred=(24/k)**(1/3)
        assert abs(rr/pred-1)<.09,(k,rr,pred)
        count+=1
    for lam in [-4,-2,0,2,4]:
        for k in [1e6,1e9]:
            eps=k**(-1/3); b=1+lam*eps
            t=brentq(lambda t:t**3+3*lam*t*t-24,max(0,-3*lam)+1e-12,100)
            rr=root(-b,k)
            pred=eps*t
            assert abs(rr/pred-1)<.15,(lam,k,rr,pred)
            count+=1
    for a in [-1.9,-.5,0,.5,2]:
        for k in [.1,1,10]:
            r=root(a,k)
            for factor in [.1,.5,.9,1.1,3,10]:
                assert m(factor*r,a,k)>m(r,a,k)-1e-11
                count+=1
    print('PASS numerical derivative signs, unique-root brackets, asymptotics, crossover:',count,'assertions')
    for b in [.5,1,2]:
        for k in [1e3,1e6,1e9]:
            rr=root(-b,k)
            print(f'b={b} k={k:.0e} rho_opt={rr:.11g}')
    for lam in [-3,0,3]:
        k=1e9; eps=k**(-1/3); b=1+lam*eps
        t=brentq(lambda t:t**3+3*lam*t*t-24,max(0,-3*lam)+1e-12,100)
        rr=root(-b,k)
        print(f'lambda={lam:+d}, crossover t={t:.8g}, scaled numerical={rr/eps:.8g}')

def check_resolvent():
    # Independent Gaussian transition-density integral, not the derivative formula.
    checks=0
    for v in [-3., -1., 0., 1., 3.]:
        for rate in [0.3, 2., 5.]:
            x0=1.; diffusion=1.
            integrand=lambda t: math.exp(-((x0+v*t)**2)/(4*diffusion*t)-rate*t)/math.sqrt(4*math.pi*diffusion*t)
            green,_=quad(integrand,0,math.inf,epsabs=5e-11,limit=250)
            expected=math.exp(-(v+math.sqrt(v*v+4*diffusion*rate))*x0/(2*diffusion))/math.sqrt(v*v+4*diffusion*rate)
            assert abs(green-expected)<2e-9
            for sink in [0.4, 1.8, 10.]:
                from_integral=sink*green/(1+sink/math.sqrt(v*v+4*diffusion*rate))
                closed=sink*math.exp(-(v+math.sqrt(v*v+4*diffusion*rate))*x0/(2*diffusion))/(sink+math.sqrt(v*v+4*diffusion*rate))
                assert abs(from_integral-closed)<2e-9
                checks+=1
    print('PASS independent Brownian resolvent quadratures:', checks)

if __name__=='__main__':
    check()
    check_resolvent()
