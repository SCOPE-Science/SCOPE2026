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

The standalone `check.py` executes the formula checks using only Python standard-library modules. Verified by invocation `python check.py`: 256 exact rational polynomial substitutions, 72 independent interface resolvent comparisons, 192 nonlinear pole comparisons, and seeded simulations for tumbling rates 0, 0.5 and 2. All completed with PASS.

The stochastic simulations are finite-sample diagnostics, not evidence of the general infinite-time LDP. The proof in RESULT.md supplies the necessary renewal-theorem and convex-duality arguments. No independent review has occurred.
