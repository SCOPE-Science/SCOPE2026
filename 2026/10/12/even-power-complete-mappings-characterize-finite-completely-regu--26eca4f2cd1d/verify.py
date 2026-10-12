#!/usr/bin/env python3
"""Exact finite-table tests for the even-power complete-mapping theorem.

Independent enumeration validates small cases. It is not the proof for arbitrary order.
"""
from itertools import product, permutations
from math import gcd, factorial


def mul(t, n, a, b):
    return t[a*n+b]


def associative(t,n):
    return all(mul(t,n,mul(t,n,a,b),c)==mul(t,n,a,mul(t,n,b,c))
               for a,b,c in product(range(n),repeat=3))


def power(t,n,a,k):
    assert k>=1
    x=a
    for _ in range(k-1): x=mul(t,n,x,a)
    return x


def L_ideal(t,n,a):
    return frozenset([a]+[mul(t,n,x,a) for x in range(n)])


def completely_regular(t,n):
    return all(L_ideal(t,n,a)==L_ideal(t,n,power(t,n,a,2)) for a in range(n))


def kcomplete(t,n,perm,k):
    return len({mul(t,n,x,power(t,n,perm[x],k)) for x in range(n)})==n


def exists(t,n,k):
    return any(kcomplete(t,n,perm,k) for perm in permutations(range(n)))


def exponent_choice(k,m):
    assert k%2==0 and k>=2
    return next(a for a in range(1,m+1)
                if gcd(a,m)==gcd(1+k*a,m)==1)


def brandt(n, complete):
    # Combinatorial Brandt semigroup: n^2 matrix units plus zero.
    # The diagonal sandwich pattern gives matrix-unit multiplication;
    # the full pattern gives a rectangular band plus zero.
    size=n*n+1;zero=size-1
    def x(i,j):return i*n+j
    t=[zero]*(size*size)
    for i,j,h,l in product(range(n),repeat=4):
        if complete or j==h:
            t[x(i,j)*size+x(h,l)]=x(i,l)
    assert associative(t,size)
    return tuple(t),size


def main():
    total=cr_total=odd_cases=0
    for n in (1,2,3):
        local=0
        for t in product(range(n),repeat=n*n):
            if not associative(t,n): continue
            cr=completely_regular(t,n)
            for k in (2,4,6):
                assert exists(t,n,k)==cr, (n,t,k,cr)
                if cr:
                    e=exponent_choice(k,factorial(n))
                    perm=tuple(power(t,n,x,e) for x in range(n))
                    assert sorted(perm)==list(range(n))
                    assert kcomplete(t,n,perm,k)
            assert not exists(t,n,3) or cr
            odd_cases+=exists(t,n,3)
            total+=1;local+=1;cr_total+=cr
        print('ORDER',n,'ASSOCIATIVE_TABLES',local)
    for n in (2,3):
        t,size=brandt(n,False)
        assert exists(t,size,1) if n==2 else True
        assert not exists(t,size,2) if n==2 else not completely_regular(t,size)
        t,size=brandt(n,True)
        assert completely_regular(t,size)
        for k in (2,4,6):
            e=exponent_choice(k,factorial(size))
            perm=tuple(power(t,size,x,e) for x in range(size))
            assert sorted(perm)==list(range(size))
            assert kcomplete(t,size,perm,k)
    # Small odd-power obstruction: C2 is completely regular but not 3-complete.
    cyclic2=(0,1,1,0)
    assert completely_regular(cyclic2,2)
    assert not exists(cyclic2,2,3)
    # Arithmetic CRT witness existence, including exponents divisible by 3,5,7.
    arithmetic=0
    for m in range(1,151):
        for k in (2,4,6,8,10,12):
            e=exponent_choice(k,m)
            assert gcd(e,m)==gcd(1+k*e,m)==1
            arithmetic+=1
    print('ASSOCIATIVE_TOTAL',total,'COMPLETELY_REGULAR',cr_total,
          'ODD_THREE_COMPLETE',odd_cases,'CRT_CASES',arithmetic,'VERIFY_OK')

if __name__=='__main__': main()
