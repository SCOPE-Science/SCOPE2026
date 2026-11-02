"""Standalone finite checks for the one-defect continuous-time directed-cycle theorem.
Run: python verify.py. Standard library only.
"""
from fractions import Fraction as F
from math import sqrt, isclose
import random


def kemeny_from_rates(rates):
    t=[F(1,1)/r for r in rates]
    T=sum(t)
    return sum(t[i]*t[j] for i in range(len(t)) for j in range(i+1,len(t)))/T


def hitting_kemeny(rates, start):
    n=len(rates)
    t=[F(1,1)/r for r in rates]
    T=sum(t)
    ret=F(0)
    for j in range(n):
        wait=sum(t[(start+v)%n] for v in range((j-start)%n))
        ret+=t[j]*wait/T
    return ret


def optimum_ratio(n, price):
    k=n-1
    qc=F(k*(k+1),2)
    if price >= qc: return None
    return (sqrt(float(F(k+1,k-1)*(k*k-price)/price))-1)/k


def float_cost_and_k(n, q, u, budget=1.0):
    k=n-1
    x=budget/(k+q*u)
    y=u*x
    return (k*x+q*y, k*(k+q*u)*((k-1)*u+2)/(2*budget*(k*u+1)))


def run():
    rng=random.Random(20261030)
    checks=0
    # Exact rational chain identity for all starting vertices and random rates.
    for n in range(3,15):
        for _ in range(45):
            rates=[F(rng.randrange(1,35),rng.randrange(1,35)) for _ in range(n)]
            val=kemeny_from_rates(rates)
            for start in range(n):
                assert hitting_kemeny(rates,start)==val
                checks+=1
    # Exact pair smoothing for arbitrary others: equal-price rate sum is invariant.
    for n in range(3,13):
        for _ in range(100):
            rates=[F(rng.randrange(1,30),rng.randrange(1,20)) for _ in range(n)]
            rates[0]=F(rng.randrange(1,30),rng.randrange(1,20))
            rates[1]=F(rng.randrange(1,30),rng.randrange(1,20))
            pre=kemeny_from_rates(rates)
            rate_avg=(rates[0]+rates[1])/2
            candidate=[rate_avg,rate_avg]+rates[2:]
            post=kemeny_from_rates(candidate)
            assert post<=pre
            if rates[0]!=rates[1]: assert post<pre
            assert candidate[0]+candidate[1]==rates[0]+rates[1]
            checks+=3
    # Positive-ratio stationarity and global comparisons for many costs and n.
    for n in range(3,31):
        k=n-1
        qc=k*(k+1)/2
        for price in [0.0125,0.1,0.7,1.0,1.3,2.0,3.0,qc*.2,qc*.8,qc*.999,qc,qc*1.1,qc*5]:
            ratio=optimum_ratio(n,F(str(price)))
            if ratio is not None:
                assert ratio>0
                eq=price*(k*(k-1)*ratio**2+2*(k-1)*ratio+2)-k*(k+1)
                assert abs(eq)<1e-8*max(1,k*k)
                cost,K=float_cost_and_k(n,price,ratio)
                assert isclose(cost,1.0,abs_tol=1e-12)
                for frac in [.01,.05,.1,.5,.9,1.1,1.5,2,4,10,100]:
                    _,K2=float_cost_and_k(n,price,ratio*frac)
                    assert K2>=K-1e-10
                    checks+=1
                checks+=3
            else:
                assert price >= qc-1e-12
                boundary=k*k
                old=None
                for u in [1, .1, .01, .001, .00001, .00000001]:
                    _,val=float_cost_and_k(n,price,u)
                    assert val>boundary-1e-9
                    if old is not None: assert val<old+1e-9
                    old=val
                    checks+=2
    print('PASS',checks,'exact-rational and floating checks')


if __name__=='__main__': run()
