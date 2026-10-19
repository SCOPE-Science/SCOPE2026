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

# Reproducibility and limits

Run `python verification/check.py` with Python 3 and `mpmath`. The program verifies 186 high-precision numerical statements across dimensions 2 through 6 and four moderate target fidelities, supplemented by endpoint examples. It compares the positive-resolvent derivative with a hypergeometric backward-ODE representation, checks strict second-moment and Laplace bounds, and evaluates the harmonic identity by numerical integration. All 186 assertions passed in the recorded check.

The complete quantified proof is in `RESULT.md`: the finite checks are not exhaustive and cannot prove asymptotics or uniqueness by themselves. No Lean, external theorem certification, or external independent audit was performed. The idealized isotropic Brownian model and fixed-dimension/finite-transform parameter restrictions matter.
