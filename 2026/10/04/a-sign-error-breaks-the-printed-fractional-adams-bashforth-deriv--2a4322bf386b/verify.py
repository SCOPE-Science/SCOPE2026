#!/usr/bin/env python3
from fractions import Fraction
import math

# Exact endpoint witness h=1, Lambda=1, Delta=1, v=1.
h=1
v=1
Delta=Fraction(1)
correct=Delta*((v+1)-v)
printed=Delta*((v+1)+v)
assert correct == 1
assert printed == 3

# At h=1, fixed T=1 and Delta=1/N, the printed accumulated
# constant-forcing change is exactly N, while the true change is 1.
for N in (2,4,8,16,32):
    D=Fraction(1,N)
    accum=sum(D*((j+1)+j) for j in range(N))
    assert accum == N

# Representative fractional orders: direct formulas and refinement growth.
def incs(h,v,Delta=1.0,Lambda=1.0):
    c=Lambda**(1-h)*Delta**h/math.gamma(h+1)
    return c*((v+1)**h-v**h), c*((v+1)**h+v**h)

for h in (0.25,0.5,0.7,0.9,1.0):
    for v in (1,2,5):
        good,bad=incs(h,v)
        assert bad > good > 0

# For fixed T=1, Delta=1/N, printed accumulation grows ~ const*N.
for h in (0.3,0.7,1.0):
    vals=[]
    for N in (100,200,400):
        D=1.0/N
        c=D**h/math.gamma(h+1)
        bad=c*(N**h + 2*sum(j**h for j in range(1,N)))
        exact=1/math.gamma(h+1)
        assert bad > exact
        vals.append(bad)
    assert vals[1] > 1.8*vals[0]
    assert vals[2] > 1.8*vals[1]

print('VERIFY_OK')
print('integer_correct_increment', correct)
print('integer_printed_increment', printed)
print('integer_fixed_T_accum_N32', 32)
