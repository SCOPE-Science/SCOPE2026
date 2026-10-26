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
# Reproducibility checks

Run `python verify.py` using Python and NumPy to reproduce `verify_output.txt`. The checker verifies the sharp rank-one counterexample using `fractions.Fraction` on both sides of the threshold for six budgets and three spectral ratios (36 exact witness cases), and tests iterates of 455 seeded positive semidefinite matrices from the allowed class. The finite checks do not replace the dimension-uniform proof given in `RESULT.md`, and do not certify originality. The exact equality case relies on an adversarial but allowed tie decision; the analytic proof supplies the boundary argument.
