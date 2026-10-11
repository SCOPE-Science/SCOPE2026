import sympy as sp

x, k = sp.symbols("x k", positive=True, real=True)
s = sp.sin(x)
c = sp.cos(x)
H = 1 + (4*k**2 - 1)*s**2

def L(u, n):
    return sp.simplify(
        sp.diff(u, x, 2)
        + (4*k**2 - 1)*s*c/H * sp.diff(u, x)
        - n**2/H*u
        + (2 + 8*k**2/H**2)*u
    )

# First positive odd threshold.
uplus = (1 + (2*k - 1)*s**2) / sp.sqrt(H)
assert sp.simplify(sp.trigsimp(L(uplus, 2*k + 1))) == 0

# Last negative odd threshold.
raw = sp.together(sp.trigsimp(L(s, 2*k - 1)/s))
num, den = raw.as_numer_denom()
z = sp.symbols("z", nonnegative=True, real=True)
num_z = sp.factor(
    sp.expand_trig(num)
      .subs(sp.cos(x)**2, 1-sp.sin(x)**2)
      .subs(sp.sin(x)**2, z)
)
target_num = (2*k-1)*(2*k+1)*(4*k-1)*z + 8*k**2 + 4*k - 1
assert sp.factor(num_z-target_num) == 0
assert sp.factor(den - H**2) == 0

# Unit normal for the oriented double cover.
y = sp.symbols("y", real=True)
F = sp.Matrix([
    sp.cos(y)*sp.cos(x),
    sp.sin(y)*sp.cos(x),
    sp.cos(2*k*y)*sp.sin(x),
    sp.sin(2*k*y)*sp.sin(x),
])
nu = sp.Matrix([
    -2*k*sp.sin(x)*sp.sin(y)/sp.sqrt(H),
     2*k*sp.sin(x)*sp.cos(y)/sp.sqrt(H),
     sp.cos(x)*sp.sin(2*k*y)/sp.sqrt(H),
    -sp.cos(x)*sp.cos(2*k*y)/sp.sqrt(H),
])
assert sp.simplify((F.dot(nu))) == 0
assert sp.simplify(sp.diff(F,x).dot(nu)) == 0
assert sp.simplify(sp.diff(F,y).dot(nu)) == 0
assert sp.simplify(nu.dot(nu)-1) == 0

R13 = sp.expand_trig(F[0]*nu[2] - F[2]*nu[0])
uplus_half = uplus/2
uminus_half = (1-(2*k+1)*sp.sin(x)**2)/(2*sp.sqrt(H))
rhs = (
    uplus_half*sp.sin((2*k+1)*y)
    + uminus_half*sp.sin((2*k-1)*y)
)
assert sp.simplify(sp.trigsimp(R13-rhs)) == 0

# Ground-state transform checked algebraically at the integrand level.
f = sp.Function("f")(x)
w = sp.sqrt(2*H)
q = (2*k+1)**2/H - 2 - 8*k**2/H**2
lhs = sp.diff(f,x)**2 + q*f**2
g = f/uplus
rhs_density = uplus**2*sp.diff(g,x)**2
# Weighted ground-state identity; the difference is an exact boundary derivative.
boundary_term = sp.diff(w*sp.diff(uplus,x)/uplus*f**2, x)
assert sp.simplify(sp.trigsimp(w*(lhs-rhs_density)-boundary_term)) == 0

# Deterministic sign diagnostics for small integer k.
for K in range(1, 11):
    pos_const = 8*K*K + 4*K - 1
    pos_slope = (2*K-1)*(2*K+1)*(4*K-1)
    assert pos_const > 0 and pos_slope > 0

print("VERIFY_OK")
print("symbolic_positive_zero_mode=true")
print("symbolic_negative_threshold_identity=true")
print("rotational_jacobi_decomposition=true")
print("ground_state_transform=true")
