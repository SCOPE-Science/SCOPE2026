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

# Reproducibility and verification

The algebraic proof in `RESULT.md` uses an exact slice integration, conditional beta/Dirichlet moments, a determinant-one shear, a strict elementary ratio inequality, and Stirling's estimate. No infinite statement is inferred from finite enumeration.

Run `python check_split_isotropy.py` with Python 3 and packages `scipy` and `numpy`. The checker works with rational fractions for second moments and covariance determinants, and uses numerical convex-hull volumes only on independent, small-dimensional 0/1-vertex descriptions.

Observed output:

`VERIFY_OK exact_covariance_determinants=29 convex_hull_volumes=15 strict_ratio_cases=498`

The finite checks cover parameter pairs through dimension nine for exact covariance calculations, lower dimensions for convex-hull volume calculations, and a finite range of adjacent-ratio instances. The critical general statements remain dependent on the written proof. No external independent audit was performed.
