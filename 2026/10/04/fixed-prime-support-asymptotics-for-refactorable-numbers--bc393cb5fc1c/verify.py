#!/usr/bin/env python3
import math
from itertools import product


def valuations_on_support(z, primes):
    out=[]
    for p in primes:
        v=0
        while z % p == 0:
            z//=p
            v+=1
        out.append(v)
    return out if z == 1 else None


def structural(exponents, primes):
    rows=[]
    for a in exponents:
        row=valuations_on_support(a+1, primes)
        if row is None:
            return False
        rows.append(row)
    for j,a in enumerate(exponents):
        if sum(row[j] for row in rows) > a:
            return False
    return True


def direct(exponents, primes):
    n=1
    tau=1
    for p,a in zip(primes, exponents):
        n*=p**a
        tau*=a+1
    return n % tau == 0


def check_box(primes, bound):
    total=0
    for exponents in product(range(1,bound+1), repeat=len(primes)):
        total+=1
        if direct(exponents, primes) != structural(exponents, primes):
            raise AssertionError((primes,exponents))
    return total


def two_prime_lattice_count(T, p=2, q=3):
    L=math.exp(T)
    lp,lq=math.log(p),math.log(q)
    vals=[]
    maxr=int(T/lp)+3
    maxs=int(T/lq)+3
    for r in range(maxr+1):
        for s in range(maxs+1):
            A=(p**r)*(q**s)
            if A <= 1 + L/min(lp,lq):
                vals.append((A,r,s))
    vals.sort()
    count=0
    for A,r,s in vals:
        a=A-1
        if a < 1:
            continue
        for B,u,v in vals:
            b=B-1
            if b < 1:
                continue
            if a*lp+b*lq > L:
                break
            if r+u <= a and s+v <= b:
                count+=1
    pred=T**4/(4*lp**2*lq**2)
    return count, count/pred


def main():
    checks=[((2,),40),((2,3),20),((2,5),20),((2,3,5),7)]
    total=0
    for primes,bound in checks:
        total+=check_box(primes,bound)
    ratios=[]
    for T in (5,7,9,11,13):
        c,r=two_prime_lattice_count(T)
        ratios.append((T,c,round(r,6)))
    print('structural_cases', total)
    print('two_prime_ratios', ratios)
    print('VERIFY_OK')

if __name__=='__main__':
    main()
