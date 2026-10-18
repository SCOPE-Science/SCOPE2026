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

The mathematical proof classifies all vertices of the graph-Lipschitz dual ball and verifies a finite rational optimality certificate for the four nonspherical instances. For the remaining infinite parameter range, equilateral-ball inclusion and an explicit bound on exceptional vertices establish the optimal spherical containment without extrapolating from samples.

Use `python3 checker.py` with Python 3. The checker uses exact rational arithmetic for every orbit constraint and multiplier in the nonspherical cases. For the spherical family it makes bounded finite sanity checks only, while the paper's inequality \(R_p^2\ge2\) gives the actual infinite proof. No tolerance or numerical optimization is needed. The checker and the six accompanying files are embedded directly with this result; independent validation has not been performed.
