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

Run `python3 verify.py` using a Python 3 standard-library interpreter. The verifier performs four exact-rational beta/binomial identity checks with \(\kappa=2\), checks monotone ordering across eight even sketch dimensions, checks the exact quadratic-form eigenvalue trace and determinant at \(\rho=3/4\), compares large-sketch approximations at two sizes and two angles, and simulates sixty thousand independent Gaussian sketches for each of four parameters. Its actual completed output ends in `VERIFY_OK`.

The exact-rational checks apply to those parameter values only, and the Monte Carlo tests are finite statistical diagnostics. The infinite-dimensional-in-sketch-size asymptotic and all-real-correlation exact probability are established by the analytic proof in `RESULT.md`, not by exhaustive computer enumeration. No external or independent audit has been performed.
