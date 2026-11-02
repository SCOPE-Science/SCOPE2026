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
# Reproducibility
Run `python checker.py` using Python 3 standard library. This checks the exact symmetrization identity for 5,145 rational parameter choices and the Gaussian angular integral for 171 spectral pairs (5,316 checks in total). No external data or files are required. The infinite-domain correctness proof is provided in `RESULT.md`: exact projection identity, symmetrized rational nonnegativity, iid equality classification and elementary polar integral. Numerical midpoint quadrature verifies representative cases but is not a proof of the integral. Independent validation has not been performed.
