"""Exact finite corroboration for a short-prime-gap weird-number criterion."""
from math import isqrt

def primes_upto(n):
    sieve=bytearray(b'\x01')*(n+1)
    sieve[:2]=b'\x00\x00'
    for p in range(2,isqrt(n)+1):
        if sieve[p]:
            sieve[p*p:n+1:p]=b'\x00'*(((n-p*p)//p)+1)
    return [i for i,v in enumerate(sieve) if v]

def old_criterion(M,p,q,a):
    # Exact complement-to-semiperfectness calculation; coefficients for 2^k.
    if a<=0: return False
    for t in range(a//q+1):
        b=a-t*q
        if b%p<=M and b//p<=M:
            return False
    return True

def new_criterion(M,p,q,a):
    x=p-M
    return (a>M and a<q and 1<=x*(q+1)%p<=x-1)

def main():
    pairs=0; matches=0; witnesses=[]
    for k in range(1,10):
        M=2**(k+1)-1
        # a>M => q<M*p/x, hence all possible q are finite.
        for x in range(2, isqrt(M)+2,2):
            if (x-1)**2>M: continue
            p=M+x
            if p not in set(primes_upto(p)): continue
            upper=(M*p-1)//x
            ps=primes_upto(upper)
            for q in ps:
                if q<=p: continue
                a=M*(p+1)-x*q
                if a<=0:continue
                old=old_criterion(M,p,q,a)
                new=new_criterion(M,p,q,a)
                assert old==new,(k,M,p,q,a,old,new)
                pairs+=1
                if old:
                    matches+=1
                    witnesses.append((k,p,q,a))
    assert (3,19,61,56) in witnesses
    print('VERIFY_OK', 'tested_prime_pairs',pairs,'weird_witnesses',matches,'examples',witnesses[:5])

if __name__=='__main__':main()
