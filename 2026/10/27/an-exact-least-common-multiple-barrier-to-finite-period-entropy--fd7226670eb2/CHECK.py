#!/usr/bin/env python3
"""Small exact periodic-orbit tests; not an infinite proof."""
from itertools import product
from math import gcd
for k in (2, 3, 4):
    for m in range(1, 7):
        for n in range(1, 7):
            count = 0
            for x in product(range(k), repeat=n):
                y = [((x[(i+m)%n] - x[i]) % k) for i in range(n)]
                if all(a in (0, 1) for a in y) and all(not(y[i] and y[(i+1)%n]) for i in range(n)):
                    count += 1
            assert (count == k**n) == (m % n == 0), (k, m, n, count)
            if m <= 3:
                d = gcd(m,n)
                L = n//d
                good = 0
                for y in product((0,1), repeat=n):
                    if any(y[i]*y[(i+1)%n] for i in range(n)):
                        continue
                    if all(sum(y[(r+j*m)%n] for j in range(L)) % k == 0 for r in range(d)):
                        good += 1
                assert count == k**d * good, (k,m,n,count,good)
print('PASS: finite exact fixed-period checks and residue-sum checks')
