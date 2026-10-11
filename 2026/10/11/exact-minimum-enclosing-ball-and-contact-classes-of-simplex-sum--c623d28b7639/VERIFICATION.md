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

# Reproducibility and finite checks

Run `python3 verify.py` from the extracted package. The script uses Python 3 standard-library `fractions.Fraction`, `itertools.permutations`, and a fixed-seed local pseudorandom generator for independent generic support vectors. In the recorded run, it passed exact rank identities for all integers from 1 to 80 (3,320 identities), explicit enumeration of 125,672 vertices in dimensions 1 through 8, 46,241 exact vertex-sphere contacts, the weighted contact-barycenter conditions, and 600 independent simplex-sum support calculations. All distance, clearance, and contact tests use exact rational integers; the support-vector cases choose distinct integer coefficients.

No computational enumeration proves the statements for unbounded \(k\). The infinite conclusion follows from the support-function enumeration, geometric-series identity, and positive barycentric variance identity written in RESULT.md. Computations neither establish priority nor substitute for independent mathematical validation.
