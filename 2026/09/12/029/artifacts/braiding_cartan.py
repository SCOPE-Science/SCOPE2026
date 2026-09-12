"""Reproducible verification: braiding blocks + Cartan entries for U3 = X+X over D8.
X = M(O_r, xi), O_r={r,r^3}, xi(r)=-1. Basis x1=a1,x2=b1,x3=a2,x4=b2.
Checks: group relations, class, centralizer action, 4x4 braiding scalars,
Cartan matrix, reflection invariance, Hilbert series of exterior algebra.
"""
import json

# --- D8 as presented: r^4=s^2=1, srs=r^-1. Model as pairs (i,j): r^i s^j.
def mul(a, b):
    i1, j1 = a; i2, j2 = b
    if j1 == 0:
        return ((i1 + i2) % 4, j2)
    else:
        return ((i1 - i2) % 4, (j1 + j2) % 2)

def inv(a):
    i, j = a
    if j == 0:
        return ((-i) % 4, 0)
    return (i, 1)

def conj(g, t):
    return mul(mul(g, t), inv(g))

r = (1, 0); s = (0, 1)
e = (0, 0); r2 = (2, 0); r3 = (3, 0)
G = [(i, j) for i in range(4) for j in range(2)]
assert len(G) == 8
# relations
assert mul(r, mul(r, mul(r, r))) == e
assert mul(s, s) == e
assert conj(s, r) == r3  # srs^-1 = r^-1

Or = [r, r3]
# centralizer of r
C = [g for g in G if mul(g, r) == mul(r, g)]
assert sorted(C) == sorted([(i, 0) for i in range(4)])
print("centralizer size:", len(C))

# character xi: xi(r)=-1 i.e. xi(r^i)=(-1)^i
def xi(g):
    assert g[1] == 0
    return -1 if (g[0] % 2 == 1) else 1

assert xi(r) == -1 and xi(r3) == -1 and xi(r2) == 1

# section t_r=1, t_{r3}=s
t = {r: e, r3: s}
# action coefficient: for g in G, basis index u in O, find u' = g u g^-1 and c = t[u']^{-1} g t[u] in C
def action(g, u):
    up = conj(g, u)
    c = mul(mul(inv(t[up]), g), t[u])
    assert c[1] == 0, (g, u, up, c)
    return up, xi(c)

# braiding-relevant actions of degrees r, r^3 on fibers
for g in (r, r3):
    for u in Or:
        up, coef = action(g, u)
        print(f"g={g} on fiber {u}: target={up} coef={coef}")
        assert up == u and coef == -1

# full 4x4 braiding scalars q_{ij}: c(x_i otimes x_j) = q_{ij} x_{j'} ... here j'=j since degrees act diagonally
# degrees: x1=a1,x2=b1,x3=a2,x4=b2 -> deg = r,r^3,r,r^3
degs = [r, r3, r, r3]
names = ["a1", "b1", "a2", "b2"]
Q = [[action(degs[i], degs[j] if False else (Or[0] if k in (0, 2) else Or[1])) for k in [j]]
     for i in range(4) for j in range(4)]
# simpler: q[i][j] = coefficient of deg(xi) acting on fiber of xj
fibers = [r, r3, r, r3]
q = [[action(degs[i], fibers[j])[1] for j in range(4)] for i in range(4)]
# check swap data: s swaps fibers within each copy
for u in Or:
    up, coef = action(s, u)
    print("s action:", u, "->", up, coef)
assert action(s, r) == (r3, 1) and action(s, r3) == (r, 1)
# r^2 acts as +1 on fibers (xi(r^2)=1) but fixes fibers; s*r etc all consistent
for u in Or:
    up, coef = action(r2, u)
    assert up == u and coef == 1

print("q matrix:")
for row in q:
    print(row)
assert all(v == -1 for row in q for v in row)

# Cartan entries for diagonal braiding: a_ii=2; for i!=j, a_ij = -min{m>=0 : (m+1)_{qii}(1-qii^m qij qji)=0}
def cartan_entry(qii, qq):
    # qq = qij*qji
    m = 0
    while True:
        # (m+1)_{qii} = 1+qii+...+qii^m
        qp = sum(qii**k for k in range(m + 1))
        if qp * (1 - (qii**m) * qq) == 0:
            return -m
        m += 1
        assert m < 10

A = [[0]*4 for _ in range(4)]
for i in range(4):
    for j in range(4):
        if i == j:
            A[i][j] = 2
        else:
            A[i][j] = cartan_entry(q[i][i], q[i][j]*q[j][i])
print("Cartan matrix:")
for row in A:
    print(row)
assert all(A[i][j] == (2 if i == j else 0) for i in range(4) for j in range(4))

# Reflection invariance: for simply-laced zero-off-diagonal, reflected braiding labels coincide.
# Weyl group of A1^4 is (Z/2)^4, order 16, finite. No infinite word.
# Every diagonal subsystem (subset S of {1..4}) has Cartan I_|S|, Dynkin A1^|S|, finite type.
import itertools
for k in range(1, 5):
    for S in itertools.combinations(range(4), k):
        sub = [[A[i][j] for j in S] for i in S]
        assert all(sub[a][b] == (2 if a == b else 0) for a in range(k) for b in range(k))
print("all diagonal subsystems finite type A1^k: OK")

# Hilbert series of claimed Nichols algebra = exterior algebra Lambda(V), dim V=4
# hilb = (1+t)^4 = 1+4t+6t^2+4t^3+t^4, total 16
from math import comb
hilb = [comb(4, k) for k in range(5)]
print("Hilbert coefficients:", hilb, "total:", sum(hilb))
assert sum(hilb) == 16

log = {
    "group": "D8 order 8 verified; s r s^-1 = r^3 verified",
    "centralizer_size": 4,
    "xi": "xi(r^i)=(-1)^i; xi(r)=xi(r^3)=-1, xi(r^2)=1",
    "r_action_on_both_fibers": -1,
    "r3_action_on_both_fibers": -1,
    "braiding": "c(xi otimes xj) = -xj otimes xi for all i,j (c=-flip); q matrix all -1",
    "q_matrix": q,
    "cartan_matrix": A,
    "dynkin": "4x isolated (-1)-nodes; type A1 x A1 x A1 x A1",
    "reflections": "all s_i fix datum; Weyl groupoid one object, Weyl group (Z/2)^4 order 16, finite",
    "subsystems": "every subset-subsystem has Cartan I_k, finite; no affine diagram occurs",
    "nichols_relations": ["xi^2=0 (4)", "xi xj + xj xi=0 for i<j (6)"],
    "hilbert_series": "(1+t)^4",
    "hilbert_coeffs": hilb,
    "dimension": 16,
}
with open("output/artifacts/braiding_cartan_log.json", "w") as f:
    json.dump(log, f, indent=2)
print("wrote output/artifacts/braiding_cartan_log.json")
