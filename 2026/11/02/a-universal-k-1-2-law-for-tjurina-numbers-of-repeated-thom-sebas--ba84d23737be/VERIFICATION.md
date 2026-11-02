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

## Reproducibility
Run `python verify.py` with Python 3.9 or newer. The checker uses only the standard library and verifies selected exact character-coefficient values, finite-dimensional nilpotent Kronecker-sum cokernel dimensions over a large prime, and the displayed polynomial derivative identity for the explicit plane-curve example. Its successful completion prints `VERIFY_OK`.

## Mathematical verification boundary
The certificate is finite and does not assert exhaustive testing of all singularities or all tensor powers. The main proof is an algebraic identification with a finite-dimensional \(\mathfrak{sl}_2\)-module followed by a standard lattice local central limit argument. The weighted-standard-basis proof of the specific plane-curve algebra is written in the result, rather than replaced by the finite computations. No independent mathematical audit has been performed.
