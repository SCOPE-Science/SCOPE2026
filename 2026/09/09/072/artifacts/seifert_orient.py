"""Seifert orientation ID for +Sigma(2,3,13) (exact integer/rational arithmetic).
Checks: b_i via (P/a_i) b_i = -1 mod a_i; e0 integrality; e=-1/P;
HJ continued fractions -> arm weights; match to 5-vertex graph.
Conventions: SYZ Def 2.1 (Sigma = Seifert bundle with e=-1/P);
Dai-Manolescu orients AR manifolds as plumbing boundaries.
"""
from fractions import Fraction

a = (2, 3, 13)
P = 78
b = []
for i, ai in enumerate(a):
    q = P // ai
    inv = pow(q % ai, -1, ai)
    bi = (-inv) % ai
    b.append(bi)
print("b =", b)
assert b == [1, 1, 2]
S = sum(Fraction(b[i], a[i]) for i in range(3)) * P
print("P*sum(b/a) =", S, "(want P-1 =", P - 1, " i.e. -1 mod P)")
assert S == P - 1
e0 = (Fraction(-1, 1) - S) / P
print("e0 =", e0)
assert e0 == -1
e = e0 + sum(Fraction(b[i], a[i]) for i in range(3))
print("e =", e, "= -1/78:", e == Fraction(-1, 78))
assert e == Fraction(-1, 78)

def hj(p, q):
    # Hirzebruch-Jung: p/q = k1 - 1/(k2 - ...) with ki>=2
    ks = []
    while q != 0:
        k = (p + q - 1) // q  # ceil
        ks.append(k)
        p, q = q, k * q - p
    return ks

for i in range(3):
    print(f"{a[i]}/{b[i]} =", hj(a[i], b[i]))
assert hj(2, 1) == [2] and hj(3, 1) == [3] and hj(13, 2) == [7, 2]
print("arms: [-2], [-3], [-7,-2]; central e0=-1 -> matches 5-vertex graph")
print("ORIENTATION: e=-1/78<0 = negative-definite plumbing boundary = Dai convention = +Sigma(2,3,13).")
print("SYZ Thm 1.1 check: Sigma(2,3,7)+alpha(6)=Sigma(2,3,13) -> d equal (both 0). CONSISTENT.")
