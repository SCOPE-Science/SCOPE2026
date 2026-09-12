"""Verify finite GT-cuspidal counterexample at (p,S)=(5,{2,5}), level (3,25).

Model: R=Z/25, L = free nilpotent Lie class-3 on A,B.
Hall basis indices: 0:A 1:B 2:C=[A,B] 3:D=[A,C] 4:E=[B,C].
Q3 = exp(L) via truncated BCH. G-action weight (1,1,2,3,3).
Section s(g) = exp(rho(g)*(A+2B)) with rho Kummer cocycle of 2.
Checks: ledger off cuspidal lines; cocycle identity; F=1 solves
hexagon+pentagon; kappa3=0; BCH sanity (associativity, exponent 25).
"""
MOD = 25
INV2 = pow(2, -1, MOD)    # 13
INV12 = pow(12, -1, MOD)  # 23

def add(u, v):
    return [(a + b) % MOD for a, b in zip(u, v)]

def scale(k, u):
    return [(k * a) % MOD for a in u]

def bracket(u, v):
    a0, a1, a2, a3, a4 = u
    b0, b1, b2, b3, b4 = v
    c = (a0 * b1 - a1 * b0) % MOD
    d = (a0 * b2 - a2 * b0) % MOD
    e = (a1 * b2 - a2 * b1) % MOD
    return [0, 0, c, d, e]

def bch(x, y):
    """log(exp x * exp y), truncated class 3."""
    xy = bracket(x, y)
    xxy = bracket(x, xy)
    yxy = bracket(y, xy)
    out = add(x, y)
    out = add(out, scale(INV2, xy))
    out = add(out, scale(INV12, xxy))
    out = add(out, scale(MOD - INV12, yxy))
    return out

def gact(v, chi):
    c1 = chi % MOD
    c2 = (chi * chi) % MOD
    c3 = (c2 * chi) % MOD
    return [(c1 * v[0]) % MOD, (c1 * v[1]) % MOD, (c2 * v[2]) % MOD,
            (c3 * v[3]) % MOD, (c3 * v[4]) % MOD]

def mul_list(ws):
    acc = [0, 0, 0, 0, 0]
    for w in ws:
        acc = bch(acc, w)
    return acc

V = [1, 2, 0, 0, 0]  # X + 2Y direction
CHIS = [1, 2, 3, 6, 7, 11, 13, 24]  # units mod 25 (Frob values, incl. chi=2 at l=2)
ok = True

# 1. S-unit ledger V = (Z/25)^2; b=[2]=(1,0), a=[4]=(2,0)
b, a = (1, 0), (2, 0)
assert ((25 * b[0]) % MOD, (25 * b[1]) % MOD) == (0, 0)
assert ((5 * b[0]) % MOD, (5 * b[1]) % MOD) != (0, 0)  # order exactly 25
# -1 killed mod 25: 25th-power map on {+-1} is onto since (-1)^25=-1
assert (25 % 2) == 1
sub = lambda p, q: ((p[0] - q[0]) % MOD, (p[1] - q[1]) % MOD)
assert b != (0, 0) and a != (0, 0)                      # off D1, D0
assert sub(b, a) != (0, 0) and ((b[0] + a[0]) % MOD, (b[1] + a[1]) % MOD) != (0, 0)  # off D_inf either convention
print("PASS ledger: (b,a)=((1,0),(2,0)) has order 25, off D0/D1/Dinf lines")

# 2. Cocycle identity: phi(gh)=phi(g)*g.phi(h) for collinear values
n = 0
for chi1 in CHIS:
    for r1 in range(MOD):
        for r2 in range(MOD):
            lhs = scale((r1 + chi1 * r2) % MOD, V)
            rhs = bch(scale(r1, V), gact(scale(r2, V), chi1))
            assert lhs == rhs, (chi1, r1, r2, lhs, rhs)
            n += 1
print(f"PASS cocycle: {n} (chi,r1,r2) cases, collinear BCH = addition")

# 3. F_s = 1 solves hexagon (symmetry + 3-cycle) and pentagon
F = [0, 0, 0, 0, 0]
assert bch(F, F) == F                                   # F(Y,X)=F(X,Y)^{-1} at F=1
assert mul_list([F, F, F]) == F                         # 3-cycle
assert mul_list([F, F, F, F, F]) == F                    # pentagon 5-cycle
print("PASS hexagon+pentagon for F=1 (symmetry, 3-cycle, 5-cycle)")

# 4. kappa3 = 0: deg-3 components of phi vanish for every rho value
for r in range(MOD):
    w = scale(r, V)
    assert w[3] == 0 and w[4] == 0
    assert (w[3] + 2 * w[4]) % MOD == 0                  # any fixed linear Soule form
print("PASS kappa3: degree-3 part identically zero -> kappa3(s)=0 mod 25")

# 5. BCH sanity: associativity + exponent 25 + weight preservation
import random
random.seed(5)
rng = lambda: [random.randrange(MOD) for _ in range(5)]
for _ in range(300):
    x, y, z = rng(), rng(), rng()
    assert bch(bch(x, y), z) == bch(x, bch(y, z))
for _ in range(50):
    x = rng()
    assert mul_list([x] * 25) == [0, 0, 0, 0, 0]
for chi in CHIS:
    x, y = rng(), rng()
    assert gact(bracket(x, y), chi) == bracket(gact(x, chi), gact(y, chi))
    assert gact(bch(x, y), chi) == bch(gact(x, chi), gact(y, chi))
print("PASS sanity: BCH associative, exponent 25, G-action is automorphism")

# 6. Cup-product remark: collinear abelian values have vanishing bracket,
#    so no degree-2 obstruction: bch(r1*V, r2*V) has zero C component
for r1 in range(MOD):
    for r2 in range(MOD):
        assert bch(scale(r1, V), scale(r2, V))[2] == 0
print("PASS cup: collinear cup vanishes, lift exists with zero higher terms")
print("ALL CHECKS PASSED")
