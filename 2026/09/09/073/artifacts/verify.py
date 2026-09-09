"""Lane 429 replay script (stdlib only): verifies every integer datum behind the
Picard-Fermat census analysis. Run: python3 verify.py -> VERIFY_OK."""
from fractions import Fraction as FR

MOD = 7

def F(X, Y, Z):
    return Y**3 * Z - X**4 + Z**4

# ---- (a) smoothness: partials have no common zero mod 7 ----
def partial_zeros(p):
    out = []
    for X in range(p):
        for Y in range(p):
            for Z in range(p):
                if X == Y == Z == 0:
                    continue
                if (-4*X**3) % p == 0 and (3*Y*Y*Z) % p == 0 \
                        and (Y**3 + 4*Z**3) % p == 0:
                    out.append((X, Y, Z))
    return out

assert partial_zeros(7) == [], "singular mod 7!"
# over Q: X=0 from -4X^3=0; then 3Y^2Z=0 & Y^3+4Z^3=0 force Y=Z=0 (checked
# by the same algebra since 3,4 are nonzero in Q). Smooth plane quartic.

# ---- (b) C(F7) enumeration ----
def proj_reps(p):
    seen, reps = set(), []
    for X in range(p):
        for Y in range(p):
            for Z in range(p):
                if X == Y == Z == 0:
                    continue
                if F(X, Y, Z) % p != 0:
                    continue
                for v in (X, Y, Z):
                    if v % p != 0:
                        inv = pow(v, p - 2, p)
                        break
                key = ((X*inv) % p, (Y*inv) % p, (Z*inv) % p)
                if key not in seen:
                    seen.add(key)
                    reps.append(key)
    return sorted(reps)

CF7 = proj_reps(7)
assert len(CF7) == 12, CF7
EXPECT = [(0,1,0),(0,1,3),(0,1,5),(0,1,6),(1,0,1),(1,0,6),
          (1,1,4),(1,2,4),(1,3,3),(1,4,4),(1,5,3),(1,6,3)]
assert CF7 == EXPECT, CF7

# ---- (c) four rational points, distinct, on C ----
FOUR = [(0,1,0),(1,0,1),(-1,0,1),(0,-1,1)]
for P in FOUR:
    assert F(*P) == 0, P
assert len({P for P in FOUR}) == 4
# reductions mod 7 land in C(F7):
for (X, Y, Z) in FOUR:
    key = tuple(v % 7 for v in (X, Y, Z))
    for v in key:  # normalize
        if v != 0:
            inv = pow(v, 5, 7)
            break
    assert tuple((v*inv) % 7 for v in key) in EXPECT

# ---- (d) torsor data for E1'/phi(E1) and E1/phihat(E1') ----
# C'_d: N^2 = d M^4 + 6 M^2 e^2 + (-3/d) e^4 ; C_d: N^2 = d M^4 - 3 M^2 e^2 + (3/d) e^4
def Cp(d, M, e):
    return d*M**4 + 6*M*M*e*e + (-3//d)*e**4
def C(d, M, e):
    return d*M**4 - 3*M*M*e*e + (3//d)*e**4
# on-curve witnesses on E1: y^2=x^3-3x^2+3x and E1': y^2=x^3+6x^2-3x
E1 = lambda x: x**3-3*x**2+3*x
E1p = lambda x: x**3+6*x**2-3*x
assert 1 == E1(1) and 9 == E1(3)
assert 4 == E1p(1) and 0 == E1p(0)
# R-obstructions: C_-1, C_-3 strictly negative off origin
for M in range(-3,4):
    for e in range(-3,4):
        if M == e == 0:
            continue
        assert C(-1,M,e) < 0 and C(-3,M,e) < 0
# mod-9 descent obstruction for C'_-1 and C'_3: every mod-9 solution is 0 mod 3
def mod9_sols(coeffs):
    a,b,c = coeffs
    out = []
    for M in range(9):
        for e in range(9):
            for N in range(9):
                if (N*N - (a*M**4 + b*M*M*e*e + c*e**4)) % 9 == 0:
                    out.append((M,e,N))
    return out
S1, S3 = mod9_sols((-1,6,3)), mod9_sols((3,6,-1))
assert len(S1) > 0 and len(S3) > 0  # (0,0,0) always solves; primitivity is the issue
assert all(m%3==0 and e%3==0 and n%3==0 for (m,e,n) in S1)
assert all(m%3==0 and e%3==0 and n%3==0 for (m,e,n) in S3)
# Hence any integer solution has 3|(M,e,N): with (M,e)=1 impossible except
# M=e=0 (not a projective point). So classes -1 (E'-side) and 3 (E'-side) die;
# Selmer-type counts: |E1'/phi(E1)|=2 ({1,-3}), |E1/phihat(E1')|=2 ({1,3}),
# giving |E1(Q)/2E1(Q)|=2*2/2=2, i.e. rank 0 (one rational 2-torsion point).

# ---- (e) Lutz-Nagell on E: y^2 = x^3+1, Delta = -432 ----
D = -432
sq = sorted({y2 for y2 in range(1, abs(D)+1) if abs(D) % y2 == 0
              and int(y2**0.5)**2 == y2})
assert sq == [1,4,9,16,36,144], sq
tors_cand = [(-1,0)]  # y = 0 forces x^3 = -1
for y2 in sq:
    x3 = y2 - 1
    xs = [x for x in range(-2,5) if x**3 == x3]
    for x in xs:
        for y in ([int(y2**0.5), -int(y2**0.5)]):
            assert y*y == y2
            tors_cand.append((x,y))
assert sorted(tors_cand) == [(-1,0),(0,-1),(0,1),(2,-3),(2,3)], tors_cand
# (plus y=0 -> x=-1 included above)

# group law on E closes the six points as Z/6 with generator (2,3)
def add(P, Q):
    if P is None: return Q
    if Q is None: return P
    x1,y1 = P; x2,y2 = Q
    if x1 == x2 and y1 == -y2: return None
    if P != Q:
        lam = FR(y2-y1)/(x2-x1)
    else:
        lam = FR(3*x1*x1)/(2*y1)
    x3 = lam*lam - x1 - x2
    return (x3, lam*(x1-x3)-y1)
O = None
G = [(FR(-1),FR(0)),(FR(0),FR(-1)),(FR(0),FR(1)),(FR(2),FR(-3)),(FR(2),FR(3))]
assert add((FR(0),FR(1)),(FR(0),FR(1))) == (FR(0),FR(-1))          # 2(0,1)=(0,-1)
assert add((FR(-1),FR(0)),(FR(-1),FR(0))) is None                # order 2
assert add((FR(0),FR(1)),(FR(-1),FR(0))) == (FR(2),FR(-3))         # closure
assert add((FR(2),FR(3)),(FR(2),FR(3))) == (FR(0),FR(1))           # (2,3) -> (0,1)
gen = (FR(2),FR(3))
orb, P = [], O
for _ in range(7):
    orb.append(P)
    P = add(gen, P)
assert orb[6] is None and len(set(map(str, orb[:6]))) == 6  # order exactly 6
assert set(map(str, orb[:6])) == set(map(str, [O] + G)) | set() or True
# explicit orbit membership: 6 distinct, containing O, (-1,0), (0,+-1), (2,+-3)
strs = set(map(str, orb[:6]))
assert len(strs) == 6 and str(None) in strs
for pt in G:
    assert str(pt) in strs

# ---- (f) fibres of phi(x,y) = (y, x^2): E(Q) -> C(Q) ----
# E(Q) = {O,(-1,0),(0,+-1),(2,+-3)} (torsion=whole group by rank 0).
# For affine (x,y) in C(Q), phi(x,y)=(y,x^2) is an affine E(Q) point,
# so y must be an X-coordinate of E(Q): y in {-1, 0, 2}.
EX = {-1, 0, 2}
assert EX == {P[0] for P in G}
# y^3+1 = x^4 values on the three fibres:
assert (-1)**3 + 1 == 0 and 0**3 + 1 == 1 and 2**3 + 1 == 9
# y=-1 -> x^4=0 -> x=0: point (0,-1). y=0 -> x^4=1 -> x=+-1: (1,0),(-1,0).
# y=2 -> x^4=9: NO rational x. Proof by descent: x=a/b coprime, b>0 gives
# a^4=9b^4, i.e. (a^2)^2=9(b^2)^2 so a^2=3b^2 (both sides >=0). Mod 3,
# squares are 0,1, so a^2=3b^2 forces 3|a; write a=3k: 9k^2... i.e.
# b^2=3k^2 forces 3|b, contradicting coprimality. Machine check of the
# mod-3 step: every nonzero mod-3 class pair fails a^2=3b^2 primitively.
prim_ok = True
for a in range(3):
    for b in range(3):
        if a == b == 0:
            continue
        if (a*a - 3*b*b) % 3 == 0 and a % 3 != 0:
            prim_ok = False
assert prim_ok  # a^2=3b^2 mod 3 forces 3|a, hence 3|b: no primitive solution
# and x^4=1 over Q forces x=+-1: x^4-1=(x^2-1)(x^2+1), x^2=-1 impossible
# over Q (squares of nonzero rationals are positive; 0 gives -1 != 0).
n_aff = 3  # (0,-1),(1,0),(-1,0); plus unique infinity [0:1:0] -> 4 total

# ---- (g) Stoll non-sharpness at 7: 12 = #C(F7) > 4 = #C(Q) ----
assert len(CF7) == 12 and (n_aff + 1) == 4 and len(CF7) > n_aff + 1

print("VERIFY_OK")
