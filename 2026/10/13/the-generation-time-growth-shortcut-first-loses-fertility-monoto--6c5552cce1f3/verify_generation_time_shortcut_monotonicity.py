#!/usr/bin/env python3
from decimal import Decimal, getcontext

getcontext().prec = 60

def shortcut(a,b):
    S = Decimal(a+b)
    return S*S.ln()/Decimal(a+2*b)

def exact_lambda(a,b):
    return (Decimal(a) + (Decimal(a*a+4*b)).sqrt())/Decimal(2)

def decreases_after_one_late_birth(a,b):
    # Compare S log S / D with (S+1) log(S+1)/(D+2)
    # by exponentiating the cross-multiplied logarithmic inequality.
    S=a+b
    D=a+2*b
    return pow(S, S*(D+2)) > pow(S+1, (S+1)*D)

# Exhaust every positive integer two-age schedule with initial R0 <= 6.
failures=[]
for S in range(2,7):
    for a in range(1,S):
        b=S-a
        dec=decreases_after_one_late_birth(a,b)
        if dec:
            failures.append((a,b))
        # Exact Euler-Lotka growth factor must increase after adding late fertility.
        assert exact_lambda(a,b+1) > exact_lambda(a,b)
        # Integer comparison agrees with high-precision logarithmic replay.
        assert dec == (shortcut(a,b+1) < shortcut(a,b))

assert failures == [(5,1)]

# Exact witness values.
lam1=exact_lambda(5,1)
lam2=exact_lambda(5,2)
q1=shortcut(5,1)
q2=shortcut(5,2)
assert lam1 < lam2
assert q1 > q2
assert 6**54 > 7**49

# Continuous mechanism: derivative wrt the late-age contribution b is
# [2S-a(1+log S)]/(2S-a)^2, where S=a+b.
def late_derivative_numerator(a,b):
    S=Decimal(a+b)
    return 2*S-Decimal(a)*(1+S.ln())
assert late_derivative_numerator(5,1) < 0

print('VERIFY_OK')
print('unique_first_failure', failures)
print('lambda_5_1', lam1)
print('lambda_5_2', lam2)
print('r_exact_5_1', lam1.ln())
print('r_exact_5_2', lam2.ln())
print('r_shortcut_5_1', q1)
print('r_shortcut_5_2', q2)
print('integer_certificate', '6^54 > 7^49')
