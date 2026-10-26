"""Independent finite-state and conditional-hazard checks for a directed two-class SIS model."""
import math
import numpy as np
from scipy.linalg import expm


def finite_chain(m,n,lam,mu,t):
    states=[(i,j) for i in range(m+1) for j in range(n+1)]
    index={x:k for k,x in enumerate(states)}
    Q=np.zeros((len(states),len(states)))
    for k,(a,b) in enumerate(states):
        moves=[]
        if a>0: moves.append(((a-1,b),a))
        if b>0: moves.append(((a,b-1),mu*b))
        if a>0 and b<n: moves.append(((a,b+1),lam*a*(n-b)/m))
        for state,r in moves:
            Q[k,index[state]]+=r
            Q[k,k]-=r
    trans=expm(t*Q)[index[(m,0)]]
    return trans[index[(0,0)]],sum(p*b for p,(a,b) in zip(trans,states)),sum(p for p,(a,b) in zip(trans,states) if a>0)


def upper_mean(m,n,lam,mu,t):
    delta=mu-1
    kernel=(-math.expm1(-delta*t)/delta)*math.exp(-t) if abs(delta)>1.e-8 else t*math.exp(-t)
    # Equivalent to e^{-mu*t} integral e^{(mu-1)s} ds; stable for any mu near 1.
    if abs(delta)>1e-8:
        kernel=math.exp(-mu*t)*math.expm1(delta*t)/delta
    else:
        kernel=t*math.exp(-t)
    return n*lam*kernel


def saturation_bound(m,n,lam,mu,t):
    # E[n(q0-q)] <= n*lambda^2*e^{-mu*t} * integral of E[A(s) A(u)]/m^2 * e^{mu*s}.
    # Numerical one-dimensional deterministic quadrature; deliberately distinct from generator.
    from scipy.integrate import quad
    def integrand(s):
        return math.exp(mu*s)*((1-1/m)*math.exp(-s)*(math.exp(-s)-math.exp(-t))
                            +(math.exp(-s)-math.exp(-t))/m)
    return n*lam**2*math.exp(-mu*t)*quad(integrand,0,t,epsabs=1e-12)[0]


def exact_conditional_q(lifetimes,t,lam,mu):
    m=len(lifetimes); ds=np.sort(lifetimes[lifetimes<t]); q=0.; prev=0.; a=m
    for d in np.append(ds,t):
        h=lam*a/m; k=h+mu; gap=d-prev
        q=q*math.exp(-k*gap)+(h/k)*(-math.expm1(-k*gap))
        prev=d; a-=1
    return q, int(np.sum(lifetimes>t))


def main():
    tests=0
    for m in (2,3,4,5):
      for n in (2,3,4):
        for lam in (0.4,1.3):
          for mu in (0.8,1.0,1.4):
            for t in (0.7,1.5):
                cdf,mean_b,alive_a=finite_chain(m,n,lam,mu,t)
                ub=upper_mean(m,n,lam,mu,t)
                err=saturation_bound(m,n,lam,mu,t)
                assert -2e-10<=ub-mean_b<=err+2e-10, (m,n,lam,mu,t,mean_b,ub,err)
                assert abs(alive_a-(1-(1-math.exp(-t))**m))<1e-10
                assert 0<cdf<1
                tests+=1
    print('PASS: ',tests,'finite-generator inequalities, source-survival identities, and positivity cases')
    rng=np.random.default_rng(20261019)
    for theta in (-2.,0.,2.):
        n=m=2200; lam=1.4; t=math.log(n)+math.log(math.log(n))
        mu=1+theta/math.log(n)
        ps=[]; ca=[]
        for _ in range(350):
            lifetimes=rng.exponential(1,size=m)
            q,na=exact_conditional_q(lifetimes,t,lam,mu)
            ps.append((1-q)**n);ca.append(na)
        pred=math.exp(-lam*((1-math.exp(-theta))/theta if theta else 1.))
        measured=np.mean(ps)
        print(f'theta={theta:+.0f} n={n}: finite conditional extinction CDF {measured:.6f}, limit {pred:.6f}, source survivors {np.mean(ca):.3f}')
        assert abs(measured-pred)<.17
    print('PASS: 3 large-system near-resonance checks (finite-n comparisons only, not a proof)')
if __name__=='__main__': main()
