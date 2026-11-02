"""Exact integer upper certificate for a divisor-sum comparison density.
No packages or network required; Python 3.10+.
"""
from functools import lru_cache
from fractions import Fraction
from math import factorial, isqrt

A, B, Y, T = 50001, 50000, 1000, 500
CAPS = {2:12,3:9,5:7,7:6,11:5,13:5,17:4,19:4,23:4,29:4,31:4}

def prime_list(limit):
    sieve = bytearray(b'\x01')*(limit+1)
    sieve[:2] = b'\x00\x00'
    for p in range(2,isqrt(limit)+1):
        if sieve[p]:
            sieve[p*p:limit+1:p] = b'\x00'*((limit-p*p)//p+1)
    return [p for p in range(limit+1) if sieve[p]]

@lru_cache(None)
def bp(z):
    if z>=0: return A**z,B**z
    return B**(-z),A**(-z)

def leq(n,d,z):
    x,y=bp(z)
    return n*y<=d*x

def ratio(p,e):
    if e==0:return (1,1)
    return (p**e+1, sum(p**d for d in range(1,e+1) if e%d==0))

def quant(p,e):
    if e==0:return 0
    n,d=ratio(p,e)
    # An exact bracket of size at most 65,536 steps, then binary search.
    lo,hi=-65536,65536
    assert not leq(n,d,lo) and leq(n,d,hi)
    while hi-lo>1:
        z=(lo+hi)//2
        if leq(n,d,z): hi=z
        else:lo=z
    assert leq(n,d,hi) and not leq(n,d,hi-1)
    return hi

def main():
    primes=prime_list(Y)
    assert len(primes)==168
    arr=[1]; offset=0; denom=1
    for p in primes:
        if p in CAPS:
            cap=CAPS[p]
            terms=[(quant(p,e),(p-1)*p**(cap-e)) for e in range(cap+1)]
            local_d=p**(cap+1)
            assert sum(w for _,w in terms)==local_d-1
        else:
            terms=[(0,p-1),(quant(p,1),1)]
            local_d=p
            assert sum(w for _,w in terms)==local_d
        lower=min(k for k,w in terms)
        upper=max(k for k,w in terms)
        nxt=[0]*(len(arr)+upper-lower)
        for i,v in enumerate(arr):
            if v:
                for exponent,weight in terms:
                    nxt[i+exponent-lower]+=v*weight
        arr=nxt
        offset+=lower
        denom*=local_d
    cutoff=-T-offset
    assert 0<cutoff<len(arr)
    numerator=sum(arr[cutoff:])
    assert numerator*1_000_000<denom*784_271
    missing=sum((Fraction(1,p**(CAPS[p]+1)) for p in CAPS), Fraction(0))
    assert missing<Fraction(145,1_000_000)
    # For x in [0,1], e^x-1 <= (e-1)x. Exact rational
    # checks below certify e^(e-1)<6 and exp(500000/50001)>20000.
    assert sum(Fraction(1,factorial(k)) for k in range(9))<Fraction(11,4)
    # remainder bound for exp(1) after degree 8: < 1/(8!*8)
    assert sum(Fraction(1,factorial(k)) for k in range(9))+Fraction(1,8*factorial(8))<Fraction(11,4)
    x=Fraction(7,4)
    exp_upper=sum((x**k/factorial(k) for k in range(9)),Fraction(0))
    tail_next=x**9/factorial(9)
    # Successive tail terms are at most x/10 of their predecessor.
    exp_upper+=tail_next/(1-x/10)
    assert exp_upper<6
    z=Fraction(999,100)
    assert Fraction(500000,50001)>z
    assert sum((z**k/factorial(k) for k in range(30)),Fraction(0))>20000
    # Tail bound: 6*exp(-500000*log(50001/50000)) < 6/20000.
    assert Fraction(784271+145+300,1_000_000)==Fraction(784716,1_000_000)
    assert Fraction(784716,1_000_000)<Fraction(785,1000)
    print('VERIFY_OK prime_count=',len(primes),'states=',len(arr),'cutoff=',cutoff,'offset=',offset)
    print('finite_probability_bounds: P<784271/1000000, omit<145/1000000, tail<300/1000000')
    print('density_upper_strict: 0.784716; all comparisons exact rational/integer')
    print('finite_p=',float(Fraction(numerator,denom)),'omit=',float(missing))

if __name__=='__main__':main()
