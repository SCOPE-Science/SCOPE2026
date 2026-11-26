---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

At least one complementary vertex is necessary, and their indices form a clique in the original cycle, hence there are at most two. One b_j forces a_{j−1},a_{j+1} and leaves a path of length n−5 in vertices; two consecutive b's leave n−2 path vertices and no complementary domination constraint. The type-one set has 3+ceil((n−5)/3) vertices (the 2+ in the first expression of the frozen counting paragraph is a typo); type two has 2+ceil((n−2)/3), equal to the former and to floor(n/3)+2. For a nonempty path with s=ceil(m/3), the two endpoint slack bits and s−1 gap-shortening bits have total 3s−m; counting them, with the empty path separately, gives precisely the claimed counts. For path slides, shift the ordered positions by 2(i−1): successive differences are 0 or 1. Coordinatewise minimum preserves the constraints, and lowering the first coordinate in the last constant block that differs from the target preserves the constraints. In particular, a next block at height one larger cannot obstruct this move: it would also have to differ from the target by the target's own gap bound. The displayed inter-fibre moves are valid for both mobile residues, including n=6,7: the type-one forced end vertex is in I_j, and the first and last path gaps fit in both consecutive type-two fibres. For n=3k+2 each fibre is a singleton. The unique length-2 or length-5 cyclic gap of the original-layer selection identifies its same-type fibre (one original-layer vertex suffices at n=5 in type two). Adding a second b can only add b_{j±1} and remove its matched a, but the other forced a is not in the target type-two pattern. So no one-for-one exchanges exist there. More generally a vertex removed from an independent dominating set has no neighbor in the retained set, so the inserted vertex must be adjacent to it: jumping and sliding give the same graph here. A separate increasing-cardinality search with pairwise exchange tests regenerated and matched both frozen TSVs byte-for-byte for n=5..12 (python3 /workspace/branches/reproduce_reviews.py 2). The supplied structural code for n=13..21 was inspected, not executed; no numerical check substitutes for the unbounded proof.

## originality

PASS

The supported contribution is principally the complete minimum-set exchange transition on complementary cycle prisms, with explicit inter-fibre moves and a freezing proof. Do not claim the exchange definition or equivalence of jumps and slides, and do not assign priority to the count independently of the unavailable earlier maximal-independent-set paper.

## value

PASS

A natural infinite family has opposite exchange behaviors at adjacent sizes: one connected graph of every optimum, or no valid single-token exchange at all. The proof explains the mod-three switch by path slack and explicit between-fibre moves, not by a finite census. The classification and state counts also make the transition usable for enumerating or navigating the optima.

The dated certificate retains the supplied scientific assessment, sources and limitations.
