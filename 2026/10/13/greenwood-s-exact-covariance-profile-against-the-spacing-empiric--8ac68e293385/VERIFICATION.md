---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---
# Verification

The theorem is analytic for every \(m\ge2\) and every \(0\le x\le m\).

`checker.py` uses exact rational arithmetic. For each \(2\le m\le80\), it evaluates a dense family of rational thresholds, computes \(\mathbb E[G_m\mathbf 1\{D_1>t\}]\) independently by exact beta-integral formulas, reconstructs the covariance with the exceedance count, and compares it to the closed covariance profile. It separately checks the variance of the empirical spacing CDF from one- and two-coordinate exceedance probabilities, the interior sign classification, and the exact zero-integral identity.

The finite checks are reproducibility tests for algebraic identities. The universal formulas are established by the proof in `RESULT.md`.
