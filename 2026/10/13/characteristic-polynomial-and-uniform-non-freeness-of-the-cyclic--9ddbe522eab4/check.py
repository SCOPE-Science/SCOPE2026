#!/usr/bin/env python3
"""Finite-field and integer-identity checks for gain-four-cycle complements."""
from itertools import product

def chi(m, q):
    return ((q-1)**2 + m*(q-1)*(q-m)**2
            + 2*(q-1)*(q-m-1)**2
            + (q-1)*(q-1-m)*(q-2*m)**2)

def count(m, q):
    powers = [pow(x, m, q) for x in range(q)]
    return sum(1 for a,b,c,d in product(range(q), repeat=4)
               if powers[a] != powers[c] and powers[a] != powers[d]
               and powers[b] != powers[c] and powers[b] != powers[d])

# p = 5,11 contain mu_2; p = 7,13 contain mu_3; p = 13 contains mu_4.
for m,p in ((2,5),(2,11),(3,7),(3,13),(4,13)):
    assert (p-1)%m == 0
    brute=count(m,p)
    predicted=chi(m,p)
    assert brute == predicted, (m,p,brute,predicted)

def discr(m):
    return -3*m**6-8*m**5-32*m**4+16*m**3+224*m**2-256*m+32

def shifted_discr(n):
    return -(3*n**6+44*n**5+292*n**4+1040*n**3
             +1808*n**2+1408*n+416)
for m in range(2,300):
    assert discr(m) == shifted_discr(m-2) < 0
assert chi(3,7) == 450
assert chi(3,13) == 10980
print('GAIN_FOUR_CYCLE_CHARACTERISTIC_CHECK_OK')
