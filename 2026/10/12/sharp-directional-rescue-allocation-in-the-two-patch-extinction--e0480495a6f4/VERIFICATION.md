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

# Verification and limits

Run `python3 verify_allocation.py` with Python 3 (standard library only). The exact checker printed:

`VERIFY_OK exact_backward_systems=576 weighted_expectations=8640 allocation_instances=960 global_grid_inequalities=8640`

The checker constructs the transient \(3\times3\) backward matrix independently of the proposed closed forms, solves each system by fraction-valued Gauss-Jordan elimination, checks all closed-form values and weighted expectations, and compares the projected optimum against feasible grids. It also verifies exact strict local maximality for interior stationary points.

The sampling domain is \(a,b,C\in\{1,2,3,4\}\), allocations \(x=jC/8\), and all nonnegative three-state distributions with denominator-four weights summing to one. These finite enumerations are corroboration only; the all-parameter guarantee rests on the algebraic first-step proof and exact quadratic identity in `RESULT.md`. No finite experiment is claimed to prove uniqueness in an infinite parameter domain. Literature access limitations are documented in `REVIEW.md`. Independent audit has not been performed.
