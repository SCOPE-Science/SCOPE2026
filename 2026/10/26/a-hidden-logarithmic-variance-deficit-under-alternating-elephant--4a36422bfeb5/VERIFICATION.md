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

# Verification checks and limits

The theoretical proof is contained in `RESULT.md`. To replay the independent finite-state diagnostics, place `verify.py` in the same directory and run `python3 verify.py`. The original recorded output is in `verification_output.txt`.

The program verified 322 exact-rational or floating-point assertions. Exact finite-state recursion checks seven rational alternating parameters through eleven full-memory updates, compares moments and two-step identities, and numerically evaluates log-slopes and macroscopic covariances. Those checks cannot establish the existence of an infinite-index limit; the elementary summable-error proof and the bounded-increment martingale functional limit establish the two analytic conclusions. This file records no independent mathematical audit.
