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

# Reproducibility

Run `python3 checks/check.py` from the directory containing this file. No nonstandard Python dependencies are required. The checker performed 1,170 assertions successfully: exact rational ratio monotonicity and factorial-weighted log-concavity, 80-digit decimal mean/variance, finite truncation normalization, and agreement of the first-site Stein-factor formula with the maximum over 80 positive indices.

The proof itself requires no computational certificates: each inequality and all infinite sums are handled analytically in RESULT.md. The 101-term finite probability sums serve only as diagnostics and are never used to infer an infinite theorem; their normalization residual was checked below \(10^{-60}\) in each displayed case. The arbitrary-parameter statement, the infinite-support property, the exact supremum and the failure of the universal variance-scaled bound are established in the analytic argument.

No independent review or validation was performed.
