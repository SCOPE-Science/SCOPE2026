"""Exact independent cyclotomic checks of the order-24 Jacobi-sum dichotomy.

Represent F_{p^2} as F_p[u]/(u^2-d), where d is a nonsquare.
No floating-point operations are used.
"""
from itertools import chain

PRIMES=(5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79)
PRIMITIVE_EXPONENTS=(1,5,7,11,13,17,19,23)

def prime_factors(n):
    out=[]
    r=2
    while r*r<=n:
        if n%r==0:
            out.append(r)
            while n%r==0:n//=r
        r+=1
    if n>1:out.append(n)
    return out

def reduce_zeta24(power):
    # Cyclotomic polynomial Phi_24(X) = X^8 - X^4 + 1.
    table=[[int(i==j) for i in range(8)] for j in range(8)]
    for j in range(8,24):
        table.append([table[j-4][k]-table[j-8][k] for k in range(8)])
    return table[power%24]

RED=[reduce_zeta24(k) for k in range(24)]

def check_prime(p):
    d=next(x for x in range(2,p) if pow(x,(p-1)//2,p)==p-1)
    def mul(x,y):
        a,b=x;c,e=y
        return ((a*c+d*b*e)%p,(a*e+b*c)%p)
    def power(x,n):
        out=(1,0)
        while n:
            if n&1:out=mul(out,x)
            x=mul(x,x)
            n//=2
        return out
    q=p*p
    factor=prime_factors(q-1)
    g=next((a,b) for a in range(p) for b in range(p)
           if (a,b)!=(0,0) and all(power((a,b),(q-1)//ell)!=(1,0) for ell in factor))
    log={}
    x=(1,0)
    for j in range(q-1):
        assert x not in log
        log[x]=j
        x=mul(x,g)
    assert len(log)==q-1 and x==(1,0)
    sums={t:[0]*8 for t in PRIMITIVE_EXPONENTS}
    for x,j in log.items():
        if x==(1,0):continue
        y=((1-x[0])%p,(-x[1])%p)
        eta=1 if log[y]%2==0 else -1
        for t in PRIMITIVE_EXPONENTS:
            v=RED[t*j%24]
            for k in range(8):sums[t][k]+=eta*v[k]
    predicted=p%24 in (13,17,19,23)
    for t,coeffs in sums.items():
        equals=all(v==0 for v in coeffs[1:]) and abs(coeffs[0])==p
        assert equals==predicted,(p,t,coeffs,predicted)
        if predicted:assert coeffs[0] in (p,-p)
    return (p,p%24, predicted, sums[1][0] if predicted else 'nonpure')

if __name__=='__main__':
    checks=[check_prime(p) for p in PRIMES]
    for entry in checks:print(*entry)
    for residue in (1,5,7,11,13,17,19,23):
        predicted=residue in (13,17,19,23)
        for t in PRIMITIVE_EXPONENTS:
            f=lambda r,x:x+(r*x)%24
            assert (f(residue,t)==f(residue,(t+12)%24))==predicted
    print('CHECK_PASS: exact Jacobi sums and digit-sum congruence for every listed field')
