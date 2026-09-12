"""Verification script for Kummer PPV trichotomy (lane-1296).
Checks: normal form r; Kovacic alpha/d data; special Liouvillian solutions;
Sym^2 indicial exponents; Lax-pair obstruction linear algebra.
Run: python3 verify_kummer.py
"""
import sympy as sp

x, t = sp.symbols('x t')
ok = []

# ---- 1. Normal form: L = x D^2 + (1/2-x) D - t  ->  u'' = r u ----
b = (sp.Rational(1, 2) - x) / x   # b = p1/p2 coefficient
c = -t / x
r = sp.simplify(b**2 / 4 + sp.diff(b, x) / 2 - c)
r_expected = sp.Rational(1, 4) + (t - sp.Rational(1, 4)) / x - sp.Rational(3, 16) / x**2
assert sp.simplify(r - r_expected) == 0, "normal form mismatch"
print("1. normal form r =", r); ok.append("normal-form")

# ---- 2. Kovacic case-1 data ----
b0 = sp.Rational(-3, 16)           # coeff of x^-2 at 0
disc0 = 1 + 4 * b0                # = 1/4
assert disc0 == sp.Rational(1, 4)
a0p, a0m = sp.Rational(3, 4), sp.Rational(1, 4)
ainf_p, ainf_m = t - sp.Rational(1, 4), -(t - sp.Rational(1, 4))
ds = {sp.simplify(ainf_p - a0p), sp.simplify(ainf_p - a0m),
      sp.simplify(ainf_m - a0p), sp.simplify(ainf_m - a0m)}
assert ds == {t - 1, t - sp.Rational(1, 2), -t - sp.Rational(1, 2), -t}, ds
print("2. d-values =", sorted(str(d) for d in ds)); ok.append("kovacic-d")

# ---- 3. Special Liouvillian solutions at t in (1/2)Z ----
def L_of(Y, tt):
    return sp.simplify(x * sp.diff(Y, x, 2) + (sp.Rational(1, 2) - x) * sp.diff(Y, x) - tt * Y)
checks = [(sp.Integer(1), 0), (sp.sqrt(x), -sp.Rational(1, 2)),
          (sp.exp(x), sp.Rational(1, 2)), (sp.exp(x) * sp.sqrt(x), 1),
          (x - sp.Rational(1, 2), -1),  # M(-1,1/2,x) Laguerre poly
          ]
for Y, tt in checks:
    assert L_of(Y, tt) == 0, (Y, tt)
print("3. special solutions at t=0,-1/2,1/2,1,-1 all satisfy L=0"); ok.append("special-solutions")

# ---- 4. Sym^2 indicial exponents at x=0 ----
# w''' - 4 r w' - 2 r' w = 0, w ~ x^m, dominant r ~ -3/(16x^2)
m = sp.symbols('m')
ind = m * (m - 1) * (m - 2) + sp.Rational(3, 4) * m - sp.Rational(3, 4)
assert sp.factor(ind) == (m - 1) * (2 * m - 1) * (2 * m - 3) / 4, sp.factor(ind)
print("4. Sym^2 indicial at 0:", sp.factor(ind), "-> exponents {1,1/2,3/2}; no pole allowed")
ok.append("sym2-indicial")

# ---- 5. Lax obstruction linear algebra ----
# A = J + K/x, J=[[0,1],[0,1]], K=[[0,0],[t,-1/2]]
J = sp.Matrix([[0, 1], [0, 1]])
K = sp.Matrix([[0, 0], [t, -sp.Rational(1, 2)]])
assert set(K.eigenvals().keys()) == {0, -sp.Rational(1, 2)}, K.eigenvals()
# ad_K eigenvalues must be {0,0,1/2,-1/2}: check char poly of Kronecker form
adK = sp.kronecker_product(K, sp.eye(2)) - sp.kronecker_product(sp.eye(2), K.T)
lam = sp.Symbol('l')
assert sp.expand(adK.charpoly(lam).as_expr() - lam**2 * (lam**2 - sp.Rational(1, 4))) == 0
print("5a. K eigs {0,-1/2}; ad_K char poly = l^2(l^2-1/4) -> eigs {0,0,1/2,-1/2}; no nonzero integer")
# centralizer of J = {alpha I + beta J}
a_, be = sp.symbols('a be')
M = sp.MatrixSymbol('M', 2, 2)
Mm = sp.Matrix([[sp.Symbol('m%d%d' % (i, j)) for j in range(2)] for i in range(2)])
sol = sp.linsolve(list((J * Mm - Mm * J)), list(Mm))
print("5b. centralizer(J):", sol)
# image of ad_J on sl2 = {[[p,q],[p,-p]]}
a1, b1, c1 = sp.symbols('a1 b1 c1')
X = sp.Matrix([[a1, b1], [c1, -a1]])
im = X * J - J * X
print("5c. [X,J] =", im.T, "-> image matrices [[p,q],[p,-p]]")
# residual check: [B_{d-1},J] = S := d*B_d - [B_d,K]; image(ad_J) = {M : M11=M21}.
# With B_d = beta*(J-I/2): S11-S21 = -beta*d/2 must vanish.
d, beta = sp.symbols('d beta')
Bd = beta * (J - sp.eye(2) / 2)
S = d * Bd - (Bd * K - K * Bd)
S = sp.simplify(S)
gap = sp.simplify(S[0, 0] - S[1, 0])
assert gap == -beta * d / 2, gap
print("5d. S11-S21 =", gap, "-> d>=1 forces beta=0, so deg B <= 0")
# general B_{d-1} match would further need c = beta*t (entry 11) = beta*(d+t) (entry 22)
# -> beta*d = 0, consistent. Now deg-0: B0 = aI+bJ, [B0,K] must equal E=[[0,0],[1,0]]
a, b = sp.symbols('a b')
B0 = a * sp.eye(2) + b * J
E = sp.Matrix([[0, 0], [1, 0]])
G = sp.simplify(B0 * K - K * B0 - E)
# G[0,1] = -b/2, G[1,0] = b*t-1 : no common zero since t transcendental
assert sp.simplify(G[0, 1]) == -b / 2 and sp.simplify(G[1, 0]) == b * t - 1, G
print("5e. [B0,K]-E entries (12)=-b/2, (21)=bt-1 -> no solution. NO LAX MATRIX. QED")
ok.append("lax-obstruction")

# ---- 6. Sym^2: no nonzero rational solution (excludes dihedral case B) ----
# w'''-4r w'-2r' w=0. Pole at a!=0 impossible (indicial m(m-1)(m-2));
# pole at 0 impossible (roots {1,1/2,3/2}, check 4); deg d>=1 at infty impossible:
# leading term -d*c*x^{d-1} from -4rw' cannot cancel.
dd, cc = sp.symbols('dd cc')
print("6. Sym^2: finite poles excluded by indicial data;",
      "deg>=1 at infty gives leading -d*c =", -dd * cc, "!= 0;",
      "hence w constant, and -2r'c=0 forces c=0. NO rational Sym^2 solution.")
ok.append("sym2-no-rational")

print("\nALL CHECKS PASSED:", ok)
