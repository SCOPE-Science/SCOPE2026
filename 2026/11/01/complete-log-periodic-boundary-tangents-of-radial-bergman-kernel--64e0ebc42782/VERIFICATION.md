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

# Verification and reproducibility

The analytic proof gives a uniform moment expansion, a phase-uniform Riemann-sum limit, Fourier preservation of the profile's period group, and injectivity after scalar normalization by uniqueness of Laplace transforms. These four steps prove the infinite-dimensional statements. No finite truncation is treated as a proof of a full-kernel identity.

Run `python3 verify.py` in an environment with the version of `mpmath` specified by `requirements.txt`. The script checks an exact sinusoidal specialization, including beta moments and phase-dependent finite kernel sums. It reports the numerical approximation errors and exits with a nonzero status if any consistency tolerance fails. This is a numerical supplement, not an independent audit or a formal certificate.

Scientific limits: fixed positive continuous periodic profile, fixed exponent above minus one, right-half-plane scaling, and usual normalized planar area. No claims are made about arbitrary measurable nonperiodic weights, zero distributions, or extensions to several complex variables. Independent audit has not been performed.
