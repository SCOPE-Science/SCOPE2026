from fractions import Fraction as Q

# Exact example: kappa=1, a=1/10, b=4, F=2, D=1.
kappa, a, b = Q(1), Q(1, 10), Q(4)
F, D, lam = Q(2), Q(1), Q(1, 1000)
ta, tb = kappa + a, kappa + b
tstar = min(tb, max(ta, 2*F/D))
q = lambda t: (2*F*D*t - 3*F*F) / (t**4)
lam_c = max(Q(0), q(tstar))
assert tstar == 4
assert lam_c == Q(1, 64)
assert lam < lam_c
# At c=3, t=4 and j''=lambda-q(t*)<0 exactly.
assert lam - q(kappa + Q(3)) == Q(-117, 8000)

def deriv(c):
    t = kappa + c
    return lam*c - F*F/(t**3) + F*D/(t**2)

# The unique stationary point is bracketed in (0.99, 0.999).
assert deriv(Q(99, 100)) < 0
assert deriv(Q(999, 1000)) > 0
# On c >= F/D-kappa = 1, the derivative is strictly positive.
assert deriv(Q(1)) > 0
assert deriv(Q(3)) > 0
print("VERIFY_OK", "lambda_c=1/64", "lambda=1/1000", "j''(c=3)=-117/8000")
