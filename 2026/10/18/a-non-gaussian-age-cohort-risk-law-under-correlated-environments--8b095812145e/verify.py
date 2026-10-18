"""Independent finite-state and Monte Carlo checks for a two-stage semelparous model.

Standard library only. This checks finite examples; the asymptotic theorem has an
analytical proof in RESULT.md.
"""
from itertools import product
from fractions import Fraction
from math import exp, log, pi, sqrt
import math
import random

# Python's math.logaddexp is not portable. Use an explicitly stable expression.
def logsumexp(u,v):
    m=max(u,v)
    return m+log(exp(u-m)+exp(v-m))

def direct(seq,a,b,F,s,x,y):
    for e in seq:
        x,y=F*exp(a*e)*y,s*exp(b*e)*x
    return log(x+y)

def parity(seq,a,b,F,s,x,y):
    assert len(seq)%2==0
    S=sum(seq)
    D=sum(e if (j%2==0) else -e for j,e in enumerate(seq,1))
    return len(seq)*log(F*s)/2+(a+b)*S/2+logsumexp(log(x)+(a-b)*D/2,log(y)-(a-b)*D/2)

def covariance_exact(n,q):
    rho=1-2*q
    VS=Fraction(n)
    VD=Fraction(n)
    for k in range(1,n):
        VS += 2*(n-k)*(rho**k)
        VD += 2*(n-k)*((-rho)**k)
    return VS,VD

def enumerate_cov(n,q):
    ES=ED=ESS=EDD=ESD=Fraction(0)
    for seq in product((-1,1),repeat=n):
        pr=Fraction(1,2)
        for j in range(1,n): pr*=q if seq[j]!=seq[j-1] else 1-q
        S=sum(seq); D=sum((1 if j%2==0 else -1)*v for j,v in enumerate(seq,1))
        ES+=pr*S; ED+=pr*D; ESS+=pr*S*S; EDD+=pr*D*D; ESD+=pr*S*D
    return ESS-ES*ES,EDD-ED*ED,ESD-ES*ED

def checks():
    trials=0
    for a,b,F,s,x,y in ((0.8,-0.3,2.0,0.3,1.1,0.7),(1.0,0.0,2.0,0.5,1.0,1.0),(-0.4,-0.4,1.5,0.5,0.4,2.0)):
        assert s*exp(abs(b))<=1+1e-14
        for n in (2,4,6,8,10):
            for seq in product((-1,1),repeat=n):
                if abs(direct(seq,a,b,F,s,x,y)-parity(seq,a,b,F,s,x,y))>2e-11:
                    raise AssertionError(('matrix/parity mismatch',a,b,n,seq))
                trials+=1
    print('direct products versus parity factorization:',trials,'passed')
    count=0
    for n in (2,4,6,8):
        for q in (Fraction(1,4),Fraction(1,2),Fraction(3,4)):
            vS,vD,cov=enumerate_cov(n,q)
            predictedS,predictedD=covariance_exact(n,q)
            assert (vS,vD,cov)==(predictedS,predictedD,Fraction(0)),(n,q,vS,vD,cov,predictedS,predictedD)
            count+=1
    print('exact Markov covariance identities:',count,'passed')
    a,b=0.8,-0.3
    h,d=(a+b)/2,(a-b)/2
    z=1-2/pi
    qstar=abs(h)/(abs(h)+sqrt(z)*abs(d))
    def v(q):return h*h*(1-q)/q+z*d*d*q/(1-q)
    eps=1e-6
    assert abs((v(qstar+eps)-v(qstar-eps))/(2*eps))<1e-7
    assert all(v(q)>v(qstar)+1e-7 for q in (0.1,0.2,0.3,0.6,0.7,0.9))
    print('unique variance minimizer: q* =',qstar,'V* =',v(qstar))
    rng=random.Random(142857)
    for q in (0.2,0.5,0.8):
        n=300; rep=14000
        sum_y=sum_y2=0.0
        for _ in range(rep):
            state=1 if rng.random()<0.5 else -1
            S=D=0
            for t in range(1,n+1):
                if t>1 and rng.random()<q:state=-state
                S+=state; D+=state if t%2==0 else -state
            Y=h*S+logsumexp(log(1.1)+d*D,log(0.7)-d*D)
            sum_y+=Y;sum_y2+=Y*Y
        mean=sum_y/rep/sqrt(n)
        var=(sum_y2/rep-(sum_y/rep)**2)/n
        meanlim=abs(d)*sqrt(2/pi)*sqrt(q/(1-q))
        varlim=v(q)
        assert abs(mean-meanlim)<0.045,(q,mean,meanlim)
        assert abs(var-varlim)<0.055,(q,var,varlim)
        print(f'finite-horizon q={q}: scaled mean {mean:.6f}, limit {meanlim:.6f}; scaled variance {var:.6f}, limit {varlim:.6f}')
    print('PASS: all checks. Simulations are corroborative, not infinite proofs.')

if __name__=='__main__':checks()
