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
# Verification and reproducibility

The complete all-length proof is analytical: it derives the probability-generating polynomial from the transfer matrix, excludes every imaginary-axis zero via a continuant recurrence, transports the negative root location from the fair-coin point by continuity, and groups conjugate roots into nonnegative quadratic probability factors. The exact variance comparison independently certifies sharpness of the factor-support bound for every biased sample with at least three observations.

The accompanying `check.py` requires only the Python 3 standard library. Run `python3 check.py` to verify transfer-matrix and recurrence coefficients by exact fractions, to compare small samples with explicit sequence enumeration, to test strict Routh–Hurwitz leading-minor inequalities for rational biases, and to check the first two moments and the sharp variance obstruction.

A successful replay printed `PASS {'coefficient_identities': 594, 'positive_Hurwitz_determinants': 396, 'exact_moment_identities': 132, 'last_tested_sample_size': 12}`. These are finite diagnostics and are **not** a proof about all \(n\) or all real \(p\); the general argument is contained in `RESULT.md`. No independent audit has been performed.
