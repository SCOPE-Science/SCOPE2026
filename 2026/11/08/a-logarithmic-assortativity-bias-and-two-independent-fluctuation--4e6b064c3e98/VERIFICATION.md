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

The standalone `check.py` program uses only Python's `fractions`, `itertools`, and `math` modules. It checks all feasible two-type counts with both types present up to 30 vertices, seven rational affinity values, and exact small-chain edge-count distributions. It independently computes the first two moments of the quadratic imbalance functional by exhaustive sign-sequence enumeration and compares them to the covariance-sum formula.

Observed output when executed from the complete package: `PASS 15432 exact-rational assertions`.

Limits of verification: exhaustive checks are finite, do not certify the infinite-population Gaussian limits or literature priority, and should not be interpreted as independent audit. The analytic proof supplies the martingale and almost-sure steps. The displayed numerical examples are exact rational consequences of the formula.
