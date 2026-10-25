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

Run `python verification.py` after installing the dependencies listed in `requirements.txt`. The source checks symbolic transfer identities and the first two Taylor coefficients, the exact mean-square damping formula and both sharp asymptotic constants, high-precision numerical quadrature for seven values of the stiffness parameter, and Euclidean contraction on 1,680 generated nonnormal dissipative complex matrix cases.

The printed successful status is `VERIFY_OK symbolic transfer, exact gap and two-term stiff asymptotic; 7 numerical integrals; 1680 nonnormal dissipative matrix checks; rigidity limits`. The matrix checks are finite stress tests, and the large-stiffness spot checks are diagnostic. Universal conclusions depend on the complete proof in `RESULT.md`; computations alone cannot verify a property for every matrix or every coupling. Independent audit was not performed.
