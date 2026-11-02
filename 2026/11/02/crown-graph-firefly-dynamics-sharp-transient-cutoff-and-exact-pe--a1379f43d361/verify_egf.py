#!/usr/bin/env python3
"""Exact polynomial-ring check of the period-four exponential generating function."""
from collections import defaultdict
from math import comb

# The 19 finite-state certificate coefficients; (singletons, repeated types).
P4 = {
 (0,2):4,(0,3):8,(0,4):2,(1,2):36,(1,3):24,(1,4):4,
 (2,1):52,(2,2):68,(2,3):24,(2,4):2,
 (3,1):72,(3,2):48,(3,3):8,(4,0):25,(4,1):39,
 (4,2):12,(5,0):11,(5,1):8,(6,0):2,
}
# Treat E=exp(z) as a formal indeterminate. Expand z^a(E-1-z)^b
# in the integer polynomial ring Z[z,E]; no numerical evaluation is used.
got = defaultdict(int)
for (a,b), count in P4.items():
    for k in range(b+1):
        for r in range(b-k+1):
            got[(k,a+r)] += count*comb(b,k)*(-1)**(b-k)*comb(b-k,r)
got = {key: value for key,value in got.items() if value}
# 2E^4(z+1)^2-4E^2(z+1)(z+2)+E(-z^4+4z^2+8)
# -2(3z-1)(4z^2+z-1).
expected = {
 (4,0):2,(4,1):4,(4,2):2,
 (2,0):-8,(2,1):-12,(2,2):-4,
 (1,0):8,(1,2):4,(1,4):-1,
 (0,0):-2,(0,1):8,(0,2):2,(0,3):-24,
}
assert got == expected, (got, expected)
print('EXACT_EGF_POLYNOMIAL_IDENTITY_OK')
print('nonzero_terms=',len(got))

# An identical coefficient-ring calculation certifies the two recurrent-state
# counting formulas. Their E^0 corrections have bounded degree and affect
# only the exceptional small sizes excluded by the closed forms.
def expansion(table):
    result = defaultdict(int)
    for (a,b), count in table.items():
        for k in range(b+1):
            for r in range(b-k+1):
                result[(k,a+r)] += count*comb(b,k)*(-1)**(b-k)*comb(b-k,r)
    return {k:v for k,v in result.items() if v}

recurrent3 = {(1,0):9,(0,1):3,(2,0):3,(0,3):2}
expected3 = {
 (3,0):2,(2,0):-6,(2,1):-6,(1,0):9,(1,1):12,(1,2):6,
 (0,0):-5,(0,2):-3,(0,3):-2,
}
recurrent4 = {
 (0,4):2,(1,3):8,(0,3):8,(2,2):12,(1,2):16,(0,2):4,
 (4,1):1,(3,1):8,(2,1):8,(5,0):1,(4,0):3,
}
expected4 = {
 (4,0):2,(2,0):-8,(2,1):-8,
 (1,0):8,(1,1):8,(1,4):1,
 (0,0):-2,(0,2):4,
}
assert expansion(recurrent3) == expected3
assert expansion(recurrent4) == expected4
print('EXACT_RECURRENT_EGF_IDENTITIES_OK')
