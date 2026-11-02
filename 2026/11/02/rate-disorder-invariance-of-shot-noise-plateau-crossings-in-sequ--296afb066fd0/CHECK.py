"""Independent checks of renewal current noise against Markov-generator resolvents.
Numerics support but do not replace the Hurwitz stability and phase proof.
"""
import math
import numpy as np
from itertools import combinations

def elementary(rates, k):
    return sum(math.prod(xs) for xs in combinations(rates, k))

def renewal(rates, omega):
    rates = np.array(rates, dtype=float)
    prod = np.prod(rates)
    z = np.prod(rates + 1j*omega)
    return (abs(z)**2-prod**2) / abs(z-prod)**2

def generator(rates, omega):
    n=len(rates)
    Q=np.zeros((n,n))
    for j,r in enumerate(rates):
        Q[j,j]-=r
        Q[j,(j+1)%n]+=r
    # Under row generator: conditional rate for a marked jump at t>0 from initial post-jump state 0
    # is rho_{n-1} times [exp(tQ)]_{0,n-1}.
    M=np.linalg.solve(1j*omega*np.eye(n)-Q,np.eye(n))
    return 1 + 2*np.real(rates[-1]*M[0,n-1])

def roots(rates):
    n=len(rates)
    # Re P(i omega)-P(0) = -e_{n-2} omega^2 + e_{n-4} omega^4 - ... .
    # Positive roots in x=omega^2, after factoring x.
    m=n//2
    coef=[(-1)**k*elementary(rates,n-2*k) for k in range(1,m+1)]
    poly=list(reversed(coef))
    rr=np.roots(poly)
    good=[]
    for x in rr:
        assert abs(x.imag)<1e-6, (rates,rr)
        assert x.real>0,(rates,rr)
        good.append(math.sqrt(x.real))
    return sorted(good)

def check():
    rng=np.random.default_rng(89273)
    checks=0
    for n in range(2,12):
        for run in range(6):
            rates=np.exp(rng.uniform(-1.2,1.2,n)) if run <5 else np.geomspace(.4,5.0,n)
            zero=roots(rates)
            assert len(zero)==n//2-1,(rates,zero)
            checks+=1
            for freq in np.geomspace(.07,40,31):
                a=renewal(rates,freq)
                b=generator(rates,freq)
                assert abs(a-b)<3e-9, (n,rates,freq,a,b)
                checks+=1
            for j,omega in enumerate(zero):
                assert abs(renewal(rates,omega)-1)<1e-8,(rates,omega)
                checks+=1
                gap=min([omega, *[abs(omega-y) for k,y in enumerate(zero) if k!=j]])
                left=renewal(rates,omega-min(.03*gap,.01))-1
                right=renewal(rates,omega+min(.03*gap,.01))-1
                assert left*right <0,(rates,omega,left,right)
                checks+=1
            assert renewal(rates,1e-3)<1
            checks+=1
    assert roots([1,1,1,1]) == [math.sqrt(6)]
    checks+=1
    print(f'CHECKER PASS: {checks} assertions, n=2..11, 6 heterogeneous rate profiles each; renewal vs generator; spectral plateau crossings')

if __name__=='__main__':
    check()
