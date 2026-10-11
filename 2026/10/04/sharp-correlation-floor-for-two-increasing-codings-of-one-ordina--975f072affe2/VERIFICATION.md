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

The cut-indicator proof reconstructs. With positive adjacent gaps, centered scores are positive combinations of nested upper-cut indicators H_j. Their covariance is P_min(1-P_max), and the normalized cut correlation is minimized by j=1,k=m-1, giving squared floor p1*pm/((1-p1)(1-pm)). Positivity plus the L2 triangle inequality transfers this floor to arbitrary strict codings; diagonal terms make it strict for m>=3. Dominant first-versus-last gap sequences approach the floor, Cauchy--Schwarz gives correlation at most one with equality exactly for positive affine recodings, and connectedness gives the entire interval. An independent random-gap stress test for m=3,...,7 approached but never crossed the bound.

## originality

PASS

Best-of-knowledge originality passes. Checked sources establish qualitative association or optimize correlation with fixed marginals/couplings, but no inspected result gives the exact endpoint-mass floor when both score vectors vary over all strict increasing codings of one fixed ordinal law.

## value

PASS

The exact worst Pearson agreement between arbitrary order-preserving codings of a fixed ordinal law is a natural robustness question. The theorem identifies the full attainable range and shows that only endpoint category masses control the worst case, substantially sharpening qualitative positive association.

The dated certificate retains the supplied scientific assessment, sources and limitations.
