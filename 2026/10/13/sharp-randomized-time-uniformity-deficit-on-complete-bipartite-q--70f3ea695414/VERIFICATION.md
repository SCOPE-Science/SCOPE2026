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

# Reproducible checks and mathematical limits

Execute `python3 verify.py` from the directory containing this document and the standalone verification script; it needs only Python's standard library and makes no network requests.

The reproducible output is:

`VERIFY_OK exact_gradient_tests=432 exact_matrix_entry_tests=138840 star_formula_tests=72 two_by_many_tests=73 balanced_threshold_tests=73 feasible_two_atom_tests=1872`

The program checks exact integer-matrix multiplication for the adjacency-cubic identity; exact rational reductions of all five transition-probability types; exact central differences of the two partial derivatives; the exact formula and boundary-gradient certificate for 72 stars; the exact root and loss for 73 two-by-many graphs; and the balanced threshold and loss for 73 cases. Its two-atom comparisons are merely sample-based, with numerical tolerance, and cannot establish global minimality.

The general conclusion over all part sizes and all time probability measures comes from the explicit polynomial spectral reduction, the exact cosine-moment feasible region, the positive-definite Hessian, and the global supporting-hyperplane or increasing-cubic arguments in `RESULT.md`. The complete scientific proof is required: the script is not a formal proof or an independent evaluation. No finite experiment is represented as an exhaustive test of infinite mathematical domains.
