---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

Reconstructed the matching-to-function bijection and the full sharp bound. Two unmatched original vertices would leave their shared subdivision vertex available. With only i unmatched, each edge from j to e_ij is forced; these matchings for different i are edge-disjoint, so their symmetric difference is 2(n−1)>2 (the weaker wording in RESULT.md line 29 is insufficient on its own). In the full tier, a jump changes exactly one coordinate and the legal choices at i are n−2−indeg(i), summing to n(n−3). If no wrong coordinate can be directly set, g permutes the wrong set in cycles of length at least three and the current map is g inverse there. On any such cycle some j has indegree at most n−3 since 3(n−2)>n; a legal temporary target cannot equal the blocked g(j) or the old target, the latter being j's predecessor. Thus the predecessor edit is legal after this temporary move, and each subsequent backward edit targets a vertex already corrected and cannot create a target 2-cycle. Each disjoint repaired cycle adds only one move beyond Hamming distance. In the inverse-cycle witness, no edit outside a cycle removes its initial obstruction, so each of floor(n/3) cycles forces one move besides the n last edits. For n=3 there are exactly two full-tier maps, both with degree zero. VERIFY.py independently constructs small incidence graphs, then uses BFS at n=4,5 and one source at n=6; these are finite diagnostics and the proof, not those runs, establishes the universal claims. The frozen checker was inspected, not executed.

## originality

PASS

Pass applies to the exact diameter and matching-tier structure, not the known count or the token-jump model. The closest general matching results and related catalogue metrics do not state or supply the needed uniform one-detour cycle bound and sharp witness for this subdivision family.

## value

PASS

The family is the canonical incidence subdivision of a clique and the invariant measures worst-case reconfiguration cost, not just existence. The exact additive detour term, where inverse directed cycles require a temporary edit even when every coordinate must already move, identifies a structural obstruction that neither counting nor a connectivity test describes. The isolated smaller tier explains the separation between inclusion-maximal and maximum matchings under the prescribed jump.

The dated certificate retains the supplied scientific assessment, sources and limitations.
