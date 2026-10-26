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

# Reproducibility and scope

Run `python3 verify_orientation_threshold.py` using Python 3 and the standard library. The program recomputes both orientation graphs directly from the angular-distance definition; checks the eight-angle equitable quotient, twelve-angle six-regularity and positive Perron vectors; computes expected letter fractions in exact-integer transfer counts for half-stacks of lengths 12, 30, and 80; and prints `VERIFY_OK` upon success. The count 102102368 at eight orientations and the rounded 1.99e10 at twelve agree with the primary table for a half-stack of length 12. The original mathematical argument additionally invokes standard analytic Perron perturbation and Chernoff concentration; finite numerical checking alone does not verify the all-length exponential tail bounds. The 10-percent conclusion concerns the quota alone, with balance not imposed. The critical quota equalities are not analyzed.
