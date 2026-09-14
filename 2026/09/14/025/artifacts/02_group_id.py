"""Group identification for the degree-12 triple (replaces buggy 02_primitivity.py).

Cites: (1) vinf^6 is a 7-cycle + Jordan's theorem (primitive group containing a
p-cycle with p <= n-3 contains A_n), giving L >= A12, upgraded to S12 by the
odd generators; (2) independent sympy check: |G| = 12!, transitive, primitive.
The earlier generator-only minimal-block closure script was insufficient in
principle (blocks must be tested against the full group, not just generators)
and is superseded by this file.
"""
import json

N = 12

def compose(a, b):
    return [b[a[i]] for i in range(len(a))]

def sign_of(p):
    seen = [False] * len(p)
    ncyc = 0
    for i in range(len(p)):
        if not seen[i]:
            ncyc += 1
            j = i
            while not seen[j]:
                seen[j] = True
                j = p[j]
    return 1 if ((len(p) - ncyc) % 2 == 0) else -1

d = json.load(open("triple.json"))
v0, v1, vinf = d["v0"], d["v1"], d["vinf"]

# (1) Jordan input: vinf^6 kills the disjoint 3- and 2-cycles, leaving a 7-cycle.
w = list(range(N))
for _ in range(6):
    w = compose(w, vinf)
seen = [False] * N
lens = []
for i in range(N):
    if not seen[i]:
        j = i
        L = 0
        while not seen[j]:
            seen[j] = True
            j = w[j]
            L += 1
        lens.append(L)
lens.sort(reverse=True)
print("vinf^6 cycle structure (sorted lens):", lens)
assert lens == [7, 1, 1, 1, 1, 1]
print("7-cycle present: yes; Jordan applies (p=7 <= n-3=9) once primitivity holds")

print("signs v0,v1,vinf:", sign_of(v0), sign_of(v1), sign_of(vinf))

# (2) Independent check via sympy (order + transitivity + primitivity).
from sympy.combinatorics import Permutation
from sympy.combinatorics.perm_groups import PermutationGroup
G = PermutationGroup(Permutation(v0), Permutation(v1))
order = G.order()
print("order:", order, "transitive:", G.is_transitive(), "primitive:", G.is_primitive())
assert order == 479001600
assert G.is_transitive() and G.is_primitive()
print("CONCLUSION: L = S12 (Jordan gives >= A12; odd element gives S12; "
      "sympy order confirms). Centralizer of S12 in S12 is trivial => Aut = 1.")
