---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-22.md",
      "INDEPENDENT_AUDIT_2026-10-22.json"
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

For real ℓ1^n→ℓ∞^m maps the induced norm is the maximum entry magnitude, so unit ball is [-1,1]^{mn} and extremes are exactly sign matrices. Every norm-one rank-one A=uvᵀ has a finite decomposition into rank-one sign matrices using independent Bernoulli signs with expectations u_i and v_j. For each r≥2, choose S with columns 1 and 1−2e_1,...,1−2e_{r−2} and S′ obtained by flipping row r−1, column r. Then ranks are r−1,r, every strict interior edge point has rank r, and every saturated coordinate forces any extreme decomposition to use both S and S′, hence a lower-rank vertex. All m,n≥r covered, including r=2, one-row/column cases have only rank1. Inspected exact-rational checker for ranks and independent-sign barycentres; finite tests are supplemental, not a universal argument.

## originality

PASS

Best-of-knowledge: targeted semantic published search, direct mathematical implication checks and primary full-text comparisons identify relevant component machinery or partial results but not a dominating exact statement, with the listed residual risks.

## value

PASS

This is a complete sharp order-by-order classification of a named rank-constrained Krein–Milman property for a whole natural rectangular operator class. The adjacent-rank exposed cube edge is a structural obstruction useful for tensor/operator geometry, not a renamed extreme-point count or an isolated rank-two example.

The dated certificate retains the supplied scientific assessment, sources and limitations.
