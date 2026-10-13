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

The analytical proof establishes the universal low-degree and two-dimensional statements. The bundled `verify.py` uses only the Python standard library and exact rational arithmetic to replay the finite witness. It checks the three eigenvalues from the block structure, constructs the degree-three Chebyshev approximate-inverse polynomial at \(\kappa=4\), multiplies it by the stated right-hand side, verifies the negative coordinate exactly, and verifies the stated positive exact solution by direct multiplication.

The checker does not enumerate arbitrary matrices and is not evidence for the universal quantifiers; those are discharged symbolically in the proof. Floating-point behavior, loose spectral bounds, irreducible witnesses, and degrees beyond three are not verified or claimed.
