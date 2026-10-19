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

The exact real proof is the drift calculation in `RESULT.md`, which derives a positive lower bound uniformly over both branches and over all allowed remainders. The program `verify.py` is a supplementary exact-rational stress test. Executing `python verify.py` checks 5,968 state/parameter/branch instances (including reversed and equal determinant signs), raising an exception if any strict lower-bound check fails.

The program does not certify uncountably many parameter values or all nonlinear remainders; the displayed analytic inequalities do. Published-source comparison is documented in `AUDIT.json` and the scientific review. Independent mathematical audit has not been performed.
