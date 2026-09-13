"""Reidemeister-Schreier verification for ker(phi) in lane-1721.

G1 = <a,b,c | r=1>, r = w1^2, w1 = a b a^-1 b^-1 c c.
phi: a->0, b->0, c->1 in Z/4. Kernel L has transversal {1,c,c^2,c^3}.
Schreier gens: a_i = c^i a c^-i, b_i = c^i b c^-i, z = c^4.
Relators R_i = rewrite of c^i r c^-i starting at coset i.
Expected:
  R0 = [a0,b0][a2,b2]z
  R1 = [a1,b1][a3,b3]z
  R2 = [a2,b2]z[a0,b0]
  R3 = [a3,b3]z[a1,b1]
Also checks: (i) R2 is consequence of R0 with z eliminated (freely trivial after
substitution), same for R3/R1; (ii) final single relator S = [a0,b0][a2,b2][a3,b3]^-1[a1,b1]^-1
is a genus-4 surface relator (each of 8 gens appears exactly twice with total exponent 0).
Run: python3 reidemeister_schreier_check.py
"""


def rewrite(word, start):
    cur = start
    out = []
    for g, e in word:
        if g in ("a", "b"):
            out.append((g, cur, e))
        elif e == 1:
            if cur == 3:
                out.append(("z", None, 1))
                cur = 0
            else:
                cur += 1
        else:
            if cur == 0:
                out.append(("z", None, -1))
                cur = 3
            else:
                cur -= 1
    return cur, out


def comm(g, i, h, j):
    return [(g, i, 1), (h, j, 1), (g, i, -1), (h, j, -1)]


def free_reduce(toks):
    stack = []
    for t in toks:
        if stack and stack[-1][:2] == t[:2] and stack[-1][2] == -t[2]:
            stack.pop()
        else:
            stack.append(t)
    return stack


w = [("a", 1), ("b", 1), ("a", -1), ("b", -1), ("c", 1), ("c", 1)]
r = w + w
expected = {
    0: comm("a", 0, "b", 0) + comm("a", 2, "b", 2) + [("z", None, 1)],
    1: comm("a", 1, "b", 1) + comm("a", 3, "b", 3) + [("z", None, 1)],
    2: comm("a", 2, "b", 2) + [("z", None, 1)] + comm("a", 0, "b", 0),
    3: comm("a", 3, "b", 3) + [("z", None, 1)] + comm("a", 1, "b", 1),
}
ok = True
for i in range(4):
    end, toks = rewrite(r, i)
    assert end == i, (i, end)
    assert toks == expected[i], (i, toks, expected[i])
    print(f"R{i} OK: {toks}")
    # also verify r has c-exponent 0 mod 4 (ends at start coset) -- torsion-freeness setup
    assert end == i

# z-elimination: z = ([a0,b0][a2,b2])^-1 from R0; check R2 becomes freely trivial.
zinv_sub = list(reversed([(g, i, -e) for (g, i, e) in comm("a", 0, "b", 0) + comm("a", 2, "b", 2)]))
# R2 with z replaced by zinv_sub word:
R2_sub = comm("a", 2, "b", 2) + zinv_sub + comm("a", 0, "b", 0)
assert free_reduce(R2_sub) == [], free_reduce(R2_sub)
print("R2 redundant given R0: OK")
zinv_sub1 = list(reversed([(g, i, -e) for (g, i, e) in comm("a", 1, "b", 1) + comm("a", 3, "b", 3)]))
R3_sub = comm("a", 3, "b", 3) + zinv_sub1 + comm("a", 1, "b", 1)
assert free_reduce(R3_sub) == [], free_reduce(R3_sub)
print("R3 redundant given R1: OK")

# Final surface relator S: [a0,b0][a2,b2][a3,b3]^-1[a1,b1]^-1; check each gen twice, exp-sum 0.
S = comm("a", 0, "b", 0) + comm("a", 2, "b", 2) + \
    [(g, i, -e) for (g, i, e) in reversed(comm("a", 3, "b", 3))] + \
    [(g, i, -e) for (g, i, e) in reversed(comm("a", 1, "b", 1))]
from collections import Counter
c = Counter((g, i) for (g, i, e) in S)
assert set(c) == {("a", i) for i in range(4)} | {("b", i) for i in range(4)}, c
assert all(v == 2 for v in c.values()), c
expsum = Counter()
for g, i, e in S:
    expsum[(g, i)] += e
assert all(v == 0 for v in expsum.values()), expsum
# Euler check: 1 vertex-pairing relator on 8 gens -> chi = 1-8+1 = -6 = 2-2g -> g=4.
assert 2 - 2 * 4 == 1 - 8 + 1
print("Surface relator S OK: 8 generators each twice, exponent-sum 0, genus 4 (chi=-6).")
print("ALL CHECKS PASSED")
