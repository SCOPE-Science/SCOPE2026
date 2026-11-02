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

# Reproducibility and proof coverage

Run `python3 verify.py` using Python 3. The file uses only the standard library and exact `fractions.Fraction` arithmetic. It enumerates all ternary-valued nonnegative profiles for \(2\le n\le8\), testing all integer horizons; 73,809 profile/horizon inequalities passed. It also tests 3,000 signed rational profiles at lengths \(9,10,13,21,37\), and the exact sharpness identity for 35 endpoint indicator/horizon pairs. No numerical tolerances were used.

The infinite family of inequalities is proved in RESULT.md by peak-plateau contact, partition into neighboring peak-to-valley subpaths, and the admissible full-interval average. The finite program checks this statement on test inputs only; it is not a formal certificate for all lengths. The publication originality assessment remains provisional pending independent review.
