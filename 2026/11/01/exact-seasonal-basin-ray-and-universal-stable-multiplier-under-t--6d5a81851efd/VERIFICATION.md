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

The analytic verification is the four-step proof in `RESULT.md`: projective scalar monotonicity, reciprocal-abundance affine integration, triangular Floquet spectrum and global boundary attraction. The attached `verify.py` independently integrates a time-varying example and compares the predicted two multipliers with finite-difference full-system annual Jacobian eigenvalues. This numerical test is not a proof for infinitely many coefficient functions. The result remains to be audited independently.
