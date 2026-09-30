"""Audit the dimension-dependent residual exponents in the Section-10 barrier record.

This script deliberately distinguishes two formulas that the original package blurred:
(1) the literal residual exponent copied from the filed Dodson bookkeeping, and
(2) a generalized cutoff-deficit model used to test a monotone delta>=0 modification.
"""
from fractions import Fraction


def literal_residual(d: int) -> Fraction:
    return (Fraction(8,d)-Fraction(3,5*d)-Fraction(7,10*d*d))*Fraction(2*d,d-8)


def generalized_residual(d: int, delta: Fraction=Fraction(0)) -> Fraction:
    gain=(Fraction(8,d)-Fraction(1,5*d))*(1-Fraction(1,10*d)-delta)
    loss=Fraction(2,5*d)
    return (gain-loss)*Fraction(2*d,d-8)


def exact_delta_bound(d: int) -> Fraction:
    # generalized_residual(d,delta)>=2 iff delta <= this number
    return Fraction(77-5*d,39)-Fraction(1,10*d)

for d in (9,10,12,15,16,17,20,30):
    lit=literal_residual(d)
    gen=generalized_residual(d)
    bound=exact_delta_bound(d)
    print(f"d={d:2d} literal={float(lit):.12f} generalized(delta=0)={float(gen):.12f} delta_bound={float(bound): .12f}")

assert literal_residual(15) > 2
assert literal_residual(16) < 2
assert exact_delta_bound(15) > 0
assert exact_delta_bound(16) < 0
# delta enters with a negative coefficient for d>8.
for d in (9,15,16,20):
    assert generalized_residual(d, Fraction(1,100)) < generalized_residual(d, Fraction(0))
print('OK: d=16 obstruction verified; generalized delta>=0 cannot improve its residual.')
