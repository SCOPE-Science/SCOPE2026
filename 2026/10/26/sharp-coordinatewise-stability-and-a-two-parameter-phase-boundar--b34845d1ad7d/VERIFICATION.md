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

The universal theorem follows from the mathematical proof in `RESULT.md` and is not inferred from computation. The accompanying Python 3 standard-library file `verify_extended_cone.py` was executed successfully with 164490 assertions.

The program independently compares finite-difference projection derivatives against the analytic active-set Jacobian for many integer pairs; tests 14 random global input pairs for each tested dimension; checks randomized active-chart row bounds; and tests both claimed asymptotic extremizing mechanisms. It also checks the strictly concave scalar objective against a 1001-point grid in each of 29 vector dimensions.

Reproduce with `python3 verify_extended_cone.py` from the package directory. All files required for this check are embedded together. This numeric verification is neither an exhaustive proof nor an independent audit, and the asymptotic and all-dimensions conclusions rely entirely on the analytic argument.
