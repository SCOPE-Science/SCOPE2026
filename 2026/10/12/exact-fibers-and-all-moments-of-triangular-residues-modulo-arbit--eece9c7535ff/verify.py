#!/usr/bin/env python3
"""Exact small-modulus checks for triangular residue fibers."""
from math import prod
from collections import Counter

def odd_factors(n):
    a=0
    while n%2==0:
        a+=1;n//=2
    out=[]
    p=3
    while p*p<=n:
        if n%p==0:
            e=0
            while n%p==0:
                n//=p;e+=1
            out.append((p,e))
        p+=2
    if n>1:out.append((n,1))
    return a,out

def roots_odd_power(p,a,D):
    q=p**a
    D%=q
    if D==0:return p**(a//2)
    v=0;z=D
    while z%p==0:
        z//=p;v+=1
    if v%2:return 0
    if pow(z%p,(p-1)//2,p)!=1:return 0
    return 2*p**(v//2)

def pred_fiber(m,t):
    _,fac=odd_factors(m)
    return 2*prod(roots_odd_power(p,a,8*t+1) for p,a in fac)

def count_square_values(p,a):
    return 1+(p-1)*sum(p**(a-2*j-1) for j in range((a-1)//2+1))//2

def main():
    pairs=0
    for m in range(1,1001):
        c=Counter((n*(n+1)//2)%m for n in range(2*m))
        factors=odd_factors(m)[1]
        assert all(c.get(t,0)==pred_fiber(m,t) for t in range(m)),('fibers',m)
        E=sum(k*k for k in c.values())
        numerator=4*m
        for p,a in factors:
            numerator=numerator*(p+a*(p-1))//p # unsafe iterative division? factor numerator initially 4m divisible by each p^a yes, later factors multiply etc
        assert E==numerator,('energy',m,E,numerator)
        count= sum(v>0 for v in (c.get(t,0) for t in range(m)))
        target=(2**odd_factors(m)[0])*prod(count_square_values(p,a) for p,a in factors)
        assert count==target,('occupancy',m)
        assert sum(c.values())==2*m
        pairs+=len(c)
    for m in range(1,300):
        c=Counter((n*(n+1)//2)%m for n in range(2*m))
        alpha,fac=odd_factors(m)
        for k in range(1,7):
            direct=sum(v**k for v in c.values())
            moment=2**(k+alpha)
            for p,a in fac:
                local=p**(k*(a//2))+2**(k-1)*(p-1)*p**(a-1)*sum(p**((k-2)*j) for j in range((a-1)//2+1))
                moment*=local
            assert direct==moment,(m,k,direct,moment)
    for p in [3,5,7,11,13,17,19,31]:
        for a in range(1,8):
            R=count_square_values(p,a)
            conjecture_numer= (1+sum((-1)**(j+1)*p**j for j in range(1,a+1)) if a%2 else 2+sum((-1)**j*p**j for j in range(1,a+1)))
            assert 2*R==conjecture_numer,(p,a,R,conjecture_numer)
    print('VERIFY_OK')
    print('all_moduli=1..1000')
    print('complete_residue_fiber_formulas=PASS')
    print('complete_collision_second_moments=PASS')
    print('complete_saturation_counts=PASS')
    print('moment_orders=1..6_moduli=1..299_PASS')
    print('Ulness_Conjecture_1_local_formula_prime_checks=8_primes_x_7_exponents')

if __name__=='__main__':main()
