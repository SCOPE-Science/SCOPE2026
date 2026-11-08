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

# Verification of the finite-mean bound

The claimed expectation estimate is established analytically in `RESULT.md`. In particular, the drift inequality applies simultaneously for all admissible integer states at every time \(n\ge9999\). The checker `verify.py` does not enumerate those infinitely many states and is not an infinite proof.

To replay locally, run `python3 verify.py` using only the standard library. It checks finite-horizon transition probabilities and moment identities with `fractions.Fraction`; checks the rational Lyapunov identity and its coarse bound at specified rational arguments; and checks a sample of exact discrete transitions against the proved envelope. The proof's independent steps are the explicit calculus estimates, stopping argument, and exact second-moment recurrence.

Scope limitation: the displayed bound is not optimal. No claim is made about the precise mean return time or higher-dimensional recurrence type. Independent audit has not yet been performed.
