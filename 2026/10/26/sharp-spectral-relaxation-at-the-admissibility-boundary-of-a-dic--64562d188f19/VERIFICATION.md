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

Finite reproducibility: run `python3 verify.py` with the Python 3 standard library. The script checks the exact moment identities with rational arithmetic, validates transition probabilities for a finite range, and verifies small characteristic-log residuals of the winding-one root for specified dimensions. It reports the numerical root gaps and second-order moment estimates.

Infinite verification: RESULT.md proves the characteristic equation, local analytic root existence, strict radial ordering of its phase for modulus greater than the maximum holding probability, and the moment asymptotic through the fourth moment. The fourth-moment term supplies the displayed negative next-order correction; moment growth bounds control the remainder. Finite tests do not certify these limits or the global spectral ordering.

This package contains no independently conducted audit or independently validated mathematical certificate. The result applies only to the stated boundary-normalized ring and claims no general quantum-state fidelity rate.
