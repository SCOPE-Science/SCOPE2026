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

# Verification record

The direct proof establishes the infinite-dimensional statement by averaging, zonal polynomial decomposition, a sign-function dual bound, Beta/Gamma integrals, and a two-region sign-error expansion. The accompanying `verify.py` uses only the Python standard library and passed 60 numerical checks of normalization, first-band multiplier comparison and dimension-dependent one-sided expansions. The finite tests are not used as proof, and no external or independent validation has been undertaken.

Run with `python verify.py` after extracting the file next to this document. The result concerns real-valued continuous functions and fixed dimension; it does not assert a universal stability rate for nonsymmetric minimizers.
