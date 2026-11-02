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

The attached `CHECKER.py` reproduces the 21 small-degree exact rational ranks used in the proof. It constructs 12 representatives from each normalized 24-cell, verifies antipodal sizes and all cross-part nonorthogonality counts, and computes ranks of the 24-by-24 parity-reduced matrices. The matrices have rational integer entries after a transparent congruence transformation in odd degrees. No floating-point tolerance, numerical rank heuristic, or third-party service is required.

The mathematical proof establishes strict diagonal dominance for every odd degree at least 19 and every even degree at least 24. The checker deliberately verifies only the remaining degrees; the infinite assertion uses the analytic bound. Independent symbolic rank calculations were also performed for degrees 4, 6, 8, 9, 10, 14, 16, 20, and 22 and gave the same integers.

This checks a complete, finite arithmetic certificate for the remaining exceptions, but does not assess rank of arbitrary perturbations or constitute independent external review.
