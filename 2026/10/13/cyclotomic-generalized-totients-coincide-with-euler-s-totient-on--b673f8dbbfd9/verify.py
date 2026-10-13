from math import gcd
from sympy import cyclotomic_poly, symbols, totient
x=symbols('x')
ms=[3,4,5,7,8,9,11,16,25,27]
limit=400
checked=0
for m in ms:
    # identify underlying prime
    mm=m
    ell=None
    for p in range(2,m+1):
        if all(p%d for d in range(2,int(p**0.5)+1)):
            t=m
            while t%p==0:t//=p
            if t==1:
                ell=p;break
    assert ell is not None
    P=cyclotomic_poly(m,x,polys=True)
    degphi=int(totient(m))
    def rho(p):
        if p==ell: return 1
        return degphi if (p-1)%m==0 else 0
    for n in range(2,limit+1):
        direct=sum(1 for a in range(n) if gcd(int(P.eval(a)),n)==1)
        # exact formula by distinct prime divisors
        t=n; primes=[]; d=2
        while d*d<=t:
            if t%d==0:
                primes.append(d)
                while t%d==0:t//=d
            d+=1
        if t>1: primes.append(t)
        num=n
        den=1
        # compute integer via fractions
        from fractions import Fraction
        f=Fraction(n,1)
        for p in primes: f*=Fraction(p-rho(p),p)
        formula=f.numerator//f.denominator
        assert formula==direct,(m,n,direct,formula,primes)
        eq=(direct==int(totient(n)))
        expected=(set(primes)=={ell})
        assert eq==expected,(m,n,direct,int(totient(n)),primes,ell)
        checked+=1
print(f'VERIFY_OK m_cases={len(ms)} n_limit={limit} checked={checked}')
