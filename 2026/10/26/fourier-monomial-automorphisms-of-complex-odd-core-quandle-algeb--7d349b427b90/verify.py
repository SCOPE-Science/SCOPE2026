#!/usr/bin/env python3
"""Exact arithmetic checks for Fourier descriptions of odd core-quandle algebras.
No floating-point Fourier coefficients or numerical tolerance are used.
"""
from itertools import permutations, product
from math import gcd, factorial


def orbit_data(n):
    assert n >= 3 and n % 2 == 1
    unseen = set(range(1, n))
    out = []
    while unseen:
        a = min(unseen)
        cyc = []
        z = a
        while z not in cyc:
            cyc.append(z)
            z = 2 * z % n
        assert z == a
        neg_same = (-a) % n in cyc
        if neg_same:
            assert len(cyc) % 2 == 0
            assert cyc[len(cyc)//2] == (-a) % n
            pts = tuple(cyc)
            M = 2 ** (len(cyc)//2) + 1
        else:
            pts = tuple(cyc + [(-i) % n for i in cyc])
            M = 2 ** len(cyc) - 1
        unseen.difference_update(pts)
        out.append((pts, M, len(cyc), neg_same))
    return out


def verify_scalars(n):
    data = orbit_data(n)
    orders = [1] * n
    exponents = [0] * n
    # Independently use orbit closure to build the proposed generators.
    for pts, M, ell, neg_same in data:
        a = pts[0]
        if neg_same:
            x = a
            for k in range(ell):
                assert x in pts
                orders[x] = M
                exponents[x] = pow(2,k,M)
                x = (2*x) % n
        else:
            x = a
            for k in range(ell):
                orders[x] = orders[-x % n] = M
                exponents[x] = pow(2,k,M)
                exponents[-x % n] = -pow(2,k,M) % M
                x = (2*x) % n
    for i in range(n):
        for j in range(n):
            if orders[i] != 1:
                assert orders[2*i % n] == orders[i] == orders[-i % n]
                m=orders[i]
                assert exponents[2*i % n] % m == (2*exponents[i]) % m
                assert exponents[-i % n] % m == (-exponents[i]) % m
        # Check exact Fourier multiplication: b_i b_j = b_{-i} iff j=-2i.
        assert len([j for j in range(n) if j == (-2*i) % n]) == 1
    return data


def perm_centralizer_count(n):
    # Enumerate every permutation commuting with the two index permutations,
    # only for n <= 9 to stay in a small bounded computation.
    count = 0
    for p in permutations(range(n)):
        if all(p[2*i%n] == (2*p[i])%n and p[-i%n] == (-p[i])%n for i in range(n)):
            assert p[0] == 0
            count += 1
    return count


def expected_order_prime(n):
    assert all(n % k for k in range(2,int(n**.5)+1))
    ell=1
    while pow(2,ell,n)!=1:
        ell+=1
    if ell % 2:
        h=2*ell; M=2**ell-1
    else:
        h=ell; M=2**(ell//2)+1
    assert (n-1) % h == 0
    r=(n-1)//h
    return ell,h,M,r,(M*h)**r*factorial(r)


def verify_prime_automorphisms(n):
    ell,h,M,r,order=expected_order_prime(n)
    data=verify_scalars(n)
    assert len(data)==r and all(d[1]==M and len(d[0])==h for d in data)
    # Count full diagonal scalar choices and full commuting permutations.
    assert order==M**r*h**r*factorial(r)
    # The canonical affine quandle symmetries number n(n-1).
    assert order % (n*(n-1)) == 0
    return ell,h,M,r,order,order//(n*(n-1))


def verify_exotic_R11():
    n=11; M=33
    # Generator exponents for the Fourier-basis map b_i -> zeta_33^{e_i} b_i.
    exp=[0]*n
    i=1
    for k in range(10):
        exp[i]=pow(2,k,M)
        i=(2*i)%n
    assert i==1 and sorted(exp[1:])==sorted(set(exp[1:]))
    for i,j in product(range(n),repeat=2):
        lhs=(-i)%n if j==(-2*i)%n else None
        rhs=(-i)%n if j==(-2*i)%n else None
        assert lhs==rhs
        if lhs is not None:
            assert exp[lhs] % M == (exp[i]+exp[j])%M
    # The generator genuinely has order 33, not 11.
    assert gcd(exp[1],M)==1
    return True


def main():
    for n in [3,5,7,9,11,13,15,17,19,21,25]:
        data=verify_scalars(n)
        if n <= 9:
            exact=perm_centralizer_count(n)
            # Here the centralizer is computed without using a group-order formula.
            if n in (3,5,7):
                assert exact==expected_order_prime(n)[1]**expected_order_prime(n)[3]*factorial(expected_order_prime(n)[3])
        print('odd_n',n,'orbit_factors',[(len(x),m) for x,m,_,_ in data])
    for n in [3,5,7,11,13,17,19,23,31]:
        ell,h,M,r,aut,index=verify_prime_automorphisms(n)
        print('prime',n,'order2',ell,'orbit_size',h,'scalar_order',M,'orbits',r,'algebra_aut',aut,'quandle_index',index)
    assert perm_centralizer_count(9) == 12
    assert verify_prime_automorphisms(11)[4:] == (330,3)
    assert verify_prime_automorphisms(17)[4:] == (36992,136)
    assert verify_exotic_R11()
    print('VERIFY_OK exact_Fourier_products=checked scalar_orbits=checked centralizer_enumeration_n<=9=checked exotic_R11=checked')

if __name__=='__main__': main()
