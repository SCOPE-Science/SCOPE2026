"""Standalone diagnostic checks for cube--cross-polytope Mahler asymptotics.

The global asymptotic and uniqueness statements are proved analytically in RESULT.md.
Finite numerical tests here are not substitutes for those proofs.
"""
from fractions import Fraction
from math import comb, factorial, log, exp, sqrt, lgamma


def laguerre(d, t):
    return sum((Fraction(comb(d, k), factorial(k)) * t**k
                for k in range(d + 1)), Fraction(0))


def ratio(d, t):
    den = Fraction(1)
    for j in range(1, d+1):
        den *= t + j
    return factorial(d)*laguerre(d,t)/den


def logratio(d,t):
    terms = [log(comb(d,k)) + k*log(t) - lgamma(k+1) for k in range(d+1)] if t>0 else [0.]
    m=max(terms)
    return lgamma(d+1) + m + log(sum(exp(v-m) for v in terms))-sum(log(t+j) for j in range(1,d+1))


def gamma_fun(s):
    rho=(sqrt(s*s+4*s)-s)/2
    return rho-log(1-rho)-(1+s)*log(1+s)+s*log(s)


def root():
    lo,hi=1.0,3.0
    for _ in range(120):
        mid=(lo+hi)/2
        if mid-log(1+mid+mid*mid)>0:
            hi=mid
        else:
            lo=mid
    return (lo+hi)/2


def main():
    checks=0
    expected={2:Fraction(14),3:Fraction(136,3),4:Fraction(418,3),5:Fraction(6184,15)}
    for d,v in expected.items():
        got = (2**d)*laguerre(d,Fraction(1))
        assert got == v, (d,got,v)
        checks+=1
    for d in range(2,19):
        assert ratio(d,Fraction(0))==1
        checks+=1
        for p in [Fraction(1,10), Fraction(1,2), Fraction(1), Fraction(2), Fraction(5)]:
            r=ratio(d,p)
            assert r>1,(d,p,r)
            assert abs(float(r)-exp(logratio(d,float(p))))<1.e-6*float(r)
            checks+=2
    y=root()
    s=1/(y*(1+y)); rate=gamma_fun(s)
    assert 1.79328<y<1.79329
    assert 0.19963494<s<0.19963496
    assert 0.26115245<rate<0.26115247
    for q in [s*0.01,s*0.2,s*0.5,s*0.9,s*1.1,s*2,s*10,100]:
        assert gamma_fun(q)<rate
        checks+=1
    for d in [100,300,1000,3000]:
        ar=logratio(d,d*s)/d
        assert 0<ar<rate and abs(ar-rate)<0.12,(d,ar,rate)
        checks+=1
        print(f"d={d}: log(R_d(d*s))/d={ar:.10f}")
    print(f"universal_root_y={y:.15f}, scale_s={s:.15f}, rate_gamma={rate:.15f}, growth={exp(rate):.15f}")
    print(f"VERIFY_OK {checks}")

if __name__=="__main__":
    main()
