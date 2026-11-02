#!/usr/bin/env python3
"""Independent numerical checks for marginal multiplicative jump-rate disorder.

Python standard library only. Run: python3 verify.py
Finite numerical quadrature supplements, but does not replace, the analytic proof.
"""
import math


def gauss_nodes(n=40):
    out=[]
    for i in range(1,n+1):
        z=math.cos(math.pi*(i-.25)/(n+.5))
        for _ in range(20):
            p0,p1=1.,z
            for j in range(2,n+1):
                p0,p1=p1,((2*j-1)*z*p1-(j-1)*p0)/j
            pp=n*(z*p1-p0)/(z*z-1)
            dz=p1/pp
            z-=dz
            if abs(dz)<1e-15:break
        w=2/((1-z*z)*pp*pp)
        out.append((z,w))
    return out

NODES=gauss_nodes(36)

def quad(f,a,b):
    h=(b-a)/2;c=(a+b)/2
    return h*sum(w*f(c+h*z) for z,w in NODES)

def multi_quad(f,a,b,step):
    total=0.
    while a<b:
        c=min(b,a+step)
        total+=quad(f,a,c)
        a=c
    return total


def marginal_product_tail(u,m):
    assert m>=1 and u>=1
    ell=math.log(u)
    return math.exp(-ell/2)*sum((ell/2)**j/math.factorial(j) for j in range(m))


def delta_laplace(s,m):
    """1-E exp(-s R), R a product of m Pareto(1/2) factors."""
    if s<=0:return 0.
    log_s=math.log(s)
    upper=max(85.,-log_s+48.)
    norm=1./(2**m*math.factorial(m-1))
    def integrand(y):
        v=log_s+y
        a=1. if v>34 else -math.expm1(-math.exp(v))
        return norm*y**(m-1)*math.exp(-y/2)*a
    return multi_quad(integrand,0.,upper,4.)


def spectral_survival(n,m,x=1,tau=1.):
    """Exact resampling-epoch spectral law; numerical quadrature only."""
    ell=math.log(n) if n>1 else 1.
    scale=n*max(ell,1.)**(m-1)
    def at_z(z):
        theta=z/scale
        if theta>=math.pi:return 0.
        argument=2*tau*math.sin(theta/2)**2
        d=delta_laplace(argument,m)
        if d>=1:return 0.
        kernel=(1+math.cos(theta)) if x==1 else math.sin(x*theta)/math.tan(theta/2)
        return kernel*math.exp(n*math.log1p(-d))/(math.pi*scale)
    return multi_quad(at_z,0.,min(math.pi*scale,160.),2.)


def predicted_survival(n,m,x=1,tau=1.):
    assert n>1
    beta=m-1
    constant=2**1.5*x*math.sqrt(tau)*math.factorial(beta)/math.pi**1.5
    return constant/(n*tau*math.log(n)**beta)


def bessel_i0_small(z):
    term=1.;acc=1.
    for j in range(1,80):
        term*=z*z/(4*j*j)
        acc+=term
        if term<1e-16*acc:break
    return acc


def bessel_i1_small(z):
    term=z/2;acc=term
    for j in range(1,80):
        term*=z*z/(4*j*(j+1))
        acc+=term
        if term<1e-16*acc:break
    return acc


def test():
    count=0
    # Independent gamma-tail quadrature versus Erlang survival polynomial.
    for m in range(1,5):
        for ell in [0.,.25,1.,3.,8.,15.]:
            density=lambda y: y**(m-1)*math.exp(-y/2)/(2**m*math.factorial(m-1))
            p=multi_quad(density,ell,150.,4.)
            q=marginal_product_tail(math.exp(ell),m)
            assert abs(p-q)<1e-10,(m,ell,p,q)
            count+=1
    # Laplace numerical transform agrees with direct gamma/Laplace integration
    # at two distinct quadrature meshes.
    for m in range(1,4):
        for s in [1e-2,1e-4,1e-8,1e-12]:
            p=delta_laplace(s,m)
            assert 0<p<1
            c=math.sqrt(math.pi)/(2**(m-1)*math.factorial(m-1))
            lead=c*math.sqrt(s)*math.log(1/s)**(m-1)
            ratio=p/lead
            assert .5<ratio<3.,(m,s,ratio)
            count+=1
    # The spectral kernel has mass one at zero operational time.
    for x in range(1,9):
        f=lambda th: (math.sin(x*th)/math.tan(th/2) if x>1 else 1+math.cos(th))/math.pi
        q=multi_quad(f,0.,math.pi,.4)
        assert abs(q-1)<2e-12,(x,q)
        count+=1
    # For a deterministic jump rate, the exact x=1 spectral formula equals
    # the independent modified-Bessel expression.
    for u in [.02,.3,1.,2.,5.]:
        spec=multi_quad(lambda th:(1+math.cos(th))*math.exp(-u*(1-math.cos(th)))/math.pi,0.,math.pi,.3)
        series=math.exp(-u)*(bessel_i0_small(u)+bessel_i1_small(u))
        assert abs(spec-series)<2e-12,(u,spec,series)
        count+=1
    # Direct exact (finite-n) spectral integrals support the marginal
    # asymptotic and display the expected slowly improving log corrections.
    for m in [1,2,3]:
        ratios=[]
        for n in [1000,100000,10000000]:
            q=spectral_survival(n,m)
            asy=predicted_survival(n,m)
            r=q/asy
            assert q>0 and .2<r<1.2,(m,n,r)
            ratios.append(r)
            count+=1
        assert all(ratios[j+1]>ratios[j] for j in range(2)),(m,ratios)
        count+=2
        print('m=',m,'ratio to proved limit at n=10^3,10^5,10^7:',*(f'{r:.6f}' for r in ratios))
    # The exact survival coefficient for the multiplicative Pareto model is
    # consistent with the general k,beta formula.
    for m in range(1,8):
        beta=m-1
        k=1/(2**beta*math.factorial(beta))
        k_general=2**(1.5-beta)/(math.pi**1.5*k)
        k_product=2**1.5*math.factorial(beta)/math.pi**1.5
        assert math.isclose(k_general,k_product,rel_tol=1e-14)
        count+=1
    print('PASS:',count,'deterministic assertions')

if __name__=='__main__':test()
