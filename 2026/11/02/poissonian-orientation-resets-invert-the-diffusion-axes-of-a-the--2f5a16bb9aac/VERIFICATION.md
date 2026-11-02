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

# Verification of the analytical claim

Run `python3 VERIFY.py` with Python 3's standard library. This tests two independently coded representations of the exact compensated-renewal covariance at 500 rational reset-rate inputs, computes 288 generic-mobility rational matrix identities, checks the exact maximizer and a narrow rational bracket for the unique positive axis-switching root, and makes 450,000 simulated complete renewal excursions. An additional direct discretized-path simulation at three reset rates checks full 2D anisotropic-body covariances, including the off-diagonal component.

The independent angular increments and independent translational Gaussian increments are sampled separately; the direct path simulator does not sample from the claimed closed-form covariance law. Monte Carlo tolerances are explicit and deterministic under the published seeds. Numerical experiments cannot certify uniqueness of the positive root for all real reset rates, which is instead proved by a strictly positive derivative of the defining cubic. The regeneration theorem, renewal-law moment bounds, and limiting covariance are established analytically in RESULT.md.
