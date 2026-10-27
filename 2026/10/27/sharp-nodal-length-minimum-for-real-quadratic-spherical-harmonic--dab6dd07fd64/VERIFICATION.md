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

The exact symbolic identities in the proof are checked by `verify.py` using SymPy. Independently, spherical-curve arclength and the Crofton expectation are computed by different integrands using SciPy quadrature at eight coefficient values. The recorded output is `verification_output.txt`. Execute `python verify.py` after installing `sympy` and `scipy`.

These numerical samples are not an exhaustive search over coefficients and are not offered as proof of the global theorem. The universal quantifier and exact equality cases depend on the fully stated Crofton argument and positivity factorization. The historical upper bound is attributed to the primary source, not presented as an original theorem.
