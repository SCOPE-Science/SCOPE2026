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

The accompanying `checker.py` program uses Python 3 standard-library exact integer and rational arithmetic for small sizes. It examines all parking functions for \(2\le n\le6\), verifies their count and exact marginal recurrence, and checks the censored one-coordinate chi-square identity and data-processing inequalities in the enumerated ranges. Its latest replay returned `finite_assertions 209` and `all_finite_checks_passed`. The additional logarithmic-energy computations for selected larger sizes are diagnostic, not certificates of the limit.

The infinite theorem follows from the stated Lorentzian entropy-contraction input, exact Borel-ratio marginal recurrence, uniform endpoint asymptotics, coarsened likelihood-characteristic-function argument, and harmonic majorization. It is not proved by enumeration. The correctness and priority assessment is self-review only; independent auditing has not been performed.
