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

The proof begins from the published scalar SOFIM Algorithm 1 and retains the exact source moment and bias correction. The universal period-two identity and Jury stability inequalities are proved algebraically in `RESULT.md`. The actual bias-corrected attraction estimate is proved using explicit rational interval enclosures for the derivative, a weighted-sup contraction, and a summable correction term.

Running `python verify.py` from the package directory checks the underlying Sherman–Morrison rational identity, exact rational cycle and Jury equalities, contraction constants, and actual source-initialized trajectories for multiple positive momenta and varying source parameters. The script prints `verification passed` when all assertions succeed. Numerical trajectories are only finite consistency tests; the proof supplies all-time coverage.

Limitations: the analysis is deterministic and scalar, with constant learning rate. No external independent scientific audit has been conducted.
