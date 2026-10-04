from fractions import Fraction
import cmath

def coeffs(s):
    s=Fraction(s)
    return (
        Fraction(117,1250)*s-Fraction(29,10),
        Fraction(1751,625)-Fraction(5129,31250)*s,
        Fraction(1127,15625)*s-Fraction(1127,1250),
    )

def jury(s):
    a,b,c=coeffs(s)
    return (1-c,1+c,1+a+b+c,1-a+b-c,1-b+a*c-c*c)

bound=Fraction(19800,859)
# Exact inequalities strictly inside.
for s in (Fraction(1,10),Fraction(1),Fraction(10),bound-Fraction(1,1000)):
    vals=jury(s)
    assert all(v>0 for v in vals)

# Active boundary is the -1 condition.
a,b,c=coeffs(bound)
assert 1-a+b-c == 0
assert (-1)**3 + a*(-1)**2 + b*(-1) + c == 0
assert 1-c>0 and 1+c>0 and 1+a+b+c>0 and 1-b+a*c-c*c>0

# Immediately above, Schur fails.
assert jury(bound+Fraction(1,1000))[3] < 0

# The other upper candidate is looser.
assert bound < Fraction(59425,2254)

# First-moment-only comparison.
assert Fraction(198,1)/bound == Fraction(859,100)

print('verification passed')
