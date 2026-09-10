"""Baskakov cup vanishing among H^5 generators + triple-definability data (target deepening).

Certifies, over Q, for the four H^5 summand supports S={123,456,147,789}:
 (1) every disjoint pair has acyclic union => cup is zero;
 (2) every overlapping pair has cup zero by the Baskakov disjointness rule
     (product of classes on I,J with I cap J != empty is zero);
 (3) the triple pair-unions K_123456, K_456789 are acyclic (triple cups vanish);
 (4) the triple-defining vanishings \tilde H(K_123456)=\tilde H(K_456789)=0 hold.
Repro: python3 verify_cups_triple.py. Stdlib only (imports shared routines).
"""
import verify_target_obstruction as V
from itertools import combinations

S = {'123': (0, 1, 2), '456': (3, 4, 5), '147': (0, 3, 6), '789': (6, 7, 8)}

print("== pairwise cups ==")
for a, b in combinations(sorted(S), 2):
    I, J = set(S[a]), set(S[b])
    U = tuple(sorted(I | J))
    disj = not (I & J)
    h = V.reduced_betti(U)
    reason = "acyclic-union => 0" if (disj and not h) else (
        "Baskakov overlap => 0" if not disj else f"UNION HOMOLOGY {h} (needs inspection)")
    print(f"{a} x {b}: {'disjoint' if disj else 'overlap '+str(sorted(x+1 for x in I&J))}, "
          f"K_{''.join(str(x+1) for x in U)}={h} => cup 0 ({reason})")
    assert (not h) if disj else True, (a, b, h)

print("== triple data ==")
for name, U1 in [('123456', (0, 1, 2, 3, 4, 5)), ('456789', (3, 4, 5, 6, 7, 8))]:
    h = V.reduced_betti(U1)
    print(f"K_{name} = {h}")
    assert h == {}, (name, h)
print("TRIPLE_CUP_VANISHING_OK")
print("ALL_CUP_CHECKS_PASS")
