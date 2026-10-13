#!/usr/bin/env python3
"""Finite reproducibility checks for the power-complement cycle classification."""
from math import comb, gcd

def edges(n, k):
    return {(i, j) for i in range(n) for j in range(i+1,n) if min(j-i,n-(j-i))<=k}

def triangle_count(n,e):
    return sum((a,b) in e and (a,c) in e and (b,c) in e for a in range(n) for b in range(a+1,n) for c in range(b+1,n))

checks=0; matchcases=0; unequal_triangle=0; candidates=0
for p in range(2,8):
    for k in range(1,9):
        n=2*(p+1)*k+1
        base=edges(n,k)
        powered=edges(n,p*k)
        comp={(i,j) for i in range(n) for j in range(i+1,n) if (i,j) not in base}
        th=triangle_count(n,powered)
        tc=triangle_count(n,comp)
        formula_h=n*comb(p*k,2) + n*comb((p-2)*k+1,2)//3 if n*comb((p-2)*k+1,2)%3 == 0 else None
        assert formula_h == th, (n,k,p,th,formula_h)
        formula_c=n*comb((2*p-1)*k,2)//3
        assert n*comb((2*p-1)*k,2)%3==0 and formula_c==tc
        assert th-tc==n*k*(k-1)//2,(n,k,p,th,tc)
        if k==1:
            assert gcd(p+1,n)==1
            phi=lambda a:(p+1)*a%n
            mapped={tuple(sorted((phi(i),phi(j)))) for i,j in comp}
            assert mapped==powered,(n,p)
            matchcases+=1
        else: assert th>tc;unequal_triangle+=1
        checks+=1

# Independently check every order up to 40, including dense/completed powers;
# degree isomorphism obstruction except the true cycle family.
degchecks=0; survivor=[]
for n in range(3,41):
    for k in range(1,21):
        for p in range(2,7):
            a=edges(n,k)
            b=edges(n,p*k)
            c={(i,j) for i in range(n) for j in range(i+1,n) if (i,j) not in a}
            if len(b)==len(c):
                survivor.append((n,k,p))
                # triangle test rejects everything except (n,1,p) n=2p+3
                assert triangle_count(n,b)==triangle_count(n,c) if k==1 and n==2*p+3 else triangle_count(n,b)!=triangle_count(n,c), (n,k,p)
            degchecks+=1
assert set(survivor)=={(2*p+3,1,p) for p in range(2,7)}|{(n,k,p) for n,k,p in survivor if k>1}
print('ALL CHECKS PASSED')
print(f'triangle_parameter_profiles={checks}; obstruction_profiles={unequal_triangle}; explicit_isomorphism_profiles={matchcases}')
print(f'finite_parameter_triples_n3to40={degchecks}; degree_surviving_triples={len(survivor)}')
print('degree_survivors=' + str(survivor))
