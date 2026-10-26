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

The `verify.py` artifact runs with Python 3.10 or later and only its standard library. `verification_output.txt` records an actual execution. It independently reconstructs the embedded two-edge count distribution, with exact rational arithmetic for exponent values 0, 1 and 2 and additional floating-point checks of strict moment ordering, stochastic tail ordering, the positive drift bound, and Poissonized covariance. It passed 650 checks.

The executable does not certify the infinite-time limit or universal stochastic coupling. Those use the parity-preserving induction and the comparison recurrence (1) in `RESULT.md`. Simulated or finite-state results cannot establish an asymptotic limit. Finite checks at exponent 1 or 2 are supplementary and do not enlarge the theorem's domain.
