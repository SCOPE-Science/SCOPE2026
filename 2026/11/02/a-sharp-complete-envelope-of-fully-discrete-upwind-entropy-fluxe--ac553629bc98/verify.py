"""Exact-rational checks for a quadratic two-point entropy-flux classification.

These finite checks supplement, but do not replace, the all-state proof.
"""
from fractions import Fraction as F
from itertools import product

U = lambda a: a*a/2
H = lambda a,b,k: U(a) - k*(a-b)**2
checks = 0

for nu in (F(1,4),F(1,2),F(3,4),F(1),F(5,4)):
    vals = tuple(F(j) for j in range(-3,4))
    for k in (F(-1,8),F(0),F(1,16),F(1,8),F(1,4),F(1,2)):
        holds = True
        for left,center,right in product(vals,repeat=3):
            next_value = center - nu*(center-left)
            dissipation = U(center)-nu*(H(center,right,k)-H(left,center,k))-U(next_value)
            expected = nu*((F(1)-nu)/2-k)*(center-left)**2+nu*k*(center-right)**2
            assert dissipation == expected
            checks += 1
            if dissipation < 0:
                holds = False
        expected_all = F(0)<=k<=(F(1)-nu)/2
        assert holds == expected_all, (nu,k,holds,expected_all)
        checks += 1

for nu in (F(1,4),F(1,2),F(3,4),F(1)):
    for a,b in product((F(-2),F(-1),F(0),F(1),F(2)),repeat=2):
        z_plus = b + 2*nu*(a-b)
        h_low = U(b)+(U(z_plus)-U(b))/(2*nu)
        h_high=U(a)
        assert h_high-h_low == (F(1,2)-nu)*(a-b)**2
        for k in (F(0),F(1,16),F(1,8)):
            inside = h_low<=H(a,b,k)<=h_high
            if a!=b:
                predicted = nu<=F(1,2) and 0<=k<=F(1,2)-nu
                assert inside == predicted
            checks += 1

# An exact nonconstant example that is stable under every cell data,
# despite failure of the half-cell sufficient condition.
nu, k = F(3,4), F(1,16)
assert 0<k<(F(1)-nu)/2
assert F(1,2)-nu<0

print('PASS:', checks, 'exact-rational identities and interval tests')

# General (not necessarily polynomial) shared fluxes inside the sharp envelope.
for nu in (F(1,7),F(2,5),F(3,4),F(1)):
    # Pair-dependent coefficients are intentionally non-polynomial and asymmetric.
    def H_var(a,b):
        selector = F((2*abs(a)+3*abs(b)+7)%11, 10) / F(11,10)
        k_ab = (F(1)-nu)*selector/2
        return U(a)-k_ab*(a-b)**2
    for left,mid,right in product(range(-3,4),repeat=3):
        a,b,c = F(left),F(mid),F(right)
        updated=b-nu*(b-a)
        assert U(updated)<=U(b)-nu*(H_var(b,c)-H_var(a,b))
        checks+=1

# Every envelope violation admits a one-cell obstruction with one neighbor frozen.
for nu in (F(1,5),F(3,4)):
    for p,q in product((F(-2),F(-1),F(0),F(1),F(2)),repeat=2):
        if p==q:
            continue
        upper=U(p)
        lower=upper-(F(1)-nu)*(p-q)**2/2
        eps=F(1,100)
        for h_value in (upper+eps,lower-eps):
            if h_value>upper:
                # cell: left=center=p, right=q
                violation = U(p)-nu*(h_value-U(p))-U(p)
            else:
                # cell: left=p, center=right=q
                updated=q+nu*(p-q)
                violation = U(q)-nu*(U(q)-h_value)-U(updated)
            assert violation<0
            checks+=1
print('PASS:',checks,'total exact-rational algebraic and universality checks')
