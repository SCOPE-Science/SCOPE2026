import sympy as sp

e, kappa, p = sp.symbols("e kappa p", positive=True)

# Normalize the smallest eigenvalue to one.
# A = diag(kappa, 1), g0 = (sqrt(e), 1).
r0 = (kappa*e + 1)/(e + 1)
tau0 = 1/r0

g1_hi = sp.simplify((1-kappa*tau0)*sp.sqrt(e))
g1_lo = sp.simplify(1-tau0)

assert sp.simplify(
    g1_hi + sp.sqrt(e)*(kappa-1)/(1+kappa*e)
) == 0
assert sp.simplify(
    g1_lo - e*(kappa-1)/(1+kappa*e)
) == 0
assert sp.simplify((g1_hi**2)/(g1_lo**2) - 1/e) == 0

# First fixed-p LEFT step after the exact line-search warm-up.
h1 = p/r0
g2_hi = sp.simplify((1-h1*kappa)*g1_hi)
g2_lo = sp.simplify((1-h1)*g1_lo)

grad_ratio = sp.simplify(
    (g2_hi**2 + g2_lo**2)/(g1_hi**2 + g1_lo**2)
)
obj_ratio = sp.simplify(
    (g2_hi**2/kappa + g2_lo**2) /
    (g1_hi**2/kappa + g1_lo**2)
)

target = (p*kappa - 1)**2
assert sp.simplify(sp.limit(grad_ratio, e, 0, dir="+") - target) == 0
assert sp.simplify(sp.limit(obj_ratio, e, 0, dir="+") - target) == 0

# Representative below-frontier case: every modal factor is nonexpansive.
for kval, pval in [(sp.Rational(6,5), sp.Rational(3,2)),
                   (sp.Rational(4,3), sp.Rational(3,2))]:
    assert pval*kval <= 2
    for rval in [1, (1+kval)/2, kval]:
        h = pval/rval
        assert abs(float(1-h)) <= 1 + 1e-12
        assert abs(float(1-h*kval)) <= 1 + 1e-12

# Above the frontier, a sufficiently small witness produces actual growth.
for kval, pval in [(3, sp.Rational(3,2)), (10, sp.Rational(3,2)),
                   (2, sp.Rational(19,10))]:
    assert pval*kval > 2
    val_g = float(grad_ratio.subs({kappa:kval, p:pval, e:sp.Rational(1,10**8)}))
    val_f = float(obj_ratio.subs({kappa:kval, p:pval, e:sp.Rational(1,10**8)}))
    assert val_g > 1
    assert val_f > 1
    assert abs(val_g - float(target.subs({kappa:kval,p:pval}))) < 1e-4
    assert abs(val_f - float(target.subs({kappa:kval,p:pval}))) < 1e-4

print("VERIFY_OK")
