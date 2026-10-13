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

The analytic proof is primary.

`artifacts/verify.py` constructs \\(\\operatorname{Cr}_n\\) directly, tests the strong-majority condition from every open neighborhood, independently evaluates the side-capacity characterization, and compares direct palette and surjective counts with the multinomial and inclusion-exclusion formulas.

Replay output:

`ALL CHECKS PASSED; color_assignments_checked=672856; exhaustive_cases=[(3, 3, 36), (4, 4, 576), (5, 3, 8100), (6, 3, 8100)]; structural_formula_n=3..50`

The exhaustive computation is finite corroboration only. The arbitrary-order result follows from the exact neighborhood argument in `RESULT.md`.
