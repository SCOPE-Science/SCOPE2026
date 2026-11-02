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
# Reproducibility and verification

Execute `python verify.py` with the Python standard library. The program constructs Ornstein–Uhlenbeck variances from independent closed-form and composite-Simpson evaluations; it also tests the deterministic Gaussian-supremum envelope, the short-time upper bound, and critical-crossover root calculations for several finite parameter combinations. The finite checks are consistency tests and cannot establish convergence or originality.

The proof's substantive infinite-dimensional components are the continuous Gaussian maximal inequality, the explicit uniform expected-supremum estimate and Gaussian Mills asymptotics. The only coefficient requiring a strict numeric comparison is \(\sqrt{14/(3\pi)}/(1-e^{-1})<2\), which the checker tests. The end-to-end asymptotic deduction is mathematical, not an enumeration. Independent audit has not been performed.
