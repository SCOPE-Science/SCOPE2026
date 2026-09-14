"""Independent exact-arithmetic verification of the E_{6,3}(|x|) <= 0.02 certificate.
Uses only Python integers/Fractions (no floats). Recomputes from the
coefficient definitions: M=8000 uniform intervals on [0,1] with midpoint values
plus interval-local Lipschitz bounds. Exits 0 iff certified sup <= 1/50.
Run: python3 verify_certificate.py
"""
from fractions import Fraction as F

a0 = F('0.016343'); a2 = F('8.675825'); a4 = F('15.597868')
a6 = F('-1.619264'); b2 = F('21.310264')

# U(t) = P'(t)Q(t) - P(t)Q'(t), exact expansion:
# U0 = a2 - b2*a0, U1 = 2*a4, U2 = 3*a6 + a4*b2, U3 = 2*a6*b2.
U0 = a2 - b2*a0
U1 = 2*a4
U2 = 3*a6 + 2*a4*b2 - b2*a4
U3 = 2*a6*b2
# Valid monotonicity/positivity proof for the true U (U3 < 0):
# U'(t) = U1 + 2*U2*t + 3*U3*t^2, U''(t) = 2*U2 + 6*U3*t is decreasing in t,
# so min_[0,1] U'' = 2*U2 + 6*U3 > 0 implies U' is strictly increasing,
# hence min_[0,1] U' = U'(0) = U1 > 0, so U is strictly increasing;
# with U(0) = U0 > 0, U is positive on [0,1].
assert U0 > 0 and U1 > 0, "U(0), U'(0) must be positive"
assert 2*U2 + 6*U3 > 0, "min U'' on [0,1] must be positive"
assert a6 != 0 and b2 > 0

def Uf(t):
    return U0 + U1*t + U2*t*t + U3*t*t*t

def Efrac(x):
    t = x*x
    P = a0 + a2*t + a4*t*t + a6*t*t*t
    Q = 1 + b2*t
    assert Q >= 1
    return x - P/Q

M = 8000
worst = F(0); wk = 0
for k in range(M):
    l = F(k, M); r = F(k+1, M); m = (l + r)/2
    Em = abs(Efrac(m))
    # sup_[l,r] |R'| <= 2 r U(r^2)/(1+b2 l^2)^2 since U increasing, Q decreasing in t=x^2
    Lk = 1 + 2*r*Uf(r*r)/(1 + b2*l*l)**2
    Bk = Em + Lk*F(1, 2*M)
    if Bk > worst:
        worst = Bk; wk = k
print("certified sup_[0,1] |E| <=", float(worst))
print("exact:", worst)
print("worst interval:", wk)
assert worst <= F(1, 50), "CERTIFICATE FAILED"
print("PASS: sup <= 1/50 = 0.02")
