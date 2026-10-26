"""Independent elementary checks for random-size batch-reset covariance."""
from fractions import Fraction as F
from itertools import combinations
from math import exp

def moments(n, law):
    assert n >= 3 and sum(law.values()) == 1
    mu = sum(F(k)*p for k,p in law.items())
    q1 = mu/n
    q2 = sum(F(k*(k-1))*p for k,p in law.items())/F(n*(n-1))
    return q1,q2

def endpoint_laws(n,mu):
    k=mu.numerator//mu.denominator
    th=mu-k
    lo={k:1-th}
    if th:lo[k+1]=th
    hi={1:(n-mu)/F(n-1),n:(mu-1)/F(n-1)}
    return lo,hi

def ctime(t,q1,q2,r=1,D=1,steps=10000):
    lam=r*float(q1)
    mu2=r*float(2*q1-q2)
    dt=t/steps
    out=0.
    for i in range(steps):
        s=(i+.5)*dt
        v=2*D/lam*(1-exp(-lam*s))
        out+=r*float(q2)*exp(-mu2*(t-s))*v*v*dt
    return out

def main():
    checked=0
    for n in range(3,10):
        for z in range(1,4*n):
            mu=F(1)+F(z%(3*n-2),3) 
            if not 1<=mu<=n: continue
            low,high=endpoint_laws(n,mu)
            for law in (low,high):
                q1,q2=moments(n,law)
                assert q1==mu/n
                e1=e2=F(0)
                for m,p in law.items():
                    subsets=list(combinations(range(n),m))
                    e1+=p*sum(0 in s for s in subsets)/len(subsets)
                    e2+=p*sum(0 in s and 1 in s for s in subsets)/len(subsets)
                assert e1==q1 and e2==q2
                checked+=1
            assert moments(n,low)[1]<=moments(n,high)[1]
            for t in (F(1,5),F(1),F(4)):
                q1,qlo=moments(n,low); _,qhi=moments(n,high)
                clo=ctime(float(t),q1,qlo,steps=250)
                chi=ctime(float(t),q1,qhi,steps=250)
                assert chi>=clo-1e-12
                checked+=1
    # Closed stationary correlation for all deterministic sizes agrees with source.
    for n in range(3,26):
        for m in range(1,n+1):
            q1,q2=moments(n,{m:F(1)})
            stat=q2/(q1*q1*(2*q1-q2))
            source=F(n*n*(m-1),m*m*(2*n-m-1))
            assert stat==source
            checked+=1
    # Exact high-precision stationary example, n=6, mean size 2.
    n=6; lo,hi=endpoint_laws(n,F(2))
    q1,l=moments(n,lo); _,h=moments(n,hi)
    assert l==F(1,15) and h==F(1,5)
    assert (l/(2*q1-l))/5==F(1,45)
    assert (h/(2*q1-h))/5==F(3,35)
    checked+=4
    print('PASS:',checked,'exact/combinatorial/numerical assertion groups')

if __name__=='__main__': main()
