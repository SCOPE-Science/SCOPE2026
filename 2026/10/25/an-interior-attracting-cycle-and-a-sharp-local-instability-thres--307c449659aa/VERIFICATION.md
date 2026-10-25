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

The standalone `verify_lottery_cycle.py` was executed with Python standard-library arithmetic and its assertions passed. It uses exact `Fraction` endpoints and `math.isqrt` to outward-enclose every square root on a rational grid at scale `10**24`; no floating-point quantity enters any assertion. Its certificate gives strict endpoint signs for \(F_{1/6}^2(y)-y\) on the rational interval `[26299/100000,26300/100000]`, maps that interval disjointly into `(97447/100000,97455/100000)`, and bounds the two-step multiplier between `17/100` and `18/100` throughout the interval.

The continuum-parameter existence proof instead uses the analytic invariant interval, exact Nash multiplier and intermediate value theorem. Code checks neither uniqueness of the period-two orbit nor global attraction, and no claim relies on a finite experiment as proof for all cost ratios. The exact origin and model assumptions are described in `RESULT.md`.
