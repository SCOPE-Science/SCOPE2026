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

The analytical proof is in `RESULT.md`. Run `python verify.py` with NumPy and SciPy installed. The checker computes the known center-curvature roots independently using Kummer's confluent hypergeometric function and evaluates convolution derivatives using Gauss–Jacobi integration. The executed checks passed for five shape parameters, five critical fourth-derivative signs, ten off-critical central-curvature tests, ten derivative-mode scans, and four near-critical mode locations. The numerical ratio of the squared positive mode to the thermal gap approaches the analytically proved value 3.

The computer checks are finite and do not establish global uniqueness, exhaustive modality, or the limiting asymptotic. Those claims rest on the Riccati transversality, a proof of sign-variation of Gaussian convolution, and the heat equation/analytic implicit-function theorem. The critical curve and the convolution representation were known before this result; no independent external audit has been performed.
