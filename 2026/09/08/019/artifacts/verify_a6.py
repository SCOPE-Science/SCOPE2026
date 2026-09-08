"""Stdlib-only verifier for the A6 structural identification (no project imports).

Reads output/artifacts/a6_identification.json and checks:
  (A1) a0,b0 are even permutations of {0..5} (hence lie in A6);
  (A2) the four defining relators of G(3,4,5;2) hold: a^3=b^4=(ab)^5=[a,b]^2=1,
       with |a|=3, |b|=4, |ab|=5, |[a,b]|=2;
  (A3) <a0,b0> has order 360 by BFS = 6!/2 = |A6|, hence equals A6
       (universal property then gives a surjection G -> A6, i.e. |G| >= 360);
  (A4) element-order distribution of A6 matches the certified structure file.
Combined with the Todd-Coxeter upper bound |G| <= 360 (verify_G345k2.py),
this gives |G| = 360 and G ~= A6.
"""
import json
from math import gcd

import os
ART = os.path.join(os.path.dirname(os.path.abspath(__file__)))
ident = json.load(open(f"{ART}/a6_identification.json"))
a, b = ident["a_one_line"], ident["b_one_line"]
n = 6
assert sorted(a) == list(range(n)) and sorted(b) == list(range(n)), "A1 fail: not perms"


def parity(p):
    vis = [False] * len(p)
    par = 0
    for i in range(len(p)):
        if not vis[i]:
            c, ln = i, 0
            while not vis[c]:
                vis[c] = True
                c = p[c]
                ln += 1
            par += ln - 1
    return par % 2


assert parity(a) == 0 and parity(b) == 0, "A1 fail: not even"
print("A1 even permutations of {0..5} (lie in A6): PASS")


def comp(p, q):
    return [p[q[i]] for i in range(len(p))]


def pinv(p):
    q = [0] * len(p)
    for i, v in enumerate(p):
        q[v] = i
    return q


def pw(p, e):
    r = list(range(len(p)))
    for _ in range(e):
        r = comp(p, r)
    return r


def order(p):
    vis = [False] * len(p)
    L = 1
    for i in range(len(p)):
        if not vis[i]:
            c, k = i, 0
            while not vis[c]:
                vis[c] = True
                c = p[c]
                k += 1
            L = L * k // gcd(L, k)
    return L


I = list(range(n))
ai, bi = pinv(a), pinv(b)
ab = comp(a, b)
comm = comp(comp(a, b), comp(ai, bi))
assert pw(a, 3) == I, "A2 fail: a^3"
assert pw(b, 4) == I, "A2 fail: b^4"
assert pw(ab, 5) == I, "A2 fail: (ab)^5"
assert comp(comm, comm) == I, "A2 fail: [a,b]^2"
oa, ob, oab, oc = order(a), order(b), order(ab), order(comm)
assert (oa, ob, oab, oc) == (3, 4, 5, 2), (oa, ob, oab, oc)
print(f"A2 relators hold; |a|={oa},|b|={ob},|ab|={oab},|[a,b]|={oc}: PASS")

seen = {tuple(I)}
stack = [tuple(I)]
at, ait, bt, bit = tuple(a), tuple(ai), tuple(b), tuple(bi)
while stack:
    cur = stack.pop()
    for g in (at, ait, bt, bit):
        nxt = tuple(g[cur[i]] for i in range(n))
        if nxt not in seen:
            seen.add(nxt)
            stack.append(nxt)
assert len(seen) == 360 == 720 // 2, len(seen)
assert all(parity(list(g)) == 0 for g in seen), "A3 fail: subgroup not in A6"
print(f"A3 <a0,b0> has order {len(seen)} = 6!/2 = |A6|, so <a0,b0> = A6: PASS")

from collections import Counter
dist = dict(sorted(Counter(order(list(g)) for g in seen).items()))
st = json.load(open(f"{ART}/structure_G345k2.json"))
cert_dist = {int(k): v for k, v in st["element_orders"].items()}
assert dist == cert_dist, (dist, cert_dist)
print(f"A4 A6 element-order distribution {dist} matches certificate: PASS")
print("ALL A6 IDENTIFICATION CHECKS PASSED")
print("Lower bound: surjection G -> A6 gives |G| >= 360; "
      "TC table gives |G| <= 360; hence |G| = 360 and G ~= A6.")
