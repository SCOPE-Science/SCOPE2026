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

# Reproduction notes

Install Python 3, `mpmath`, and `sympy`. Run `python verify_regular_polygon_affine.py` from the directory containing that file. The script evaluates the exact perimeter formula, integrates the signed kernel independently edge by edge, checks covariance and sampled strict vertex dominance, and establishes the three residue-class Laurent coefficients by symbolic Taylor expansion. The output must terminate with `ALL_REGULAR_POLYGON_AFFINE_PROJECTION_CHECKS_OK`.

The formula is proved for every integer \(n\ge3\) in RESULT.md; the finite sampling of \(3\le n\le110\) is not its proof. The remaining asymptotic error is justified by analyticity in the three fixed residue branches, not by numerical extrapolation. Zero sets of the affine kernel have arclength measure zero, and input sign-extremizers are only specified up to null sets and global signs.
