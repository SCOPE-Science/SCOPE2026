#!/usr/bin/env python3
"""Exact finite certificates for odd-exponent pristine-number obstructions.

Mathematical reduction and complete boundary proof are in RESULT.md.
All arithmetic uses Python's arbitrary-precision integers; no external packages.
"""
import math
from fractions import Fraction

D_VALUES = tuple(range(9, 26, 2))


def P(d, c):
    """Fink's binomial polynomial, evaluated exactly for c>=0."""
    accum = 0
    choose = 1
    for i in range(d+1):
        if i:
            choose = choose*(c+i)//i
        accum += math.comb(d,i)*choose
    return accum


def prime_factors(n):
    """Small prime divisors by exact trial division; n used only for d!."""
    out=[]
    p=2
    while p*p<=n:
        if n%p==0:
            a=0
            while n%p==0:
                n//=p;a+=1
            out.append((p,a))
        p=3 if p==2 else p+2
    if n>1:out.append((n,1))
    return out


def factorial_divisors(d):
    fac=math.factorial(d)
    divs=[1]
    for p,a in prime_factors(fac):
        seed=divs[:]
        power=1
        for _ in range(a):
            power*=p
            divs += [v*power for v in seed]
    assert len(set(divs))==len(divs)
    assert all(fac%x==0 for x in divs)
    return divs


def nth_root_exact(n, exponent):
    assert n>=1 and exponent>=1
    x=1<<((n.bit_length()+exponent-1)//exponent)
    while True:
        y=((exponent-1)*x+n//pow(x,exponent-1))//exponent
        if y>=x:break
        x=y
    while pow(x,exponent)>n:x-=1
    while pow(x+1,exponent)<=n:x+=1
    return x,pow(x,exponent)==n


def polynomial_K_by_integer_division(d):
    """Construct d! P_d(X) in Z[X], divide by X+d+1, evaluate quotient."""
    F=math.factorial(d)
    full=[0]*(d+1)
    rising=[1]  # coefficients of product_{j=1}^i (X+j), ascending
    for i in range(d+1):
        scale=math.comb(d,i)*(F//math.factorial(i))
        for j,coeff in enumerate(rising):
            full[j]+=scale*coeff
        nxt=[0]*(len(rising)+1)
        for j,coeff in enumerate(rising):
            nxt[j]+=(i+1)*coeff
            nxt[j+1]+=coeff
        rising=nxt
    shift=d+1
    quotient=[0]*d
    quotient[-1]=full[-1]
    for j in range(d-1,0,-1):
        quotient[j-1]=full[j]-shift*quotient[j]
    assert full[0]==shift*quotient[0]
    assert all(sum(quotient[j]*c**j for j in range(d))* (c+shift)==F*P(d,c)
               for c in (1,2,5))
    K=0
    for coeff in reversed(quotient):K=K*(-shift)+coeff
    return K


def K_polynomial(d):
    """Exact Q_d(-d-1) = d! P_d'(-d-1), from coefficient identity."""
    assert d%2==1
    ans=sum(((-1)**j*Fraction(math.comb(d,j), d-2*j)
             for j in range((d-1)//2+1)),Fraction(0))
    ans*=math.factorial(d)
    assert ans.denominator==1
    return ans.numerator


def prime_divisors_of_K(K,d):
    rem=abs(K)
    result=[]
    for p in range(2,d+1):
        if p>2 and p%2==0:continue
        if not all(p%i for i in range(2,math.isqrt(p)+1)):continue
        if rem%p==0:
            result.append(p)
            while rem%p==0:rem//=p
    assert rem==1, 'K has an unaccounted prime factor'
    return result


def binary_check_exception(d,p):
    """Locate any exact root P_d(c)=p^d for c>=1 using monotonicity."""
    target=p**d
    if P(d,1)>target:return None
    lo=1;hi=1
    while P(d,hi)<target:hi*=2
    while lo<=hi:
        mid=(lo+hi)//2
        observed=P(d,mid)
        if observed==target:return mid
        if observed<target:lo=mid+1
        else:hi=mid-1
    return None


def main():
    total_checks=0
    for d in D_VALUES:
        F=math.factorial(d)
        K=K_polynomial(d)
        assert K==polynomial_K_by_integer_division(d)
        assert K!=0
        exceptions=prime_divisors_of_K(K,d)
        # Confirm the vanishing defining the factor, via finite integer
        # algebra; structural parity proof is independent of this check.
        assert sum(math.comb(d,i)*math.prod(range(-d,i-d))//math.factorial(i)
                   for i in range(d+1))==0
        divisors=factorial_divisors(d)
        candidates=[m-d-1 for m in divisors if m>=d+2]
        odd_power_hits=[]
        for c in candidates:
            v=P(d,c)
            root,exact=nth_root_exact(v,d)
            if exact and root%2==1:
                odd_power_hits.append((c,root))
        exception_hits=[]
        for p in exceptions:
            if p!=2:
                c=binary_check_exception(d,p)
                if c is not None:exception_hits.append((c,p))
        assert not odd_power_hits, (d,odd_power_hits)
        assert not exception_hits, (d,exception_hits)
        total_checks+=len(candidates)
        print('D={:02d} factorial_divisors={} candidate_c={} exceptional_odd_primes={} K={} verified=NONE'.format(
              d,len(divisors),len(candidates),','.join(map(str,(p for p in exceptions if p%2))) or '-',K),flush=True)
    print('VERIFY_OK exponent_set=9,11,13,15,17,19,21,23,25 candidate_checks={} exact_integer_arithmetic=PASS'.format(total_checks),flush=True)

if __name__=='__main__':main()
