"""Verification script for lane-1627 disproof of the Sklyanin C3-twist census claim.

Checks (all symbolic, reproducible with sympy only):
 A. Every normalized 2-cocycle mu on C3 with values in k^× is a coboundary
    (2-parameter classification + explicit trivialization via cube roots,
    which exist since k is algebraically closed of characteristic 0).
 B. d(x,y,z)=(x,w*y,w^2*z) has order 3 and preserves every Sklyanin relation.
 C. E1: x^3+y^3+z^3-3*L*xyz=0 with L^2=2 is smooth (empty singular locus,
    checked on all three affine charts by Groebner bases).
 D. Twisted-relation support: diagonal twist rescales monomials by nonzero
    scalars, so the twist keeps 3 generators and 3 nonzero quadratic relations.
"""
import itertools
import sympy as sp

print("=== A. normalized 2-cocycles on C3 are all coboundaries ===")
# indices 0,1,2 for 1,g,g^2; m[i][j] = mu(g^i,g^j), normalized: row/col 0 = 1
m11, m12, m21, m22 = sp.symbols('m11 m12 m21 m22')
m = {(0, 0): 1, (0, 1): 1, (0, 2): 1, (1, 0): 1, (2, 0): 1,
     (1, 1): m11, (1, 2): m12, (2, 1): m21, (2, 2): m22}
eqs = []
for i, j, k in itertools.product([0, 1, 2], repeat=3):
    lhs = m[(i, j)] * m[((i + j) % 3, k)]
    rhs = m[(i, (j + k) % 3)] * m[(j, k)]
    e = sp.simplify(lhs - rhs)
    if e != 0:
        eqs.append(e)
print(f"nontrivial cocycle equations: {len(eqs)}")
sol = sp.solve(eqs, (m11, m12, m21, m22), dict=True)
print("solutions:", sol)
assert len(sol) == 1
s = sol[0]
# solution: m12 = m21 = m11*m22; free parameters a=m11, d=m22 (both in k^×)
b_expr = s[m12]
assert sp.simplify(b_expr - m11 * m22) == 0
assert sp.simplify(s[m21] - b_expr) == 0
print("=> every normalized cocycle: mu(g,g^2)=mu(g^2,g)=mu(g,g)*mu(g^2,g^2)")

# verify the 2-parameter family indeed satisfies all 27 cocycle identities
a, d = sp.symbols('a d')
b = a * d
fam = {(0, 0): 1, (0, 1): 1, (0, 2): 1, (1, 0): 1, (2, 0): 1,
       (1, 1): a, (1, 2): b, (2, 1): b, (2, 2): d}
for i, j, k in itertools.product([0, 1, 2], repeat=3):
    lhs = fam[(i, j)] * fam[((i + j) % 3, k)]
    rhs = fam[(i, (j + k) % 3)] * fam[(j, k)]
    assert sp.simplify(lhs - rhs) == 0
print("=> 2-parameter family satisfies all 27 cocycle identities")

# Trivialization by hand (no Groebner needed): take gamma(1)=1, gamma(g)=a,
# gamma(g^2)=b. Then gamma(x)gamma(y)/gamma(xy) equals:
#   mu(g,g)  = a^2/b        (needs a^3/d = 1 after rescale),
# handled instead by normalized 1-cochain solve below.
# Direct constructive solve: write gamma(g)=s, gamma(g^2)=t (s,t nonzero).
# Conditions mu(g,g)=a: s^2/t=a; mu(g,g^2)=b: s*t=b  =>  s^3 = a*b, t = b/s.
# Since k alg. closed, s = cubert(a*b) exists (a*b != 0); then t = b/s != 0.
# Check remaining: mu(g^2,g)=b needs t*s=b (same equation, holds),
# mu(g^2,g^2)=d needs t^2/s=d. Now t^2/s = b^2/s^3 = b^2/(a*b) = b/a = a*d/a = d.
# All steps are field arithmetic; verify the key identity symbolically:
s_, t_ = sp.symbols('s_ t_')
assert sp.simplify((b**2 / (a * b)) - d) == 0
print("coboundary check: s^3=a*b, t=b/s gives s^2/t=a, s*t=b, t^2/s=b/a=d=a*d/a OK")
print("=> every normalized C3 2-cocycle with values in k^× is a coboundary")
print("   (uses existence of cube root of a*b in k; char != 3 since char 0)")

print()
print("=== B. diagonal automorphism d of order 3 preserves Sklyanin relations ===")
w = sp.symbols('w')
# w^2+w+1=0 => w^3=1, w!=1
print("rem(w^3-1, w^2+w+1) =", sp.rem(w**3 - 1, w**2 + w + 1, w))
assert sp.rem(w**3 - 1, w**2 + w + 1, w) == 0
A = {'x': 1, 'y': w, 'z': w**2}  # eigenvalues of d on (x,y,z)
rels = {'r1': (['y', 'z'], ['z', 'y'], ['x', 'x']),
        'r2': (['z', 'x'], ['x', 'z'], ['y', 'y']),
        'r3': (['x', 'y'], ['y', 'x'], ['z', 'z'])}
for r, (mA, mB, mC) in rels.items():
    facs = []
    for mon in (mA, mB, mC):
        f = sp.expand(A[mon[0]] * A[mon[1]])
        # reduce w^3 -> 1, w^4 -> w etc. via w^2+w+1=0
        r_ = sp.rem(f, w**2 + w + 1, w)
        facs.append(sp.simplify(r_))
    # all three monomials in one relation must share ONE common nonzero factor
    # (relation is semi-invariant, hence the ideal is preserved)
    assert facs[0] == facs[1] == facs[2], (r, facs)
    assert facs[0] != 0
    print(f"{r}: common eigenvalue-factor = {facs[0]}  -> d({r}) = {facs[0]}*{r}")
print("d^3 = id since (1,w,w^2)^3 = (1,1,1); d != id since w != 1 (w^2+w+1=0, char 0)")

print()
print("=== C. smoothness of E1: x^3+y^3+z^3-3*L*x*y*z, L^2=2 ===")
L, x, y, z = sp.symbols('L x y z')
f = x**3 + y**3 + z**3 - 3 * L * x * y * z
fx, fy, fz = sp.diff(f, x), sp.diff(f, y), sp.diff(f, z)
# singular locus needs L^3 = 1 (Hesse criterion); here (L^3)^2 = L^6 = (L^2)^3 = 8 != 1
print("L^6 - 1 mod (L^2-2) =", sp.rem(L**6 - 1, L**2 - 2, L))
assert sp.rem(L**6 - 1, L**2 - 2, L) == 7
for chart, sub in [('x=1', {x: 1}), ('y=1', {y: 1}), ('z=1', {z: 1})]:
    G = sp.groebner([L**2 - 2, f.subs(sub), fx.subs(sub),
                     fy.subs(sub), fz.subs(sub)], L, x, y, z,
                    order='lex')
    assert any(sp.simplify(g - 1) == 0 or sp.simplify(g + 1) == 0
               for g in G.polys), chart
    print(f"chart {chart}: singular ideal contains a nonzero constant "
          f"-> no singular point")
print("=> E1 smooth (also Hesse form: L^3 = 2L != 1 since (L^3)^2 = 8)")

print()
print("=== D. twist preserves monomial support (nonzero rescaling) ===")
# eigenvalues are 1, w, w^2 (all nonzero); mu-values are in k^× (nonzero).
# Each twisted monomial coefficient = old coeff * (mu-value) * (eigenvalue
# product), a product of nonzero scalars, hence nonzero.
ev = {'x': 1, 'y': w, 'z': w**2}
for r, (mA, mB, mC) in rels.items():
    for mon in (mA, mB, mC):
        assert ev[mon[0]] * ev[mon[1]] != 0
print("all 9 twisted monomial coefficients are products of nonzero scalars => nonzero")
print("=> twist is presented by 3 generators + 3 nonzero quadratic relations")
print()
print("ALL CHECKS PASSED")
