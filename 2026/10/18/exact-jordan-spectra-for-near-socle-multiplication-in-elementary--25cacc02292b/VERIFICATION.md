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
# Computational verification and proof boundaries

Run `python3 verify.py` in the directory containing this file. The script relies only on Python's standard library. It verifies the Gaussian-subspace count recurrence and the predicted rank frequencies for field orders \(2,4,8\) and dimensions \(6\) through \(11\), exhausts the \(1{,}048{,}576\) binary alternating three-forms in six variables, and constructs genuine wedge multiplication matrices to test the contraction-rank theorem in 360 reproducible examples over binary and quartic fields and dimensions six and seven. For six variables and field order two it prints the exact frequency dictionary `{0: 1, 8: 1395, 12: 54684, 14: 992496}`. The full enumeration is exhaustive only for that one finite case; finite experiments do not certify the universal theorem. The general result depends on the four-step proof in `RESULT.md` (perfect exterior duality, contraction-rank realizations and obstruction, and Gaussian Möbius inversion).

The field-order-eight portion tests integer combinatorics, not full multiplication matrices. The code is an independent implementation of finite-dimensional checks, not an external mathematical audit.
