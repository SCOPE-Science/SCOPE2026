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

# Verification procedure and mathematical scope

Run `python verify.py` in the same directory as `RESULT.md`. The checker executes entirely with Python standard-library rational arithmetic, tests the explicit Hermite polynomial cancellation for five choices of the interior parameter and polynomial degrees from three through sixteen, and checks the inequality for 400 reproducible finite atomic measures over eleven tail indices, including equality of the two-atom comparator at the same eleven indices. It reports `PASS 8870 exact polynomial and moment checks`.

Those tests check implementation and examples, **not** every admissible probability measure. Universal validity follows from the explicit nonnegative Hermite-majorant argument in `RESULT.md`. The extremizers are actual subnormal shifts by the Berger-moment correspondence. No external or independent mathematical audit is represented by this verification statement.
