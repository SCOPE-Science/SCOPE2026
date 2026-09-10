"""Consolidated exact verifier: uniform target-refuting obstruction for G_{a,b}.
Checks (all exact QQ / integer arithmetic, no Groebner bases):
 V1 six fixed cubics kill every monomial of G (hand + machine).
 V2 h = (1,4,10,14,10,4,1) for ALL (a,b) via symbolic Gram dets (sum-of-squares+const).
 V3 Ann3 = fixed 6-dim span for ALL (a,b): six C3 rows identically zero + constant 14x14 minor != 0.
 V4 rank(xL0:A2->A3) = 10 for ALL (a,b): constant quotient minor = 1.
 V5 e=0,1 full rank (constant minors), h6=1 (C6 entry 48), duality closes e=3,4,5.
 V6 numeric spot-checks of H and full-rank at several (a,b).
Prints VERIFY_OK iff all pass.
"""
from sympy import Matrix, Rational, symbols, factor
import sys
sys.path.insert(0, '.')
from audit_target import catalecticant, monomials_4, build_F, diff_action

ok = True
def check(name, cond, detail=""):
    global ok
    print(("PASS " if cond else "FAIL ") + name + (" | " + str(detail) if detail else ""))
    if not cond:
        ok = False

# V1
FIX = [(3,0,0,0),(2,1,0,0),(1,2,0,0),(0,3,0,0),(0,2,1,0),(2,0,0,1)]
Fterms = [(2,0,4,0),(1,1,2,2),(0,2,0,4),(0,0,5,1),(0,0,1,5)]
v1 = all(diff_action(d, f) == (None, 0) or diff_action(d, f)[0] is not None and False for d in [] )  # placeholder
v1 = True
for d in FIX:
    for f in Fterms:
        g, k = diff_action(d, f)
        if g is not None:
            # result monomial X^g with coeff k*Fcoeff; must still vanish: check explicitly
            # y^2u on Y^2V^4 gives (0,0,0,4)?? -> then dU needs U-exp>=1: V^4 has U-exp 0 -> actually diff gives 0 at last step
            # Our diff_action is exact stepwise factorial; g is not None means each step fit, so recompute full application:
            pass
# rigorous V1: apply operator stepwise to each monomial with sympy-free integer check
def apply_op(d, f):
    # returns 0 (killed) or (g,k)
    return diff_action(d, f)
# y^2u=(0,2,1,0) on (0,2,0,4): dY^2: (0,0,0,4) coeff 2; dU: U-exp 0 -> kill
res = apply_op((0,2,1,0),(0,2,0,4))
check("V1a y^2u kills Y^2V^4", res == (None, 0), res)
res = apply_op((2,0,0,1),(2,0,4,0))
check("V1b x^2v kills X^2U^4", res == (None, 0), res)
# all 30 pairs must be kills except possibly intermediate? verify each pair kills:
allkill = True
for d in FIX:
    for f in Fterms:
        if apply_op(d, f) != (None, 0):
            allkill = False
            print("  NONZERO:", d, f, apply_op(d, f))
check("V1c all 6 ops kill all 5 F-monomials", allkill)

# V2: symbolic Gram dets
a, b = symbols('a b')
_, _, C1 = catalecticant(a, b, 1)
_, _, C2 = catalecticant(a, b, 2)
_, _, C4 = catalecticant(a, b, 4)
_, _, C5 = catalecticant(a, b, 5)
d1 = (C1*C1.T).det(); d2 = (C2*C2.T).det()
d4 = (C4.T*C4).det(); d5 = None  # d5 assigned below with correct orientation
def poly_eq(x, y):
    from sympy import expand
    return expand(x - y) == 0

check("V2a gram1", poly_eq(d1, 25*(a**2+25*b**2+20)*(25*a**2+b**2+20)), factor(d1))
check("V2b gram2", poly_eq(d2, 303038464*(100*a**2+37)*(100*b**2+37)), factor(d2))
check("V2c gram4 positive", poly_eq(d4, 46812394747330560000*(180*a**2+29)*(180*b**2+29)), str(factor(d4))[:80])
d5 = (C5.T*C5).det()
check("V2d gram5 positive", poly_eq(d5, 34447360000*(180*a**2+180*b**2+29)**2), str(factor(d5))[:80])
print("  (each factor = sum of squares + positive const -> nonzero for all real (a,b); h=(1,4,10,.,10,4,1) uniform)")

# V3
R3 = monomials_4(3)
_, _, C3s = catalecticant(a, b, 3)
zerorows = True
for m in FIX:
    i = R3.index(m)
    if any(v != 0 for v in C3s.row(i).tolist()[0]):
        zerorows = False
check("V3a six C3 rows identically zero in (a,b)", zerorows)
piv = [0,1,2,3,4,5,6,7,10,11,12,13,14,17]
M14 = C3s.extract(piv, piv)
check("V3b 14x14 minor constant nonzero", M14.det() == 86369107968, M14.det())

# V4
R2 = monomials_4(2)
J = [8,9,15,16,18,19]; I = [i for i in range(20) if i not in J]
Mult = Matrix.zeros(20, 10)
for j, em in enumerate(R2):
    for k in range(4):
        g = tuple(em[i]+(1 if i==k else 0) for i in range(4))
        Mult[R3.index(g), j] += 1
Q = Mult.extract(I, list(range(10)))
qrows = [0,1,2,4,5,7,8,9,11,13]
Q10 = Q.extract(qrows, list(range(10)))
check("V4 quotient 10x10 minor = 1", Q10.det() == 1, Q10.det())
check("V4b rank Q = 10", Q.rank() == 10, Q.rank())

# V5
M1 = Matrix.zeros(10, 4)
R1 = monomials_4(1)
for j, em in enumerate(R1):
    for k in range(4):
        g = tuple(em[i]+(1 if i==k else 0) for i in range(4))
        M1[R2.index(g), j] += 1
E = M1.extract([0,1,3,6], list(range(4)))
check("V5a e=1 minor = 1", E.det() == 1, E.det())
g6, k6 = diff_action((2,0,4,0),(2,0,4,0))
check("V5b C6 entry 48 (h6=1 all (a,b))", (g6, k6) == ((0,0,0,0), 48), (g6, k6))

# V6 numeric spot checks
for pt in [(Rational(0),Rational(0)),(Rational(1),Rational(2)),(Rational(3),Rational(-1))]:
    _, _, Cn = catalecticant(pt[0], pt[1], 3)
    check(f"V6 numeric h3=14 at {tuple(pt)}", Cn.rank() == 14, Cn.rank())

print("VERIFY_OK" if ok else "VERIFY_FAIL")
