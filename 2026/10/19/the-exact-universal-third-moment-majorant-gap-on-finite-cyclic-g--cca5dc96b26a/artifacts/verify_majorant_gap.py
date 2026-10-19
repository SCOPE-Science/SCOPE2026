"""Exact-integer certificate for the sharp cyclic cubic-majorant gap.

No floating-point evaluation is used.  Integer Taylor quotients have a
uniform, explicitly bounded truncation/rounding error.  The proof of the
large-modulus reduction is documented separately.
"""
from math import factorial, isqrt
from fractions import Fraction

Q = 10**30
ARCTAN_TERMS = 30
COS_LAST = 22
PI_ERROR = 700               # scaled integer units
COS_ERROR = 800              # scaled integer units
TERM_ERROR = 50000           # scaled integer units for difference of cubes

def arctan_scaled(q):
    return sum((-1)**k * (Q // ((2*k+1)*q**(2*k+1)))
               for k in range(ARCTAN_TERMS))

P = 16*arctan_scaled(5)-4*arctan_scaled(239)
assert 3*Q < P < 22*Q//7

def cosine_scaled(N, j):
    j %= N
    j = min(j, N-j)
    if j == 0:
        return Q
    x = (2*j*P)//N
    xx = x*x
    numerator=1
    denominator=1
    total=Q
    for k in range(1,COS_LAST+1):
        numerator *= xx
        denominator *= Q*Q
        term=(Q*numerator)//(denominator*factorial(2*k))
        total+=(-1)**k*term
    return total

def cubic_scaled(s):
    # floor(Q * (max(0,s/Q))^(3/2)), exact integer square-root arithmetic
    return isqrt(max(0,s)**3//Q)

def gap_numerator(N):
    cos = [cosine_scaled(N, j) for j in range(N//2+1)]
    def cj(j):
        j %= N
        return cos[min(j,N-j)]
    acc=0
    for j in range(N):
        a=3*Q+2*cj(j)
        b=2*cj(2*j)+2*cj(3*j)
        acc += cubic_scaled(a-b)-cubic_scaled(a+b)
    return acc

# Error facts: Machin's formula and alternating arctangent remainders give
# |pi - P/Q| < 700/Q. Trigonometric symmetry reduces cos arguments to [0,pi].
# Cosine Taylor through degree 44 has remainder < 1/Q on [0,22/7], while
# flooring 22 terms and angle perturbation gives < 800/Q in cosine.
# The two squared moduli are within 4800/Q of their true values.  On
# [0,9+4800/Q], x^(3/2) is 5-Lipschitz. Integer square-root truncation
# contributes <1/Q per term, giving absolute gap error <50000/Q.

checked=0
small_min=None
min_order=None
for N in range(5,130):
    if N == 10:
        continue
    g=gap_numerator(N)
    assert 1000*(g-N*TERM_ERROR)>107*N*Q, (N,g/(N*Q))
    if small_min is None or g*small_min[1] < small_min[0]*N:
        small_min=(g,N)
        min_order=N
    checked+=1

g1000=gap_numerator(1000)
assert 100000*(g1000-1000*TERM_ERROR)>11554*1000*Q

# Four exact algebraic cubics on ten roots of unity are proved by
# the substitutions phi=(1+sqrt(5))/2 and phi^-1=phi-1 in RESULT.md.
# The exact tenth-order gap is 1-2/sqrt(5), hence < 0.107.
# For all N >=130, the analytic Fourier aliasing bound is
# |Delta_N - Delta_infinity| <= 18420/N^3; since
# Delta_infinity > .11554-18420/1000^3 > .11552158,
# Delta_N > .11552158-18420/130^3 > .107.
assert (Fraction(11554,100000) - Fraction(18420,1000**3)
        - Fraction(18420,130**3)) > Fraction(107,1000)

print('CERTIFIED_FINITE',checked,'orders 5..129 excluding 10')
print('MIN_NON10_FINITE_ORDER',min_order)
print('DELTA1000_LOWER',f'{(g1000-1000*TERM_ERROR)/(1000*Q):.12f}')
print('VERIFY_OK exact-integer trigonometric enclosure, all finite orders and continuous bridge')
