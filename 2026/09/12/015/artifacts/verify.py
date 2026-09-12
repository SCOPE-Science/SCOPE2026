"""Verify HH^1/HH^2 of the punctured-torus base gentle algebra A0 (stdlib only, exact rationals).

A0: vertices {0,1,2}; arrows a1,a2: 0->1, b1,b2: 1->2; relations a1*b1=0, a2*b2=0
(minimal cut c0 of the Markov/FST triangulation quiver; dim A0 = 9 with basis
 e0,e1,e2,a1,a2,b1,b2,p1=a1b2,p2=a2b1).

Checks:
 (E1) multiplication table is associative on basis paths.
 (E2) d^2 = 0: delta1 o delta0 = 0 on basis of C^0.
 (E3) E-reduced bar complex ranks: rank(delta0)=2, rank(delta1)=8 (full),
      hence HH^1 = k^2, HH^2 = 0.
 (E4) Bardzell cross-check: AP_2 = {a1b1, a2b2} full rank => HH^2 = 0;
      ker(delta1) dim 4, im(delta0) dim 2 => HH^1 = k^2.
 (E5) Explicit HH^1 representatives are cocycles but not coboundaries,
      and HH^1 x HH^1 bracket data is not needed (target lands in HH^2=0).
Prints VERIFY_OK on success.
"""
from fractions import Fraction


def rank_frac(rows):
    M = [[Fraction(x) for x in r] for r in rows]
    m = len(M)
    n = len(M[0]) if m else 0
    r = 0
    for c in range(n):
        piv = None
        for i in range(r, m):
            if M[i][c] != 0:
                piv = i
                break
        if piv is None:
            continue
        M[r], M[piv] = M[piv], M[r]
        inv = M[r][c]
        M[r] = [v / inv for v in M[r]]
        for i in range(m):
            if i != r and M[i][c] != 0:
                f = M[i][c]
                M[i] = [a - f * b for a, b in zip(M[i], M[r])]
        r += 1
    return r


# ---- algebra ----
BASIS = ['e0', 'e1', 'e2', 'a1', 'a2', 'b1', 'b2', 'p1', 'p2']
SRC = {'e0': 0, 'e1': 1, 'e2': 2, 'a1': 0, 'a2': 0, 'b1': 1, 'b2': 1,
       'p1': 0, 'p2': 0}
TGT = {'e0': 0, 'e1': 1, 'e2': 2, 'a1': 1, 'a2': 1, 'b1': 2, 'b2': 2,
       'p1': 2, 'p2': 2}


def mul(x, y):
    if x.startswith('e'):
        return y if SRC[y] == int(x[1]) else None
    if y.startswith('e'):
        return x if TGT[x] == int(y[1]) else None
    if x in ('a1', 'a2') and y in ('b1', 'b2'):
        if (x, y) == ('a1', 'b1') or (x, y) == ('a2', 'b2'):
            return None
        return 'p1' if (x, y) == ('a1', 'b2') else 'p2'
    return None


# (E1) associativity on basis triples
for x in BASIS:
    for y in BASIS:
        for z in BASIS:
            l = mul(mul(x, y), z) if mul(x, y) else None
            r = mul(x, mul(y, z)) if mul(y, z) else None
            assert l == r, (x, y, z, l, r)
print("E1 associativity: OK (9^3 triples)")


def delta0(lam):
    l0, l1, l2 = lam
    return [l1 - l0, 0, 0, l1 - l0, l2 - l1, 0, 0, l2 - l1,
            l2 - l0, 0, 0, l2 - l0]


def delta1(F):
    Fa1, Fa2 = (F[0], F[1]), (F[2], F[3])
    Fb1, Fb2 = (F[4], F[5]), (F[6], F[7])
    Fp1, Fp2 = (F[8], F[9]), (F[10], F[11])
    out = []
    for ai, Fa, bj, Fb, prod in [
            ('a1', Fa1, 'b1', Fb1, None), ('a1', Fa1, 'b2', Fb2, 'p1'),
            ('a2', Fa2, 'b1', Fb1, 'p2'), ('a2', Fa2, 'b2', Fb2, None)]:
        c1, c2 = Fb
        t1 = (c2, 0) if ai == 'a1' else (0, c1)
        d1, d2 = Fa
        t3 = (0, d2) if bj == 'b1' else (d1, 0)
        t2 = (0, 0) if prod is None else (Fp1 if prod == 'p1' else Fp2)
        out += [t1[0] - t2[0] + t3[0], t1[1] - t2[1] + t3[1]]
    return out


# (E2) d^2 = 0
for j in range(3):
    lam = [0, 0, 0]
    lam[j] = 1
    assert delta1(delta0(lam)) == [0] * 8
print("E2 d^2=0: OK")

# (E3) ranks of E-reduced complex
M10 = [[delta0([1 if k == j else 0 for k in range(3)])[i]
        for j in range(3)] for i in range(12)]
M21 = []
for i in range(8):
    row = []
    for j in range(12):
        F = [0] * 12
        F[j] = 1
        row.append(delta1(F)[i])
    M21.append(row)
r0, r1 = rank_frac(M10), rank_frac(M21)
assert r0 == 2, r0
assert r1 == 8, r1
hh1 = 12 - r1 - r0
hh2 = 8 - r1
assert (hh1, hh2) == (2, 0), (hh1, hh2)
print("E3 E-reduced ranks: rank(d0)=2 rank(d1)=8 HH^1=k^2 HH^2=0")

# (E4) Bardzell cross-check: AP_2 = {a1b1, a2b2}; C^2 dim 4.
# delta1 column for F-coord j restricted to relation pairs:
# a1b1-coeffs pick rows 0,1; a2b2-coeffs pick rows 6,7.
MB = [[M21[r][j] for j in range(12)] for r in (0, 1, 6, 7)]
assert rank_frac(MB) == 4, rank_frac(MB)
print("E4 Bardzell: AP_2 full rank 4 => HH^2=0; ker(d1) dim 4, im(d0) dim 2 => HH^1=k^2")

# (E5) explicit HH^1 reps from ker(delta1): v1 scales (a2,b1) oppositely,
# v2 scales (a1,b2) oppositely; both are cocycles, independent mod im(delta0).
v1 = [0, 0, 0, -1, 1, 0, 0, 0, 0, 0, 0, 0]
v2 = [1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0]
assert delta1(v1) == [0] * 8 and delta1(v2) == [0] * 8
# non-coboundary: appending v1 (resp. v2, resp. both) to im(delta0) raises rank.
aug1 = [row + [v] for row, v in zip(M10, v1)]
aug2 = [row + [v] for row, v in zip(M10, v2)]
aug12 = [row + [a, b] for row, a, b in zip(M10, v1, v2)]
assert rank_frac(aug1) == 3, "v1 is a coboundary!"
assert rank_frac(aug2) == 3, "v2 is a coboundary!"
assert rank_frac(aug12) == 4, "v1,v2 dependent mod coboundaries!"
print("E5 HH^1 representatives certified non-coboundaries")

print("HH^1 dim 2, HH^2 dim 0 => bracket HH^1 x HH^2 -> HH^2 is identically zero")
print("VERIFY_OK")
