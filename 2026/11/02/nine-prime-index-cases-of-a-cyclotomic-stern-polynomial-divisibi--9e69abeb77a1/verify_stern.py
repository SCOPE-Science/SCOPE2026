"""Exact certificates for cyclotomic-factor restrictions of Stern (0,1)-polynomials.

All arithmetic is integer or polynomial arithmetic over F_2; no external packages.
Run: python3 verify_stern.py
"""
from math import isqrt

FACTORS = {
 3: {5:1}, 5: {17:1}, 11: {5:2, 41:1},
 13: {17:1, 241:1}, 19: {5:1, 13:1, 37:1, 109:1},
 29: {17:1, 15790321:1}, 37: {17:1, 241:1, 433:1, 38737:1},
 53: {17:1, 858001:1, 308761441:1},
 59: {5:1, 107367629:1, 536903681:1},
}

def is_prime(n):
    if n < 2: return False
    if n % 2 == 0: return n == 2
    d = 3
    while d <= isqrt(n):
        if n % d == 0: return False
        d += 2
    return True

def prime_factors(n):
    out = []
    for p in range(2,isqrt(n)+1):
        if n % p == 0:
            out.append(p)
            while n % p == 0: n //= p
    if n != 1: out.append(n)
    return out

def gf_mul(a,b,poly,degree):
    result=0
    high=1<<degree
    while b:
        if b&1: result ^= a
        b>>=1
        a<<=1
        if a&high: a ^= poly
    return result

def eval_stern_mod_two(n,zeta,poly,degree):
    # Binary doubling evaluates the polynomial modulo (2,Phi_p).
    # Returns the ordered pair (a(n,zeta),a(n+1,zeta)).
    if n==0: return (0,1)
    a,b=eval_stern_mod_two(n//2,zeta,poly,degree)
    a2=gf_mul(a,a,poly,degree)
    b2=gf_mul(b,b,poly,degree)
    mid=gf_mul(zeta,a2,poly,degree)^b2
    return (a2,mid) if n%2==0 else (mid,b2)

def run():
    assert len(FACTORS)==9
    total_nonzero=0
    for p,factors in FACTORS.items():
        assert is_prime(p)
        # Direct exhaustive proof 2 is a primitive root modulo p.
        assert pow(2,p-1,p)==1
        assert all(pow(2,(p-1)//r,p)!=1 for r in prime_factors(p-1))
        d=p-1
        modulus=(1<<p)-1  # Phi_p(X) = sum_{j=0}^{p-1} X^j
        m=(1<<d)+1
        assert all(is_prime(r) for r in factors)
        prod=1
        for r,e in factors.items(): prod*=r**e
        assert prod==m,(p,m,prod)
        assert eval_stern_mod_two(m,2,modulus,d)[0]==0,(p,'notzero')
        residues=[]
        for r in factors:
            val=eval_stern_mod_two(m//r,2,modulus,d)[0]
            assert val !=0, (p,r,'zero')
            assert val.bit_length()<=d
            residues.append((r,format(val,'x')))
            total_nonzero+=1
        print('CERT',p,'m=',m,'factors=',factors,'residues=',residues)
    print('VERIFY_OK primes=',len(FACTORS),'nonzero_certificates=',total_nonzero)
if __name__=='__main__': run()
