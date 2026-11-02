"""Verify restricted binomial gcd valuations at the first-power boundary."""
from math import comb

def vp(n,p):
    out=0
    while n and n%p==0:
        n//=p;out+=1
    return out

def carry(x,y,p):
    c=0;t=0
    while x or y or c:
        z=x%p+y%p+c
        c=int(z>=p)
        t+=c;x//=p;y//=p
    return t

def primes(limit):
    return [n for n in range(2,limit+1) if all(n%d for d in range(2,int(n**.5)+1))]

def run():
    num=0
    for p in primes(199):
        m=p+1
        for q in range(2,p+1):
            vals=[carry(m*d,m*(q-d),p) for d in range(1,q)]
            assert vals and set(vals)==({2} if q==p else {0}),(p,q,vals)
            num+=len(vals)
        if p<=13:
            for q in range(2,p+1):
                vals=[vp(comb(m*q,m*d),p) for d in range(1,q)]
                assert set(vals)==({2} if q==p else {0})
    print('VERIFY_OK primes=',len(primes(199)),'selected coefficients=',num)

if __name__=='__main__':run()
