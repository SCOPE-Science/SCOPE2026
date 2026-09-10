"""Replayable certificate for lane-594 target (stdlib only, exact rational arithmetic).

Domain: Omega_r = {|z|<1} minus closed discs {|z-0.5|<=r}, {|z+0.5|<=r}, r in [0.20,0.35].
Trial function u(x,y)=x. Proves sup_M sigma1*L <= 161*pi/76 <= B0 - 0.10 with B0 = 6*pi.

Polynomial convention: lists of Fractions, index = power of r.
"""
from fractions import Fraction as Q


def pmul(a, b):
    c = [Q(0)] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            c[i + j] += x * y
    return c


def psub(a, b):
    n = max(len(a), len(b))
    return [ (a[i] if i < len(a) else Q(0)) - (b[i] if i < len(b) else Q(0)) for i in range(n) ]


def peval(a, r):
    return sum(x * r**i for i, x in enumerate(a))


# A(r) = (1+2r)(1-2r^2) = 1+2r-2r^2-4r^3 ; B(r) = 1+r+2r^3
A = [Q(1), Q(2), Q(-2), Q(-4)]
Apr = [Q(2), Q(-4), Q(-12)]
B = [Q(1), Q(1), Q(0), Q(2)]
Bpr = [Q(1), Q(0), Q(6)]

Nf = psub(pmul(Apr, B), pmul(A, Bpr))  # numerator of f'(r)
while len(Nf) > 1 and Nf[-1] == 0:
    Nf.pop()  # strip padding zero (r^5 cancels exactly)
assert Nf == [Q(1), Q(-4), Q(-20), Q(-16), Q(4)], Nf
print("N_f(r) =", [str(c) for c in Nf], " (r^5 cancels exactly)")

r_lo, r_hi = Q(1, 5), Q(7, 20)  # [0.20, 0.35]
assert peval(Nf, r_lo) == Q(-451, 625), peval(Nf, r_lo)
print("N_f(1/5) = -451/625 < 0  OK")

# N_f'(r) = -4-40r-48r^2+16r^3; rigorous upper bound on the interval:
# -40r <= -40*r_lo, -48r^2 <= -48*r_lo^2 (decreasing for r>0), 16r^3 <= 16*r_hi^3.
Nfp_ub = Q(-4) - Q(40) * r_lo - Q(48) * r_lo * r_lo + Q(16) * r_hi**3
assert Nfp_ub < 0, Nfp_ub
print("sup N_f' <=", float(Nfp_ub), "< 0  OK  => N_f decreasing => f decreasing")

# f(1/5) = A/B at r=1/5: A = 1+2/5-2/25-4/125 = (125+50-10-4)/125 = 161/125;
# B = 1+1/5+2/125 = (125+25+2)/125 = 152/125; f = 161/152.
assert peval(A, r_lo) == Q(161, 125) and peval(B, r_lo) == Q(152, 125)
print("f(0.2) = 161/152 exactly  OK")
print("Uniform certificate: sup_M S <= 2*pi*161/152 = 161*pi/76 ~", 161 * 3.141592653589793 / 76)

# Margin with only pi > 3 (Archimedes): B0 - F(0.2) - 0.10 = 295*pi/76 - 1/10
margin = Q(295) * Q(3) / Q(76) - Q(1, 10)
assert margin >= Q(11), margin
print("B0 - sup - 0.10 >= 295*3/76 - 1/10 =", float(margin), ">= 11 >> 0  OK")

# Cross-check against floats
import math
def F(r):
    return 2 * math.pi * (1 + 2 * r) * (1 - 2 * r * r) / (1 + r + 2 * r**3)
xs = [0.2 + i * 0.001 for i in range(151)]
assert max(F(x) for x in xs) == F(0.2)
assert 6 * math.pi - F(0.2) > 12.0
print("float cross-check: F(0.2) =", F(0.2), ", B0 - F(0.2) =", 6 * math.pi - F(0.2))
print("VERIFY_OK")
