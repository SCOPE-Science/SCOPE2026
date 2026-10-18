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

The analytic proof in RESULT.md establishes unrestricted candidate optimality when \(N(p,q)\ge0\), necessity when \(N(p,q)<0\), and uniqueness of the positive imbalance boundary. Run `python verify.py` with Python 3, SymPy and NumPy. The script checks eight exact symbolic identities and 231 finite full-matrix examples, including signed perturbations. Numerical eigenvalue comparisons use an explicit 1e-9 tolerance and are corroborative rather than universal certification. No independent audit or external validation was performed.
