"""Exact rational certificate for the alternating reciprocal-cube divisor range.

Run: python3 verify.py
Standard library only. Analytic tail theorem and prime-interval theorem
are proved/cited separately in RESULT.md. This program checks their finite
inputs and all component mergers and gaps without floating point arithmetic.
"""
from fractions import Fraction as Q
from itertools import product
from math import prod

PS = (2, 3, 5, 7)
N = 180


def alternating(p, exponent):
    q = Q(1, p ** 3)
    return sum(((-q) ** j for j in range(exponent + 1)), Q(0))


def zeta_bounds(n):
    # Integral-test bounds on the remaining reciprocal-cube series:
    # integral_(n+1)^infty x^-3 dx < sum_(k=n+1)^infty k^-3
    # < integral_n^infty x^-3 dx.
    partial = sum((Q(1, k**3) for k in range(1, n + 1)), Q(0))
    return partial + Q(1, 2 * (n + 1)**2), partial + Q(1, 2*n**2)


zlo, zhi = zeta_bounds(N)
B = prod((Q(1) - Q(1, p**3) for p in PS), start=Q(1))
tlo, thi = Q(1)/(zhi*B), Q(1)/(zlo*B)
assert 0 < tlo < thi < 1

# The value of each local prime factor is in an exact finite union of
# singleton points and, after multiplying by the prime >= 11 tail, intervals.
local = {
    2: [(alternating(2,0),alternating(2,0),'0'),
        (alternating(2,1),alternating(2,1),'1'),
        (alternating(2,2),alternating(2,2),'2'),
        (alternating(2,3),alternating(2,4),'>=3')],
    3: [(alternating(3,0),alternating(3,0),'0'),
        (alternating(3,1),alternating(3,2),'>=1')],
    5: [(alternating(5,0),alternating(5,0),'0'),
        (alternating(5,1),alternating(5,2),'>=1')],
    7: [(alternating(7,0),alternating(7,0),'0'),
        (alternating(7,1),alternating(7,2),'>=1')],
}
# Overlap of local exponent intervals within each grouped state.
for p in PS:
    if p==2:
        assert alternating(p,4)*thi < alternating(p,3)
    else:
        assert alternating(p,2)*thi < alternating(p,1)

witnesses = {11:(13,17,19),13:(17,19,23,29),
             17:(19,23),19:(23,29,31),23:(29,31,37)}
for p, primes in witnesses.items():
    assert all(q > p for q in primes)
    assert sum((Q(1,q**3) for q in primes),Q(0)) > Q(1,p**3)
# Nagura: three consecutive primes q_j < (6/5)^j p, for p>=29.
assert sum((Q(5,6)**(3*j) for j in range(1,4)),Q(0)) > 1

# Exact rational product intervals [L*T,U] for 32 low-prime states.
items=[]
for states in product(*(local[p] for p in PS)):
    L=prod((s[0] for s in states),start=Q(1))
    U=prod((s[1] for s in states),start=Q(1))
    items.append((L,U,tuple(s[2] for s in states)))
assert len(items)==32
# Certify unambiguous ordering of all lower endpoints for all T in [tlo,thi].
items.sort(key=lambda tup:tup[0])
assert all(items[i][0] < items[i+1][0] for i in range(31))
components=[]
overlap_count=0
gap_count=0
for L,U,tag in items:
    if not components or L*tlo > components[-1]['upper']:
        if components:gap_count+=1
        components.append({'lower':L,'upper':U,'members':[tag]})
    else:
        assert L*thi <= components[-1]['upper'], ('ambiguous comparison',L,U)
        overlap_count+=1
        components[-1]['members'].append(tag)
        if U > components[-1]['upper']:
            components[-1]['upper']=U
assert len(components)==19 and overlap_count==13 and gap_count==18
# Show exact coefficients and the exact integrity of each new gap.
for j,c in enumerate(components,1):
    print(f'{j:02d}  {c["lower"]}  {c["upper"]}  multiplicity={len(c["members"])}')
    if j>1:
        assert components[j-2]['upper'] < c['lower']*tlo
# Confirm exact endpoint coefficients and global endpoints (not numeric).
assert components[0]['lower']==Q(15314,18375)
assert components[-1]['lower']==Q(1)
assert components[-1]['upper']==Q(1)
assert sum(len(c['members']) for c in components)==32
print(f'EXACT_CERTIFICATE_OK local_states=32 components=19 gaps=18 overlaps=13 zeta_terms={N} tail_witnesses=5')
