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

# Verification details

The accompanying standalone `checker.py` was executed with Python 3's standard library and reported:

`PASS: 193,404 exact arithmetic assertions; exhaustive permutations n=2..9; polynomial laws n=2..80.`

The program checks conditional record-count numerators by direct full enumeration, exact normalization, symmetry under reflected positions, all integer thresholds of the adjacent conditional tail formulas, the conditional means, and the exact one-Wasserstein and total-variation distances. It uses integer arithmetic except for exact rational values in expectation comparisons.

The general proof proceeds from uniform deletion/standardization and the identity that the newly inserted fixed point contributes precisely one extra record when the earlier segment contains all smaller values. The conditional distributional polynomials yield each adjacent comparison. Real-rootedness of rising-factorial products gives unimodality for the exact variation distance. Finite computation is not an infinite certificate.

This is not a statement of independent audit or independent validation. The historical novelty comparison is qualified by the literature-coverage limits reported in the review.
