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

The theorem is proved analytically in `RESULT.md`. To reproduce the finite auxiliary checks run `python coupon_checker.py` with Python 3 and only the standard library. A run passed 90 check families: exact finite-support coupon enumeration, KKT and normalization identities, \(L=2\) optimal design, and finite-budget approaches to the sharp predicted limit. These finite checks cannot prove infinite-dimensional or asymptotic statements and are not described as doing so.

The variance of the one-hot isotropic sketch norm is infinite (indeed its second moment is infinite); this does not affect the almost-sure coordinate-projection construction and the Hilbert--Schmidt error formula. The optimizer on the closed simplex is not itself full-support isotropic. There is no independent mathematical audit and no guarantee against an older equivalent weighted-coupon result.
