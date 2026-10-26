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

Run `python verification.py` using Python 3 with its standard library. The checker verifies exact rational equality between a state-space first-arrival recursion and the derived closed finite-volume sum on all sites of 112 finite comb/rate settings. It then checks 54 finite-volume bounds by independent adaptive quadrature, plus non-asymptotic samples of strict rate ordering and the leading weak-/strong-rate limits.

The analytic derivation in RESULT.md establishes the countable-graph and arbitrary-parameter assertions; finitely many computations cannot certify them by themselves. The related independent scientific audit has not been performed.
