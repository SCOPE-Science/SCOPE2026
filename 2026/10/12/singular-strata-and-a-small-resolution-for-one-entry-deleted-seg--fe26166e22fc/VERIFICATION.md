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

# Reproducible finite checks and mathematical limits

Run `python3 checker.py` with Python 3 and no third-party dependencies. The included `checker.out` records a completed run. The program reconstructs all affine coordinate charts for integer parameters from two through six, checks bounded graded semigroup dimensions through degree four, and uses exact rational arithmetic to assess Jacobian rank on small determinantal cones. The observed outcomes match the stated chart dimensions, transversal singularities, and Gorenstein boundaries.

The general equalities of affine coordinate rings follow from the displayed monomial parametrization and the prime ideal of all two-by-two minors. Smoothness, normality, multiplicities, local divisor-class groups, and smallness are symbolic consequences explained in RESULT.md. The program neither proves these infinite statements nor independently audits the mathematics. An unindexed equivalent earlier specialization in the matrix completion literature remains a residual originality risk.
