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
# Verification

The packaged script `verify_error_budget.py` checks the exact normal-mixture allocation formulas with deterministic arithmetic. It verifies: strict positivity of the analytic second derivative in the stated confidence-level regime; equality of the closed-form objective and the claimed minimum; stationarity at the square-root clock allocation; numerical domination over dense alternative allocations in two- and three-arm examples; the characterization of equal splitting in balanced clocks; and the entropy identity used in the second-order penalty.

The checker does not establish originality and does not justify data-dependent error allocation. Its purpose is to catch algebraic, normalization, and indexing mistakes in the stated deterministic theorem.
