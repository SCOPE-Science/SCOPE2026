from fractions import Fraction
from itertools import product
from math import comb, factorial, exp, sqrt, lgamma, log1p, log

def pr(m,n,r):
    return Fraction(comb(n,r)*(m-1)**(n-r), m**n)

def prr(m,n,r):
    if 2*r>n:
        return Fraction(0)
    return Fraction(factorial(n)*(m-2)**(n-2*r), factorial(r)**2*factorial(n-2*r)*m**n)

def delta(m,n,r):
    return n*(n-1)-2*m*r*(n-1)+m*m*r*(r-1)

def cov_formula(m,n,r):
    EK=m*pr(m,n,r)
    return EK*Fraction(delta(m,n,r),n*(m-1))

def var_kr(m,n,r):
    p=pr(m,n,r); pp=prr(m,n,r)
    return m*p*(1-p)+m*(m-1)*(pp-p*p)

def var_q(m,n):
    return Fraction(2*(m-1)*(n-1),n)

def brute(m,n):
    rows=[]
    for xs in product(range(m), repeat=n):
        occ=[0]*m
        for x in xs:
            occ[x]+=1
        C=sum(v*(v-1)//2 for v in occ)
        Q=Fraction(m,n)*sum(v*v for v in occ)-n
        K=[sum(v==r for v in occ) for r in range(n+1)]
        rows.append((K,C,Q))
    N=m**n
    EQ=sum((q for _,_,q in rows),Fraction(0))/N
    EQ2=sum((q*q for _,_,q in rows),Fraction(0))/N
    assert EQ==m-1
    assert EQ2-EQ*EQ==var_q(m,n)
    checks=1
    for r in range(n+1):
        EK=sum((Fraction(k[r]) for k,_,_ in rows),Fraction(0))/N
        EKQ=sum((Fraction(k[r])*q for k,_,q in rows),Fraction(0))/N
        EK2=sum((Fraction(k[r]*k[r]) for k,_,_ in rows),Fraction(0))/N
        assert EK==m*pr(m,n,r)
        assert EKQ-EK*EQ==cov_formula(m,n,r)
        assert EK2-EK*EK==var_kr(m,n,r)
        checks+=3
    return len(rows),checks

def float_probs(m,n,r):
    lp=(lgamma(n+1)-lgamma(r+1)-lgamma(n-r+1) + (n-r)*log1p(-1/m)-r*log(m))
    p=exp(lp)
    if 2*r>n:
        pp=0.0
    else:
        lpp=(lgamma(n+1)-2*lgamma(r+1)-lgamma(n-2*r+1)+(n-2*r)*log1p(-2/m)-2*r*log(m))
        pp=exp(lpp)
    return p,pp

def run():
    allocations=0; brute_checks=0
    for m in range(2,6):
        for n in range(2,8):
            a,c=brute(m,n)
            allocations+=a; brute_checks+=c

    identity_checks=0
    for m in range(2,51):
        for n in range(2,101):
            cs=[cov_formula(m,n,r) for r in range(n+1)]
            assert sum(cs,Fraction(0))==0
            assert sum((r*cs[r] for r in range(n+1)),Fraction(0))==0
            assert var_q(m,n)==Fraction(2*(m-1)*(n-1),n)
            identity_checks+=3
            if n==2*m:
                assert cov_formula(m,n,1)==0
                identity_checks+=1

    limit_checks=0
    for lam in [0.5,1.0,2.0,3.0,5.0]:
        m=20000; n=round(lam*m)
        for r in range(0,5):
            p,pp=float_probs(m,n,r)
            vk=(m*p*(1-p)+m*(m-1)*(pp-p*p))/m
            pi=exp(-lam)*lam**r/factorial(r)
            vt=pi*(1-pi)-pi*pi*(r-lam)**2/lam
            assert abs(vk-vt)<5e-5
            scaled=(m*p*delta(m,n,r)/(n*(m-1)))/m
            target=pi*((lam-r)**2-r)/lam
            assert abs(scaled-target)<5e-4
            limit_checks+=2

    print('VERIFY_OK')
    print(f'allocations_enumerated={allocations}')
    print(f'brute_exact_checks={brute_checks}')
    print(f'closed_identity_checks={identity_checks}')
    print(f'fixed_load_limit_checks={limit_checks}')

if __name__=='__main__':
    run()
