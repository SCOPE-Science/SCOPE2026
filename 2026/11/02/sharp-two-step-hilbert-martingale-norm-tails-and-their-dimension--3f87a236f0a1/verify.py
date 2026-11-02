"""Exact-arithmetic regression checks for two-step bounded Hilbert martingale tails.

These finite tests check the stated extremal construction and algebraic formulas;
mathematical universal upper bounds are established separately by proof.
"""
from fractions import Fraction as Q

n = 0

def check(statement):
    global n
    assert statement
    n += 1

for a in range(1, 9):
    for b in range(1, 9):
        aa, bb = Q(a), Q(b)
        s = aa*aa + bb*bb
        m = (aa+bb)*(aa+bb)
        for x2 in (s, (s+m)/2, m):
            t = (x2-s)/(2*aa)
            q = bb/(bb+t)
            h2 = bb*bb-t*t
            check(Q(0) <= t <= bb)
            check(Q(0) <= h2)
            check(q*t == (Q(1)-q)*bb)
            check((aa+t)**2+h2 == x2)
            check((aa-bb)**2 < x2)
            check(q == 2*aa*bb/(x2-(aa-bb)**2))
            if x2 == s:
                check(q == 1 and t == 0)
            if x2 == m:
                check(q == Q(1,2) and t == bb and h2 == 0)
            if s < x2 < m:
                check(Q(1,2) < q < 1)
            if x2 > s:
                check(q <= s/x2)
                if a != b:
                    check(q < s/x2)
        for x2 in ((s+m)/2, m):
            qmax = 2*aa*bb/(x2-(aa-bb)**2)
            for k in (1,2,3,4,5,6,7):
                r = aa*Q(k,8)
                u = (x2-r*r-bb*bb)/(2*r)
                check(u > 0)
                check(bb/(bb+u) < qmax)
            # Equivalent factored condition for dominance over the scalar
            # optimizer: (a+b-sqrt(x2))*(sqrt(x2)+b-a) >= 0.
            check(x2 <= (aa+bb)**2 and x2 > (aa-bb)**2)
        # Fixed total squared-proxy Chebyshev envelope.
        for x2 in (s+Q(1,3), (s+m)/2, m):
            if x2 <= s: continue
            if x2 <= m:
                delta = (aa-bb)**2
                q = (s-delta)/(x2-delta)
                check(q <= s/x2)
                check((q == s/x2) == (a == b))

# Symbolic rational instance with two distinct step sizes and a nonzero
# transverse component: a=3, b=4, terminal squared threshold 30.
a,b,x2 = Q(3),Q(4),Q(30)
t=(x2-a*a-b*b)/(2*a)
q=b/(b+t)
h2=b*b-t*t
check(t==Q(5,6) and q==Q(24,29) and h2==Q(551,36))
check((a+t)**2+h2==x2)
check(q*t-(1-q)*b==0)
check((a-b)**2<x2)

print(f'PASS: {n} exact-rational assertions on norm, mean, support, sharpness, equality phases and parameter envelopes.')
print('Checks are finite algebraic evidence; the accompanying proof establishes all real parameters and Hilbert dimensions.')
