#!/usr/bin/env python3
"""Exact-arithmetic checks for a Pell cubic-window gcd theorem.

Use Python 3. No third-party dependencies. The finite tests support but do not
replace the unrestricted proof given in RESULT.md.
"""
from math import gcd

MAX_K = 480
P = [0, 1]
Q = [1, 1]
for _ in range(MAX_K + 50):
    P.append(2*P[-1] + P[-2])
    Q.append(2*Q[-1] + Q[-2])

def anti(x, y):
    return -16*x**3 - 3*x*x*y + 9*x*y*y - 2*y**3

def conjectured(k):
    if k & 1:
        return 1
    r = k//2
    t = Q[r] if (r & 1) else P[r]
    assert t % (7 if r%3==0 else 1) == 0
    return t//(7 if r%3==0 else 1) * (3 if r%4==0 else 1)

# Antidifference on genuine Pell states.
anti_checks = 0
for n in range(MAX_K + 24):
    assert anti(P[n+1],P[n+2]) - anti(P[n],P[n+1]) == 14*P[n]**3
    anti_checks += 1

cube = [z**3 for z in P]
prefix=[0]
for a in cube:
    prefix.append(prefix[-1]+a)

# The cubic Pell sequence obeys the rank-four recurrence.
recurrence_checks = 0
for n in range(0,MAX_K+18):
    assert cube[n+4] == 12*cube[n+3] + 30*cube[n+2] - 12*cube[n+1] - cube[n]
    recurrence_checks += 1

gcd_cases = 0
shift_cases = 0
for k in range(1,MAX_K+1):
    g=0
    for n in range(4):
        g=gcd(g,prefix[n+k]-prefix[n])
    assert g==conjectured(k), (k,g,conjectured(k))
    gcd_cases+=1
    for n in range(4,19):
        assert (prefix[n+k]-prefix[n])%g==0
        shift_cases+=1

matrix_cases=0
poly_cases=0
for r in range(1,MAX_K//2+1):
    t=Q[r] if r%2 else P[r]
    w=P[r] if r%2 else Q[r]
    if r%2:
        B=((t-w,w),(w,t+w))
    else:
        B=((2*t-w,w),(w,2*t+w))
    for n in range(10):
        x,y=P[n],P[n+1]
        nx=x+2*t*(B[0][0]*x+B[0][1]*y)
        ny=y+2*t*(B[1][0]*x+B[1][1]*y)
        assert (nx,ny)==(P[n+2*r],P[n+2*r+1])
        matrix_cases+=1
        delta=anti(nx,ny)-anti(x,y)
        assert delta%(2*t)==0
        phi=delta//(2*t)
        assert 7*(prefix[n+2*r]-prefix[n])==t*phi
        # At t=0 the polynomial remainder equals 3*w*G(x,y).
        G=15*x**3-9*x*x*y-x*y*y+y**3
        assert (phi-3*w*G)%t==0
        if not(r%2) and t%3==0:
            assert phi%3==0
        poly_cases+=1
    x=0;y=1
    nx=x+2*t*(B[0][0]*x+B[0][1]*y)
    ny=y+2*t*(B[1][0]*x+B[1][1]*y)
    phi0=(anti(nx,ny)-anti(x,y))//(2*t)
    if r%2==0 and t%3==0:
        assert phi0%9 == (3*w)%9

print('PASS exact Pell cubic-window gcd theorem')
print('gcd_lengths:',gcd_cases)
print('additional_shift_divisibility:',shift_cases)
print('antidifference_identities:',anti_checks)
print('fourth_order_recurrence_checks:',recurrence_checks)
print('Pell_matrix_identities:',matrix_cases)
print('integral_polynomial_and_congruence_checks:',poly_cases)
print('first_16_gcds:',[conjectured(k) for k in range(1,17)])
