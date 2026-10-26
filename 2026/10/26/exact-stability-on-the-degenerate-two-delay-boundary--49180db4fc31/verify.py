import sympy as sp

# Real symbols for the local characteristic-root calculation.
a, c, w, tau = sp.symbols("a c w tau", real=True)
I = sp.I
lam = I*w
F = 1 + 2*c*tau
T = 2*(a - 3*c + I*w)
lam_prime = -2*c*lam/F
f_ll = tau**2*T
f_ltau = 2*c + tau*lam*T
f_tautau = lam**2*T
lam_second = sp.factor(-(f_ll*lam_prime**2 + 2*f_ltau*lam_prime + f_tautau)/F)
expected_second = sp.factor(-T*lam**2/F**3 + 8*c**2*lam/F**2)
assert sp.simplify(lam_second - expected_second) == 0
assert sp.simplify(sp.re(lam_second) - 2*w**2*(a-3*c)/F**3) == 0
assert sp.simplify(sp.re(lam_prime)) == 0

# Exact algebraic witness on both signs of b.
for bsign in (1, -1):
    av, cv = sp.Integer(2), sp.Integer(1)
    bv = bsign*2*sp.sqrt(2)
    wv = sp.Integer(1)
    assert sp.simplify(bv**2 - 8*cv*(av-cv)) == 0
    assert sp.simplify((av-cv)*(3*cv-av) - wv**2) == 0
    cosv = sp.simplify(2*(cv-av)/bv)
    sinv = sp.simplify(2*wv/bv)
    assert sp.simplify(cosv**2 + sinv**2 - 1) == 0
    assert sp.simplify(av+bv+cv) > 0
    assert sp.simplify(2*(av**2-cv**2)-bv**2) < 0
    assert sp.simplify(bv**2 + 8*cv*(cv-av)) == 0

# Check the closed-form local contact coefficient is strictly negative
# for the witness, for any positive critical delay.
t = sp.symbols("t", positive=True, real=True)
assert sp.simplify(2*1**2*(2-3)/(1+2*1*t)**3) < 0
print("PASS: implicit first/second derivative identities")
print("PASS: real-part second derivative formula")
print("PASS: both signs of the exact exceptional-locus witness")
print("PASS: strict negative tangency coefficient")
