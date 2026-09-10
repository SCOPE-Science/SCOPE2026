"""Master replay for lane-494 TARGET certificate (stdlib + sympy only, ~1 min).
Recomputes from the frozen Teragaito braid word every exact integer entering
the exclusion: Alexander/Conway (a2, a4, g, det), Jones + v3, chiral constant
C0 = 6033/323 with coprimality, in-scope Diophantine emptiness, torsion table,
Thm 1.10(i-c) non-firing check, Dedekind values. Exits 0 with VERIFY_OK iff all
pass. AUDIT REPAIR: alternating-sum V0 and all Ni-Wu d-values removed (false
identity); no d-invariant is claimed; Walker equation not asserted."""
import math
import sympy as sp
from fractions import Fraction as F

t = sp.Symbol('t')
z = sp.Symbol('z')
A = sp.Symbol('A')
ok = []
def check(name, cond):
    ok.append(bool(cond))
    print(("PASS " if cond else "FAIL ") + name)

# ---------- 1. Alexander via reduced Burau (validated matrices) ----------
def red(n, i):
    M = sp.eye(n - 1)
    if i == 1:
        M[0, 0] = -t
        if n - 1 > 1:
            M[1, 0] = 1
    elif i == n - 1:
        M[n - 2, n - 2] = -t
        if n - 1 > 1:
            M[n - 3, n - 2] = t
    else:
        M[i-2, i-2] = 1
        M[i-2, i-1] = t
        M[i-1, i-1] = -t
        M[i, i-1] = 1
    return M
A4, B4, C4 = red(4, 1), red(4, 2), red(4, 3)
check("burau dets -t", A4.det() == -t and B4.det() == -t and C4.det() == -t)
check("braid 121=212", sp.simplify(A4*B4*A4 - B4*A4*B4) == sp.zeros(3))
check("braid 232=323", sp.simplify(B4*C4*B4 - C4*B4*C4) == sp.zeros(3))
def alexander(n, word):
    B = sp.eye(n - 1)
    for i in word:
        B = red(n, i) * B
    num = sp.Poly((sp.eye(n - 1) - B).det(), t)
    den = sp.Poly(sum(t**k for k in range(n)), t)
    q, r = sp.div(num, den)
    assert r.is_zero
    return sp.expand(q.as_expr())
check("trefoil Delta", sp.expand(alexander(2, [1,1,1]) - (t**2 - t + 1)) == 0)
word = [1,1,2,2,1,2,2,2,2,2,2,2,2,2,1,2,2,3,2,1,1,2,2,1,3,2,2]
D = alexander(4, word)
Dwant = (t**24-t**23+t**20-t**19+t**17-t**16+t**15-t**14+t**12-t**10+t**9
         -t**8+t**7-t**5+t**4-t+1)
check("t12533 Alexander", sp.expand(D - Dwant) == 0)
check("Delta(1)=1", D.subs(t, 1) == 1)
check("symmetric", sp.expand(D - t**24*D.subs(t, 1/t)) == 0)
check("det=1", abs(int(sp.simplify(D.subs(t, -1)))) == 1)
# Conway a2, a4 via t+1/t solve
P = sp.Poly(D, t)
spn = P.degree()  # 24
gdeg = spn // 2
u = sp.Symbol('u')
T = {0: sp.Integer(1), 1: u}
for k in range(2, gdeg + 1):
    T[k] = sp.expand(u*T[k-1] - T[k-2])
Ds = sp.expand(D * t**(-spn//2))
cs = sp.symbols('c0:%d' % (gdeg + 1))
expr = sum(cs[k]*T[k] for k in range(gdeg + 1))
lhs = sp.expand(expr.subs(u, t + 1/t))
Pt = sp.Poly(sp.expand(lhs*t**gdeg), t)
Pd = sp.Poly(sp.expand(Ds*t**gdeg), t)
sol = sp.solve([Pt.nth(e) - Pd.nth(e) for e in range(2*gdeg + 1)], cs, dict=True)[0]
nabla = sp.expand(sum(sol[cs[k]]*T[k].subs(u, z**2 + 2) for k in range(gdeg + 1)))
Pn = sp.Poly(nabla, z)
a2, a4 = int(Pn.nth(2)), int(Pn.nth(4))
check("a2=52", a2 == 52)
check("a4=681", a4 == 681)
check("nabla(0)=1", Pn.nth(0) == 1)

# ---------- 2. Jones via TL + categorical trace (import helpers) ----------
import importlib.util
spec = importlib.util.spec_from_file_location("jt", "output/artifacts/jones_tl.py")
jt = importlib.util.module_from_spec(spec)
spec.loader.exec_module(jt)
spec2 = importlib.util.spec_from_file_location("js", "output/artifacts/jones_state.py")
js = importlib.util.module_from_spec(spec2)
spec2.loader.exec_module(js)
V3, _ = js.jones2(2, [1,1,1])
check("trefoil Jones", sp.simplify(V3 - (t + t**3 - t**4)) == 0)
V, info = js.jones2(4, word)
Vwant = -t**26+t**25-t**24+t**23-t**22-t**19+t**18-t**17+t**16+t**14+t**12
check("t12533 Jones", sp.simplify(V - Vwant) == 0)
check("V(1)=1", sp.simplify(V.subs(t, 1)) == 1)
Vpp = sp.diff(V, t, 2).subs(t, 1)
Vppp = sp.diff(V, t, 3).subs(t, 1)
check("V''(1)=-312", Vpp == -312)
check("-V''/6=a2", -Vpp/6 == 52)
check("V'''(1)=-10692", Vppp == -10692)
v3 = F(int(-Vppp), 144) * -1 + F(int(-Vpp), 48) * -1  # -V'''/144 - V''/48
v3 = F(-int(Vppp), 144) + F(-int(Vpp), 48)
check("v3=323/4", v3 == F(323, 4))
V3pp = sp.diff(V3, t, 2).subs(t, 1)
V3ppp = sp.diff(V3, t, 3).subs(t, 1)
check("trefoil v3=1/4", F(-int(V3ppp), 144) + F(-int(V3pp), 48) == F(1, 4))

# ---------- 3. Chiral constant + Diophantine ----------
num = 7*a2*a2 - a2 - 10*a4
check("numerator=12066", num == 12066)
C0 = F(num, 1) / (8*v3)
check("C0=6033/323", C0 == F(6033, 323))
check("gcd=1", math.gcd(6033, 323) == 1)
sols = []
for m in range(1, 31):
    for n in range(-30, 31):
        for np_ in range(-30, 31):
            if n == 0 or np_ == 0 or n == np_ or n + np_ == 0:
                continue
            if F(m, n + np_) == C0:
                sols.append((m, n, np_))
check("no in-scope +/- solutions", sols == [])
# same-sign distinct needs n+n'>=3 > 323m/6033 for m<=30
check("same-sign bound", all(3 > 323*m/6033 for m in range(1, 31)))

# ---------- 4. Torsion table (pure Alexander arithmetic; NO d-invariants claimed)
# AUDIT REPAIR: V0-via-alternating-sum was a false identity; all d(S^3_n,0)
# values, the m=17 self-gate, and d-sum language are deleted. The torsion
# coefficients below are direct arithmetic from the verified Alexander
# polynomial and are retained as slope datum only.
sym_a = {}
for j in range(-12, 13):
    sym_a[j] = int(P.nth(j + 12)) if 0 <= j + 12 <= 24 else 0
tors = [sum(j*sym_a.get(i+j, 0) for j in range(1, 13)) for i in range(12)]
check("torsion", tors == [4,4,4,3,3,2,2,2,1,1,1,1])
# Thm 1.10(i-c) does NOT fire: O(K)=12066/323 > 52/3=8|a2|/d, so the exclusion
# rests on the Diophantine + Varvarezos route, NOT on (i-c). Locked here to
# prevent the earlier inverted-conclusion error from recurring.
check("O=12066/323", F(num, 1)/(4*v3) == F(12066, 323))
check("(i-c) does not fire", F(12066, 323) > F(8*a2, 24))

# ---------- 5. Dedekind (exact) ----------
def saw(q):
    return q - int(q) - F(1, 2) if q != int(q) else F(0)
def ded(h, k):
    return sum(saw(F(r, k))*saw(F(h*r, k)) for r in range(1, k))
check("s(1,17)=20/17", ded(1, 17) == F(20, 17))
check("s(1,37)=105/37", ded(1, 37) == F(105, 37))
check("s(1,38)=111/38", ded(1, 38) == F(111, 38))
# reciprocity spot-check: s(1,17)+s(17,1) = (1+289+1)/(12*17)-1/4
check("reciprocity", ded(1, 17) + ded(17, 1) == F(1+289+1, 12*17) - F(1, 4))

print()
print("VERIFY_OK" if all(ok) else "VERIFY_FAIL", "(%d/%d)" % (sum(ok), len(ok)))
raise SystemExit(0 if all(ok) else 1)
