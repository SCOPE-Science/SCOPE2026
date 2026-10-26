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

Run `python3 verify.py` with Python 3.8 or newer. It imports only the standard library and prints `certificate.json` when redirected to that path. The version embedded here uses exact integer-coefficient Laurent polynomials in four indeterminates to calculate the two-season matrix product and check its full determinant factorization. It independently tests 448 rational parameter/rate configurations, of which 300 have strict improvement certificates and 148 are boundary or homogeneous cases. This symbolic determinant identity is an algebraic certificate; the inferential step from a negative characteristic polynomial at one to a Perron root above one is proved in RESULT.md.

The checker does not certify the completeness of the literature search, ecological field validity, nonlinear population claims, or an external independent audit. Reproducible computations use only the files in this package and do not depend on temporary paths, prior files, or external datasets.
