#!/usr/bin/env python3
import math
from decimal import Decimal, getcontext


def d(n):
    return n * (n + 1) // 2


def H(n):
    z = 1
    for j in range(n):
        z *= (2*j + 1) ** (n-j)
    return z


def numerator(q,n):
    return (q-1) ** d(n) * math.factorial(d(n))


def denominator(n):
    return H(n) ** 2

# Exact ratio identity after cross-multiplication.
for q in range(3,9):
    for n in range(2,21):
        lhs_num = numerator(q,n) * denominator(n-1)
        lhs_den = denominator(n) * numerator(q,n-1)
        prod = 1
        for j in range(1,n+1):
            prod *= d(n-1) + j
        odd = math.prod(range(1,2*n,2))
        rhs_num = (q-1)**n * prod
        rhs_den = odd**2
        assert lhs_num * rhs_den == rhs_num * lhs_den

getcontext().prec = 70
ln2 = Decimal(2).ln()
ln3 = Decimal(3).ln()
c3 = (Decimal(1)-ln2)/Decimal(25)
c4 = (Decimal(1)+ln3/Decimal(2)-Decimal(3)*ln2/Decimal(2))/Decimal(36)
assert c4 > c3

# Numerical profile check, supplementary to the analytic derivative proof.
def cq(q):
    return (Decimal(1)+Decimal(q-1).ln()/Decimal(2)-Decimal(3)*ln2/Decimal(2))/Decimal(q+2)**2
vals = [(cq(q),q) for q in range(3,1001)]
assert max(vals)[1] == 4

print('c3=', c3)
print('c4=', c4)
print('relative_improvement=', c4/c3-1)
print('integer_q_max_checked=4 on 3..1000')
print('CHECK_OK')
