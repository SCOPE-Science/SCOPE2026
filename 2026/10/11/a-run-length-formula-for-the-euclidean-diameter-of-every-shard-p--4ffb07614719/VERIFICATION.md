---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-15.md",
      "INDEPENDENT_AUDIT_2026-10-15.json"
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

For an arc word U^{p_1}D^{q_1}...U^{p_f}D^{q_f} with nonempty alternating matchings allowed and fixed coordinate signs, the characteristic-vector support symmetric difference equals squared Euclidean distance of two shard vertices. Tracking the number of open matchings (0,1,2) gives exact singleton/spare-run max-plus matrices; distinct positions in a run of length>=2 allow 0->2 or 2->0 reward 2, whereas singleton simultaneous selection contributes zero difference. The state invariant A_i=2i+2g_i, B_i=A_i+2h_i-1, C_i=A_i+2h_i-2 after completed runs yields max closed-state score 2(f+g). Independently recomputed max-plus products for every singleton/spare pattern through f=8, agreeing with greedy g; the pinned exhaustive enumerator over all UD arc words length 2..10 was also inspected. The independent zero-vertex argument gives squared eccentricity 2f and exactly product_i p_i q_i farthest vertices. Finite checks corroborate, do not replace the all-f induction.

## originality

PASS

Best-of-knowledge PASS. Padrol--Pilaud--Ritter define shard polytopes and their alternating-matching vertex model, but their inspected primary paper handles face/normal-fan/matroid geometry rather than the ambient Euclidean metric invariant. The exact diameter formula, greedy spare-run statistic, and farthest-zero-vertex count do not follow numerically from the vertex-description statement without a nontrivial two-matching optimization. Published Resultary neighbors concern enclosing spheres, different polytope metrics, or graph distances rather than this exact diameter; no materially stronger published covering theorem was found. Metric-translation literature remains a residual risk.

## value

PASS

PASS. A closed linear-time run-statistic formula for the ordinary Euclidean diameter of every natural type-A shard polytope is an exact, reusable metric invariant. The 1-vs-2 threshold, extremal equalities and farthest-vertex enumeration give structural information, not an unmotivated small enumeration.

The dated certificate retains the supplied scientific assessment, sources and limitations.
