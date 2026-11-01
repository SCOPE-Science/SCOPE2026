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

The proof uses exact dyadic-interval images, formal power-series cancellation, the classical ballot identity, and the triangular-array central limit theorem. The only numerical evidence is the exact-rational independent check in `checker.py` (27 cases, three rational branch probabilities, times zero through eight); the critical-window asymptotic does not depend on empirical extrapolation. Execute with `python checker.py`.

The local central-limit proof applies to every fixed real crossover parameter with a uniform initial distribution. Its scaling conclusion is not a stationary-limit assertion. Independent audit: not performed.
