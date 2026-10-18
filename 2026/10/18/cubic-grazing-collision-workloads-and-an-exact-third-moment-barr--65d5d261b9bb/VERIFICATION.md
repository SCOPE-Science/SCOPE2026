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

Run `python3 verify.py` with Python 3.11 or newer. The verifier uses only standard-library modules and prints a deterministic assertion count, representative two-dimensional Gaussian probabilities, and a high-reflection asymptotic check.

The analytic proof independently establishes: the constant-chord geometric reduction, exact conditional reflection-count integral (1), the cubic integral identity (2), passage to the small-step and large-count limits using a uniform cubic bound, and the moment cutoff and expected-work limit by summing tails. Numerical quadrature and finite telescoping checks are **not** proofs of infinite-range conclusions.

No stochastic trajectory simulation or fitted exponent is used to certify the theorem. The calculation applies to a free billiard substep, not an entire stochastic integrator. No independent scientific audit has been performed.
