import sympy as sp

u, b, c, q = sp.symbols("u b c q", positive=True)

# Pointwise identity whose invariant-measure average yields the exact defect.
identity = sp.simplify(
    (u - b)
    - (1 + c*b) * (u - b) / (1 + c*u)
    - c * (u - b)**2 / (1 + c*u)
)
assert identity == 0

# Difference of the rational response at the mean and at a point.
gap = sp.simplify(b/(1+c*b) - u/(1+c*u))
assert sp.simplify(gap - (b-u)/((1+c*b)*(1+c*u))) == 0

# Combining the two identities after averaging gives the coefficient qc/(1+cb)^2.
coef = sp.simplify(q/(1+c*b) * c/(1+c*b))
assert coef == q*c/(1+c*b)**2

# Response derivative used for the global Lipschitz variance estimate.
response = q*u/(1+c*u)
deriv = sp.simplify(sp.diff(response, u))
assert deriv == q/(1+c*u)**2

print("VERIFY_OK")
