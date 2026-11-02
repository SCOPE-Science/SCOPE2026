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

# Verification of the mathematical claim

The accompanying `verify.py` checks both factorizations as exact rational identities, shows the two-cycle parametrization satisfies both dynamical equations symbolically, and checks the strictly positive numerator of the sharp \(16/3\) gap. It also checks representative rational parameter values and finite-gridded iterates; these numerical examples are diagnostics only. The global statement rests on the algebraic exclusion of period-two points, the established Coppel interval-iteration convergence theorem, invariant-interval control, and elementary monotonicity outside it. No finite computation establishes convergence at every initial state.

Independent audit: not performed. This package documents a self-review only.
