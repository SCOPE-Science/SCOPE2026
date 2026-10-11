---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-05.md",
      "INDEPENDENT_AUDIT_2026-10-05.json"
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

The primary source independently proves the lower bound: no n-chain from L reaches B_n, even with merely nonempty intersections. For the upper bound, a positive legal cylinder beginning ab lies in L and in a^2L because applying a^{-2} changes its initial pair to a^{-1}b, also a positive transition in the source matrix. The nonsingularized action preserves positivity under translation, so every consecutive pair a^{2j}L and a^{2j+2}L has positive overlap. Finally a positive legal cylinder beginning b, translated by a^{2n+2}, lies in both a^{2n+2}L and B_n. Thus an (n+1)-chain exists and the lower bound is sharp.

## originality

PASS

The primary source proves the sharp lower obstruction needed here: for B_n=[a^{2n+2}], L does not n-chain to B_n, even if positive-measure overlaps are weakened to nonempty overlaps. It does not state that an (n+1)-chain exists or identify the minimizing translate path. The audited result adds that complementary construction and therefore computes the exact depth of the source's canonical witnesses. Resultary returned the assigned finding as the exact match and no independent prior exact-depth statement.

## value

PASS

The B_n are the source's canonical witnesses for failure of bounded chaining, so their exact minimal depth is a natural quantitative invariant of the counterexample. Showing linear sharpness distinguishes mere unboundedness from the precise rate at which the obstruction grows.

The dated certificate retains the supplied scientific assessment, sources and limitations.
