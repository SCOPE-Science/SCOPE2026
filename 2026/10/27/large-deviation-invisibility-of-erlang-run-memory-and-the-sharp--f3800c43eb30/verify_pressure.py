"""Reproducible matrix-spectrum checks for phase-type alternating active velocities."""
import numpy as np
from scipy.optimize import brentq
from math import sqrt


def generator(p,q,a,b):
    n=p+q
    Q=np.zeros((n,n))
    for i in range(p):
        Q[i,i]-=a
        Q[i,(i+1)%n]+=a
    for i in range(p,n):
        Q[i,i]-=b
        Q[i,(i+1)%n]+=b
    return Q


def pressure_root(p,q,a,b,v,z,with_delta=False):
    # Solve in the positive root displacement from the largest diagonal entry.
    if 2*v*z+b-a>=0:
        baseline=v*z-a
        gap=2*v*z+b-a
        def f(delta):
            return p*(np.log(delta)-np.log(a))+q*np.log((delta+gap)/b)
    else:
        baseline=-v*z-b
        gap=-2*v*z+a-b
        def f(delta):
            return p*np.log((delta+gap)/a)+q*(np.log(delta)-np.log(b))
    upper=max(a,b)
    while f(upper)<0: upper*=2
    root=brentq(f,np.nextafter(0.,1.),upper,xtol=1e-15,rtol=5e-15)
    return (baseline,root) if with_delta else baseline+root


def markov_pressure(a,b,v,z):
    return -(a+b)/2+np.sqrt((v*z+(b-a)/2)**2+a*b)


def run():
    rng=np.random.default_rng(17041)
    checks=0
    max_err=0.
    for p in range(1,5):
        for q in range(1,5):
            for _ in range(6):
                a,b=np.exp(rng.uniform(-1,1,size=2))
                v=float(np.exp(rng.uniform(-0.8,0.8)))
                z=float(rng.uniform(-4.,4.))
                Q=generator(p,q,a,b)
                diag=np.r_[np.full(p,v*z),np.full(q,-v*z)]
                lam=max(np.linalg.eigvals(Q+np.diag(diag)).real)
                root=pressure_root(p,q,a,b,v,z)
                err=abs(lam-root)
                max_err=max(max_err,err)
                assert err<1e-9, (p,q,z,lam,root)
                checks+=1
                if p==q:
                    assert abs(root-markov_pressure(a,b,v,z))<1e-9
                    checks+=1
    # Test edge exponents at moderately large tilt.
    for p,q in ((1,2),(2,1),(2,3),(3,2),(2,2)):
        a,b,v=1.3,0.8,1.2
        for theta in (1e3,1e4):
            base,delta=pressure_root(p,q,a,b,v,theta,True)
            assert abs(base-(v*theta-a))<1e-8
            asym=a*(b/(2*v*theta))**(q/p)
            assert abs(delta/asym-1)<0.05, (p,q,theta,delta,asym)
            checks+=1
            base2,delta2=pressure_root(p,q,a,b,v,-theta,True)
            assert abs(base2-(v*theta-b))<1e-8
            asym2=b*(a/(2*v*theta))**(p/q)
            assert abs(delta2/asym2-1)<0.05,(p,q,theta,delta2,asym2)
            checks+=1
    assert checks>=100
    print(f'PASS {checks} comparisons; max spectral-root absolute error {max_err:.3g}')


if __name__=='__main__':run()
