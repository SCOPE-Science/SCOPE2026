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

# Reproducible verification

Run `python3 check_a4.py` with Python 3 and the SymPy version specified in `requirements.txt` (or a compatible version). It produces the output `ALL_CHECKS_PASS 34` and fails with an assertion if any exact identity fails. The checker independently enumerates the \(12\) matrices, computes their action on the normalized six-dimensional symmetric tensor square, and verifies the general twirl formula for three separate algebraic input generators. For the explicit optimal seed, it also checks the quartic equations, projective-design second moments, full nine-dimensional tensor moments, and exact recovery on a basis of Hermitian matrices.

The analytic proof, including equality in the sharp spectral bound and the classification for **all** unit generators, appears in `RESULT.md`. The checker is a supplementary finite symbolic test, not an infinite certification or a proof of priority. Exact arithmetic is used; no floating-point tolerance or external data is required.
