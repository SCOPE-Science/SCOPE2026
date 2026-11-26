---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

Prüfer weighting marks the fixed label's excess degree with z and gives Z=(m+z)^{m−1}. Contracting a prescribed path gives the sum of its vertex weights times the product of interior weights, divided by the total weight to the path length; the two possible path classes for nonroot endpoints give the stated telescoping tails. In coefficient extraction for those tails, putting j=k−1 cancels (m−2)_{j−1}/(m−1)_j to 1/(m−1). The root sum is mF_t; the nonroot mean per pair becomes ((m−1+r)F_t+(r−1)J_t)/(m−1), where J_t=m−(m−t)F_t, yielding the claimed formula. The recurrence F_t=1+(t/m)F_{t−1} gives the displayed adjacent difference for the nonroot contribution. Its sign for r≥2 follows by the stated descending induction, with denominator minus numerator equal to 2 at the base H_{m−2}; at r=1 the nonroot difference vanishes but the root term strictly falls. For the first step, deleting the degree-one vertex yields a uniformly chosen attachment, while suppressing a degree-two vertex yields a uniformly chosen edge. For a fixed old vertex, orienting old edges away from it identifies its distances to all possible subdivision vertices with its old distances to the corresponding farther endpoints, justifying the 2W sum. Edge cuts give W(T_m)≥(m−1)², so the resulting first-step increase is at least (m−2)/m. The n=3 tie and n=2 single value are correct. A separate connected-edge-set enumeration with all-pairs breadth-first distances agreed on both conditional contributions for n=3 through 6 (3, 16, 125 and 1296 trees); the symbolic proof establishes all sizes.

## originality

PASS

The inspected prior aggregate and joint-moment results do not supply the exact fixed-label degree regression, and the all-size degree-two maximizer does not follow even from the shared path-counting tools without an additional inequality argument.

## value

PASS

A natural local degree statistic has a genuinely nonmonotone relation to global tree distances even though its covariance with W is zero by exchangeability and the deterministic total degree. The exact profile makes that dependence usable and the unique degree-two maximum explains its shape for every nontrivial size, not only in a computed range.

The dated certificate retains the supplied scientific assessment, sources and limitations.
