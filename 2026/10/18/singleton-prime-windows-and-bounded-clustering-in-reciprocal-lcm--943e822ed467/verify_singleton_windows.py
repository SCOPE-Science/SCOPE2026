"""Reproducible numerical checks for normalized reciprocal-LCM singleton windows.
Pure standard-library high-precision arithmetic; not a proof of the asymptotic theorem.
"""
from decimal import Decimal, getcontext
from fractions import Fraction
from math import isqrt
getcontext().prec=85
D=Decimal

def dec(a):
    return D(a.numerator)/D(a.denominator) if isinstance(a,Fraction) else D(a)

def qlog(p,a,k):
    if a==0: return D(0)
    x=Fraction(1,p)
    s=sum((x**j for j in range(a)),Fraction())
    t=s+x**a
    v=(t**k-s**k)/(k*x**a)
    return dec(v).ln()/D(k-1)

def threshold(p,k):
    logp=D(p).ln()
    v1=qlog(p,1,k);v2=qlog(p,2,k)
    return (v2-v1)/logp,v1/logp

def isprime(n):
    return n>=2 and all(n%d for d in range(2,isqrt(n)+1))

def check_case(p,k):
    s,t=threshold(p,k)
    if not s<t: return False
    eps=(s+t)/2
    scores=[qlog(p,a,k)-D(a)*eps*D(p).ln() for a in range(0,14)]
    winner=max(range(14),key=lambda a:scores[a])
    # For a>=14, the bounded local factor is insufficient to beat a=1.
    tail=D(p)/(D(p)-1)
    tail_score=tail.ln()-D(14)*eps*D(p).ln()
    assert max(scores)>tail_score
    assert winner==1, (p,k,winner)
    width=(t-s)*D(p)**2*D(p).ln()
    return width

if __name__=='__main__':
    trials=0
    for k in (6,10,16,20,100):
        print('k=',k,'asymptotic_scaled_width=',D(k-5)/12)
        for p in (101,1009,10007):
            assert isprime(p)
            w=check_case(p,k)
            if w is False: print('p=',p,'no-window');continue
            print('p=',p,'scaled_width=',str(w)[:28])
            trials+=1
    for k in (2,3,4,5):
        n=0
        for p in range(2,2000):
            if not isprime(p):continue
            s,t=threshold(p,k)
            assert s>=t, (p,k,s,t)
            n+=1
        print('k=',k,'finite-absence-check-prime-count=',n)
    print('positive_window_trials=',trials)
