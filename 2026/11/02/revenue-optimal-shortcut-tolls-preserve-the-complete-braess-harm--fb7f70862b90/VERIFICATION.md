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

# Reproducible checks

Run `python3 verify.py` using Python 3.10 or newer. This script uses standard-library `fractions.Fraction` and `itertools`, and rechecks the asserted toll-optimality and Wardrop inequalities on finite rational grids. Recorded result for the packaged code: `VERIFY_OK assertions= 55507`.

The proof in `RESULT.md` is the all-real mathematical evidence. The finite checker does not prove global optimality, uniqueness or the sharp continuous maximizer; those follow from the displayed exact quadratic formulas and derivative calculation. No independent mathematical audit has been performed.
