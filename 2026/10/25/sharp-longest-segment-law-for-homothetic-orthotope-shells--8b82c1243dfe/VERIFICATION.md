---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-26.md",
      "INDEPENDENT_AUDIT_2026-10-26.json"
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

PASS. Verified the planar timing argument: two open coordinate-interior intervals must be disjoint for a hole-avoiding segment, yielding normalized displacements pq≤a(p+q). With r=a/(1−a), the exact weighted inequality αp²+βq²≤max(α+r²β,β+r²α) follows from the strictly convex p² plus [ap/(p−a)]² upper envelope on [r,1]. Interval Helly for d affine coordinate time intervals finds a disjoint pair, and the remaining d−2 displacements ≤1 force L²≤Σs_i²−(1−r²)s_min². Endpoints with full traversals except r-times one shortest side attain the bound; strict convexity/equality in every factor plus hole avoidance fixes all optimizer families under reflections and reversal. This proves all positive side lengths and all integer d≥2, not only tested finite grids.

## originality

PASS

PASS qualified best-of-knowledge, not certified historical priority. Ambrus et al. arXiv:2610.18770 Claim 2.2 contains the d=2 unit-square numeric bound for total line-intersection measure. The current claim differs by arbitrary side lengths, all d≥2, connected fully contained segment, and complete equality classification. The prior planar equal-sided special value is covered; no checked higher-dimensional theorem or Resultary same-shape entry implied the general formula. Residual risk: An older recreational geometry/visibility result under the term maximal free segment may cover the exact arbitrary-side formula.

## value

PASS

PASS. Exact all-dimensional connected-chord optimization for a naturally centered rectangular shell, with arbitrary aspect ratios and complete rigidity of equality, is a useful sharp geometric extremal invariant. The planar equal-sided number was previously known and is not independently claimed.

The dated certificate retains the supplied scientific assessment, sources and limitations.
