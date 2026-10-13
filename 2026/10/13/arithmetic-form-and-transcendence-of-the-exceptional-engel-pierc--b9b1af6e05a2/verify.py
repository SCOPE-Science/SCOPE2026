from fractions import Fraction
from decimal import Decimal, getcontext
from math import factorial

getcontext().prec = 200
EINV = (-Decimal(1)).exp()

def derangement(n):
    if n == 0: return 1
    if n == 1: return 0
    a,b=1,0
    for k in range(2,n+1):
        a,b=b,(k-1)*(a+b)
    return b

def tail_pair(m):
    # T_m = A + B/e
    return ((-1)**(m-1)*derangement(m-1), (-1)**m*factorial(m-1))

def tail_partial(m, J):
    s=Fraction(0)
    prod=1
    for j in range(J+1):
        prod *= m+j
        s += Fraction((-1)**j, prod)
    return s

def prefix_value(prefix):
    s=Fraction(0); prod=1
    for i,p in enumerate(prefix):
        prod *= p
        s += Fraction((-1)**i, prod)
    return s,prod

# Exact recurrence / derangement formula consistency.
A,B=tail_pair(1)
assert (A,B)==(1,-1)
for m in range(2,101):
    A0,B0=tail_pair(m-1)
    A1,B1=tail_pair(m)
    assert A1 == 1-(m-1)*A0
    assert B1 == -(m-1)*B0
    assert B1 != 0

# High-precision checks of the defining consecutive Pierce tails.
max_err=Decimal(0)
for m in range(1,21):
    A,B=tail_pair(m)
    closed=Decimal(A)+Decimal(B)*EINV
    s=tail_partial(m,50)
    approx=Decimal(s.numerator)/Decimal(s.denominator)
    err=abs(closed-approx)
    max_err=max(max_err,err)
    # alternating remainder bounded by first omitted term
    prod=1
    for j in range(52): prod*=m+j
    bound=Decimal(1)/Decimal(prod)
    assert err < bound*Decimal('1.0000000000000000001')

# Prefix gluing: compare full Pierce sum with rational-prefix + scaled closed tail.
cases=[([],1),([],2),([1],3),([2],5),([1,4],7),([2,5,9],12),([3,8,10,21],30)]
for prefix,m in cases:
    assert not prefix or prefix[-1] < m
    r,P=prefix_value(prefix)
    A,B=tail_pair(m)
    closed=Decimal(r.numerator)/Decimal(r.denominator) + (Decimal((-1)**len(prefix))/Decimal(P))*(Decimal(A)+Decimal(B)*EINV)
    # direct prefix + 70 tail terms
    ts=tail_partial(m,50)
    direct=r + Fraction((-1)**len(prefix),P)*ts
    directD=Decimal(direct.numerator)/Decimal(direct.denominator)
    assert abs(closed-directD) < Decimal('1e-65')

print(f"VERIFY_OK recurrence_cases=100 tail_cases=20 prefix_cases={len(cases)} max_error_lt_alternating_bound=1 nonzero_e_coeff=1")
