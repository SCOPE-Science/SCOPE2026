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

# Verification of the mathematical statement

The exact-rational `verify.py` reconstructs the full five-node simultaneous update and each edge confidence at every sampled step. Tests use decay factors \(1/2,7/10,3/4,4/5,9/10\), confirm the predicted first bridge appearance at times \(5,2,1\) for the last three, and check 61 states of the closed two-dimensional recurrence. It also checks the four-path stationary-weighted mean \(3/10\), eigenvalue relations, and high-precision numerical consistency of the exact radical coefficients.

Run `python3 verify.py`. Python version 3.9 or later and its standard library suffice. Test outcomes are checks for computation/transcription; the infinite-time iff, equality case, critical first-time asymptotic, and restricted minimum size are verified by the analytic inequalities in `RESULT.md` and are not claims of exhaustive computer verification.

No independent validation has been performed. Relevant scientific uncertainties concern unindexed equivalent literature and non-generic initial equality.
