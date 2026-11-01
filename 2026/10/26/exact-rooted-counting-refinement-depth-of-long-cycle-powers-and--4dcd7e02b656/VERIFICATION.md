---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-31.md",
      "INDEPENDENT_AUDIT_2026-10-31.json"
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

For k>=2,n>=4k+1, the first counting-refinement round separates root, the union T_1..T_k, and the far tail. The round-two near-to-far counts are j for 1<=j<=k and far-to-near counts 2k-j+1 for k<j<=2k. Each later tail index a<j<=a+k has first separated neighbor T_{j-k}, while more distant tail points have none; reflection enforces no within-T_j separation. The last residual distance alone is a class, so strict first stabilization is ceil((floor(n/2)-1)/k). At n=4k the antipodal wraparound makes T_{2k-1},T_{2k} coalesce at round two and split at round three using T_{k-1}. The argument covers all integers in the stated domain, independently corroborated by new direct exact refinement for 265 pairs and 10 boundary cases; finite checks do not prove the induction.

## originality

PASS

Best-knowledge PASS for the exact strict-round trajectory and sharp wraparound exception; the prime-order endpoint stable partition is known via Kluge and is explicitly NOT credited as new. No inspected prior result implies the all-n depth and boundary.

## value

PASS

The power-of-cycle family is a canonical undirected circulant; exact synchronous iteration depth and the 4k wraparound threshold quantify a meaningful structural complexity boundary, unbounded in n at fixed k. The parameterized frontier is stronger than an isolated finite computation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
