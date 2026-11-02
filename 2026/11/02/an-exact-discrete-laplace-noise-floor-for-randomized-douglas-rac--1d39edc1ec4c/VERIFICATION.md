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
# Verification and reproduction

Execute `python verification/verify.py` with Python 3 standard library only. This replays ordered double reflections, performs exact rational one-step and 12-step recurrence checks for each of four sampling configurations, and separately evaluates the stationary geometric characteristic function and scaled Laplace limit. It prints a `VERIFY_OK` message on success. The proof of unique invariant probability, exact probability masses, all-parameter second moments, and weak scaling is contained in `RESULT.md`; the finite and numerical checks are corroborative, not certification of infinite statements.

The computations concern exact deterministic algebra and stochastic expectations, not floating-point stability of a deployed solver. The invariant and total-variation statements require \(0<q<1\). No independent audit has been performed.
