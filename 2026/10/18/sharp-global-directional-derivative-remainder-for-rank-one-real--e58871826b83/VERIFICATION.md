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

# Verification of the trace-norm remainder formula
The exact proof is in `RESULT.md`; `verify.py` gives reproducible corroboration on finite-dimensional real matrix spaces. It checks the rational upper-branch witnesses at \(t=6/5\), \(8/5\), \(2\), the lower-dimensional scalar exception, the \(t\ge2\) extremizer, and random trace-norm-unit perturbations in several rectangular shapes. The contraction-completion lemma is justified analytically by the Julia dilation and orthogonal rotation and is not inferred from random samples.

To execute: `python verify.py`. Requirements: Python 3.10+ and NumPy. The program reports test counts and exits unsuccessfully on an unexpected result. Numerical tolerances are limited to roundoff; exact equalities use rational arithmetic. The infinite-dimensional claim is **proved, not numerically enumerated**, using the displayed lemmas.

No independent audit was performed.
