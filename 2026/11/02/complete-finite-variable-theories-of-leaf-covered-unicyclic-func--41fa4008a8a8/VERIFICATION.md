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

Two standard-library Python checkers are supplied. Execute `python verify_necklace_profiles.py` and `python verify_necklace_pebbles.py` after extracting these files into the same directory. Compare their stdout byte-for-byte against the respective `.out` files; both were replayed successfully from the package inputs.

The first checker exercises two-variable stationary extension profiles across 1,092 finite instances, Burnside necklace counts for 30 length/alphabet combinations, and 112 direct local sibling-witness tests. The second computes stable substitution-set color refinements of all variable assignments, using exact finite fixed points, across 135 two-variable examples, 52 three-variable examples, and eight four-variable pairs. It compares all predicted equivalence classes with the computed classes.

These calculations examine finite samples and provide no computational certificate for the unbounded theorem. The theorem's infinite cases rely on the variable-recycling definition, finite-path formula construction, and permanent matching strategy in RESULT.md. The review reported in REVIEW.md is not independent validation.
