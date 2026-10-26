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

# Computational checks and reproducibility

Run the included standalone `CHECK.py` using Python with SymPy, NumPy, and SciPy installed. The program reconstructs the symbolic stationary covariance, proves the zero Lyapunov residual exactly, checks the closed-form current, verifies both resultant factorizations exactly, and tests the sharp equality case. Its independent random-parameter comparisons comprise 340 stable three-variable Lyapunov covariance solves and 163 scalar optimization families, including both exact extremal mass ratios.

Observed output: `PASS: 7 exact symbolic assertions; 340 independent 3x3 Lyapunov cases; 163 optimization families and sharp extremizers.`

Only the reduced relative-displacement/velocity process is stationary; the common translation is not. Floating-point tests are not an exhaustive proof of universal inequalities. The analytical derivation of all-domain uniqueness, mass-swap symmetry, and the sharp extremal constant is in `RESULT.md`. Historical novelty rests on the stated limited primary-source comparison and is not independently established by this program. No independent external audit was conducted.
