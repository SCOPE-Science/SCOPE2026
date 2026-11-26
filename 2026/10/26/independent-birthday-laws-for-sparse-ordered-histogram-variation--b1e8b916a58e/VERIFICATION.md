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

The exact path identity is 2N−T=X₁+Xₙ+2Z, with Z the sum of neighboring occupancy minima. The difference between the adjacency-pair count W and Z is a nonnegative integer bounded by the sum of the two ordered-triple counts across each edge. Their factorial moments are (N)₃/n³ apiece. Thus the mismatch probability between the joint statistics (C,2N−T) and (C,2W) is at most 2N/n+2(n−1)(N)₃/n³ under the sampling coupling. For the two-color process, an index is independent of the entire outside family when the observation pairs are disjoint. Each observation pair meets 2N−3 pairs including itself and 2(N−2) other pairs. Conditional on the shared observation's label, the support size for a same-or-adjacent mark is 2 at either end and 3 in the interior. Its first and second moments give qₙ and sₙ, including for n=2; different colors on the same pair are mutually exclusive. AGG Theorem 2 in event-supremum TV gives the claimed 2(b₁+b₂) with b₃=0. Summing by color and doubling the second count contract TV. The error O(N/n+N³/n²) tends to zero in the stated range; vanishing, finite positive and diverging Poisson means give the three phases, with common deterministic standardization for the Gaussian comparison. Zero defect requires empty endpoints and separated occupied interior sites. Removing the mandatory gaps counts these sites by the stated binomial, and counting labeled surjections yields the two exact formulas. They concern attainment of the ceiling 2N (unattainable at n=2), not the actual largest attainable value at n=2. Inspected the frozen checker and recorded evidence without executing it: exact identities and extremal counts are checked in finite cases, the displayed joint TV bound is capped at 1 on that enumerative grid, and the simulations are diagnostic only. The nonvacuous estimate follows from the proof.

## originality

PASS

Pass for the path-specific joint collision/variation-defect estimate and closed extremal counts, not for the underlying Comb statistic, exact-null computation in general, or Poisson process theorem. The closest identified indexed analogue is cyclic and univariate, and does not give the path coupling or the joint distribution.

## value

PASS

The theorem calibrates a naturally used histogram statistic in a regime different from large samples on a fixed grid. The joint estimate shows that coincidences and neighbor interactions behave independently even though they use the same sample; its error gives a usable simultaneous range and also transfers the independent Gaussian phase. The endpoint-aware exact formula gives a finite check for zero defect. This is more than a rephrasing of a marginal birthday approximation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
