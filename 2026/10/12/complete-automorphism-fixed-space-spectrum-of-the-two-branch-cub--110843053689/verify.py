#!/usr/bin/env python3
"""Exhaustive finite-field checks for the two-branch cubic monomial algebra."""
from collections import Counter
from itertools import product

def rank_mod(matrix, p):
    m = [row[:] for row in matrix]
    r = 0
    for col in range(len(m[0])):
        pivot = next((i for i in range(r,len(m)) if m[i][col] % p), None)
        if pivot is None:
            continue
        m[r],m[pivot] = m[pivot],m[r]
        z = pow(m[r][col],-1,p)
        m[r] = [v*z % p for v in m[r]]
        for i in range(len(m)):
            if i != r:
                h = m[i][col]
                m[i] = [(u-h*v) % p for u,v in zip(m[i],m[r])]
        r += 1
        if r == len(m):
            break
    return r

def automorphisms(p):
    for swap in range(2):
        for a,d in product(range(1,p),repeat=2):
            for b,c,e,f in product(range(p),repeat=4):
                if not swap:
                    m=[[a,0,0,0],[0,d,0,0],[b,f,a*a,0],[c,e,0,d*d]]
                else:
                    m=[[0,d,0,0],[a,0,0,0],[b,f,0,d*d],[c,e,a*a,0]]
                yield [[x%p for x in row] for row in m]

def expected(q):
    if q%2:
        return (2*q**4*(q-3)*(q-2),q**3*(2*q-1)*(3*q-7),q*(7*q**3-8*q**2-3*q+1),q**3+3*q*q-q-1,1)
    return (q**4*(q-2)*(2*q-3),q**3*(q-1)*(3*q-5),q*(4*q**3-6*q*q-q+1),(q-1)*(q+1)**2,1)

def test(p):
    group = list(automorphisms(p))
    assert len(group) == 2*(p-1)**2*p**4
    cnt=Counter()
    for g in group:
        cnt[5-rank_mod([[(g[i][j]-(i==j))%p for j in range(4)] for i in range(4)],p)] += 1
    got=tuple(cnt.get(i,0) for i in range(1,6))
    assert got == expected(p),(p,got,expected(p))
    burnside = sum(got[i-1]*p**i for i in range(1,6))//len(group)
    assert burnside == (8*p if p%2 else 5*p)
    print('SPECTRUM',p,got,'ORBITS',burnside)
    if p <= 3:
        all_v=product(range(p),repeat=4)
        seen=set(); orbits=0
        for v in all_v:
            if v in seen:continue
            orbits+=1
            seen.update(tuple(sum(g[i][j]*v[j] for j in range(4))%p for i in range(4)) for g in group)
        assert orbits == (8 if p%2 else 5), (p,orbits)
        print('DIRECT_RADICAL_ORBITS',p,orbits)
for prime in (2,3,5):test(prime)
print('VERIFY_OK')
