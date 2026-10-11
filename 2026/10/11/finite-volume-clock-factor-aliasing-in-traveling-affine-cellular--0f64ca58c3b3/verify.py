#!/usr/bin/env python3
"""Independent finite-state tests for clock factors of affine traveling CA.
Uses only the standard library. Tests do not prove infinite-parameter claims.
"""
from itertools import product
from math import gcd, lcm

checks = 0
for q in range(2, 7):
    for L in range(1, 6):
        for r in (-3, -2, -1, 1, 2, 3):
            states = tuple(product(range(q), repeat=L))
            def T(x):
                return tuple((x[(i+r) % L]+1) % q for i in range(L))
            nxt = {x:T(x) for x in states}
            order = lcm(q, L//gcd(L,r))
            assert all(x == (lambda s: s)(x) for x in states)
            y = {x:x for x in states}
            for n in range(1,order+1):
                y = {x:nxt[y[x]] for x in states}
                d = gcd(L,r*n)
                prediction = q**d if (n*L//d) % q == 0 else 0
                assert sum(v==x for x,v in y.items()) == prediction, (q,L,r,n)
                checks += 1
            # Independent cycle decomposition, compared with valuation criterion.
            visited = set()
            lengths=[]
            for s in states:
                if s not in visited:
                    t=s; period=0
                    while t not in visited:
                        visited.add(t);period+=1;t=nxt[t]
                    assert t==s
                    lengths.append(period)
            clock_factor=all(v % q==0 for v in lengths)
            def vp(x,p):
                k=0
                while x%p==0:
                    k+=1;x//=p
                return k
            a=q; primes=[];j=2
            while j*j<=a:
                if a%j==0:
                    primes.append(j)
                    while a%j==0:a//=j
                j+=1
            if a>1:primes.append(a)
            predicted=all(vp(L,p)<vp(abs(r),p)+vp(q,p) for p in primes)
            assert clock_factor==predicted,(q,L,r,clock_factor,predicted)
            checks+=1
            if gcd(L,r*q)==1:
                invL=pow(L,-1,q)
                def h(x):return (invL*sum(x))%q
                assert all((h(nxt[x])-h(x))%q==1 for x in states)
                checks+=len(states)
                # For each coordinate, find a pair differing only there,
                # with different h-values (critical support check).
                for i in range(L):
                    zero=[0]*L; changed=zero.copy();changed[i]=1
                    assert h(tuple(zero)) != h(tuple(changed))
                    checks+=1
print(f'FINITE_TESTS_OK: {checks} independent count/criterion/construction assertions')
