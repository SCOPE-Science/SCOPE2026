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

The claim was checked at three levels.

1. **Analytic reduction.** With standardized fold means, each held-out log e-value is an explicit quadratic form in two independent standard Gaussians. Completing the Gaussian integral yields the exact component moment and its strict finiteness boundary.
2. **Transfer to the fold average.** For \(q\ge1\), Jensen's inequality gives the finite direction and positivity gives the divergent direction. For \(0\le q\le1\), the first moment controls the fractional moment. No independence among the \(E_j\) is assumed in this step.
3. **Executable arithmetic checks.** `verify.py` uses exact rational arithmetic for the determinant and all integer threshold tests, checks the \(K=2\) golden-ratio equation numerically at high precision, and verifies that balance uniquely maximizes the two-way ratio on a rational grid.

The executable checks support the algebra but do not replace the analytic proof. The literature search cannot certify historical novelty, and the inaccessible supporting-information file noted in the review remains a residual risk.
