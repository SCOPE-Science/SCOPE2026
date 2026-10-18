"""Deterministic finite checks of the two-edge weak-reinforcement WARM reduction.
Not a certificate of any infinite-time limit.
"""
import math
from fractions import Fraction

def f(x, alpha):
    return ((1+x)**alpha-(1-x)**alpha)/((1+x)**alpha+(1-x)**alpha)

def prob_plus(w1,w2,alpha,p0,p):
    R=p0+2*p
    return (p+ p0*w1**alpha/(w1**alpha+w2**alpha))/R

def recurrence_expect(w1,w2,alpha,p0,p):
    c=p0/(p0+2*p)
    x=(w1-w2)/(w1+w2)
    return c*f(x,alpha)

def dp(n,alpha,p0=4,p=1):
    # Equal integer initial weights 1,1; after n events W1=1+k,W2=1+n-k.
    P=[1.0]
    for step in range(n):
        N=[0.0]*(step+2)
        for k,pr in enumerate(P):
            qp=prob_plus(k+1,step-k+1,alpha,p0,p)
            N[k]+=pr*(1-qp)
            N[k+1]+=pr*qp
        P=N
    return P

def main():
    count=0
    for p0,p in [(1,1),(4,1),(9,2)]:
        for alpha in [0,0.2,0.5,0.75,0.95]:
            for w1 in [1,2,4,10,31]:
                for w2 in [1,3,5,11]:
                    prob=prob_plus(w1,w2,alpha,p0,p)
                    drift=2*prob-1
                    target=recurrence_expect(w1,w2,alpha,p0,p)
                    assert abs(drift-target)<1e-12
                    assert 0<prob<1
                    assert abs((1-drift**2)-(4*prob*(1-prob)))<1e-12
                    count+=3
    for alpha in [0,0.4,0.7,0.75,0.9]:
        probs=dp(500,alpha)
        assert abs(sum(probs)-1)<1e-12
        mean=sum((2*k-500)*q for k,q in enumerate(probs))
        assert abs(mean)<1e-10
        second=sum((2*k-500)**2*q for k,q in enumerate(probs))
        assert 0<second<500**2
        print(f'alpha={alpha:.2f} varD500={second:.6f} varD500/n={second/500:.6f}')
        count+=3
    # At zero reinforcement, D is a sum of n independent symmetric +/-1 signs.
    for n in [20,60,100,200,500]:
        probabilities=dp(n,0)
        exact=[math.comb(n,k)/2**n for k in range(n+1)]
        assert max(abs(a-b) for a,b in zip(probabilities,exact))<1e-13
        count+=1
    # At alpha < 1, f(x) is strictly inside the line x for x>0 and derivative at 0 alpha.
    for alpha in [0.15,0.5,0.9]:
        for x in [0.05,0.2,0.5,0.85]:
            assert 0<f(x,alpha)<x
            count+=1
        assert abs(f(1e-6,alpha)/1e-6-alpha)<1e-9
        count+=1
    print('VERIFY_OK',count)

if __name__=='__main__':main()
