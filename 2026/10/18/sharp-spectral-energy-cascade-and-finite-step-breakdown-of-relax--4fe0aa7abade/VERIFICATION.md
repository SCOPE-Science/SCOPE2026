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

The standalone `verify.py` uses only the Python standard library. Run `python3 verify.py` from the extracted package directory; the expected terminal line is `REPRODUCIBLE_CHECKS_OK 44509`.

The program directly evaluates stage inner products and the three correction-quadratic coefficients for 800 rational oscillator instances, separately evaluates the exact energy increment for 1200 rational data sets, and checks the two-frequency first-step/second-step boundary. Further deterministic finite-step tests check modal amplification ordering and total-energy conservation for a set of independent subcritical frequencies. The algebraic derivation and inequalities in `RESULT.md`, not these finite checks, establish the claims for arbitrary finite numbers of modes and all iterations.

Independent scientific validation has not been performed. Exact arithmetic is assumed in the theorem; floating-point underflow, overflow, branch selection near a vanishing discriminant and adaptive-step implementations are not covered.
