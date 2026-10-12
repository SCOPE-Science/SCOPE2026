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
# Reproducible mathematical checks

Run `python3 verify_cycle.py` in the same directory. Standard-library `fractions.Fraction` is the only arithmetic engine; no extra packages, internet, stochastic trials, or floating-point numerical tolerances are needed.

The checker asserts exact agreement between the source best-response discriminant and the implemented threshold, the complete four-by-four rational influence matrix, every rational decision and opinion value at both cycle steps, the coexistence of the two consensus equilibria, strict decision-input margins, and the four eigenvectors and multipliers of the two-step linearization. It also evaluates the general-family invariant-state identities for several additional exact parameter choices; the proof for all admissible parameters is given in `RESULT.md`, not inferred from those samples.

Expected output: `VERIFY_OK`.

**Review limit:** These checks corroborate a self-contained mathematical proof and specific algebraic values. They do not provide independent audit, prove uniqueness or global basins, address strictly singleton update schedules, or validate the model as an empirical description.
