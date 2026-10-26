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
Execute `python verify_switching_trap.py` with dependencies in `requirements.txt`.

The script separately solves the stationary even-moment generator recurrence and compares it against moments obtained from the two beta-prime mixture components, for 180 seeded exact-rational instances with different switching, stiffness, diffusion, and moment orders. It verifies the stationary two-state PDMP flux balance symbolically and six large-deviation beta-prime tail coefficients using arbitrary-precision incomplete-beta evaluations. Successful tests are empirical/algebraic checks of sample parameters; the all-parameter theorem follows from the proof in `RESULT.md`. The program is not a numerical certificate for all parameter values. No independent scientific audit has been performed.
