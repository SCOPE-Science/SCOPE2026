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

# Verification of the weighted quadratic norm rigidity theorem

Run `python3 verify.py` using a standard Python 3 interpreter. The script uses only the standard library. It verifies every one of the eight exhibited equal norms, the rank of their rational coefficient matrix, the exact determinant of its first eight columns (\(-608\)), all pair-collision ranks for cutoffs \(3\) through \(10\), the nonquadratic radius-nine delta-at-five witness, and the coefficient identity giving the infinite recurrence. It also tests the explicit converse on representative values of the parameters.

Actual execution returned:

`EXACT_CERTIFICATE_OK finite_threshold=10 minor_det=-608 rank10=8 rank9=6 witness_count=8 propagation_step=8`

The infinite claim rests on the printed symbolic identity and an induction from the ten initial values. Program output by itself is not an infinite proof. The outer function is characterized only on the set of positively represented values, and the minimality assertion concerns finite collision constraints, not pointwise evaluations of the original nonlinear one-function equation.
