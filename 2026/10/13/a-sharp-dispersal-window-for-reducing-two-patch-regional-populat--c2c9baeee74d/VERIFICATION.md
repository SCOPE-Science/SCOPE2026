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

# Verification of the exact two-patch calculation

Run `python3 verify_ou.py` with Python 3 and no third-party packages. The expected output is:

`VERIFY_OK polynomial_derivative=1 polynomial_ratio_monotonicity=1 matched_noise_identity=1 rational_lyapunov_cases=288 exact_witness=1`

The script uses exact sparse multivariate integer polynomials to check the derivative numerator, the monotonicity numerator of the threshold ratio, and the matched-noise identity. It then solves 288 stationary Lyapunov systems over rational numbers and reconstructs the stated rational regional-variance formula; the exact witness has variance `49/50` at dispersal rate `1`.

The infinite-parameter proof is in `RESULT.md`: covariance existence is guaranteed by positive definiteness, monotonicity by positivity of every denominator factor, uniqueness by strict endpoint monotonicity, and the sharp bound by a strict positive polynomial. Rational spot checks do not prove these uniform statements, and neither stability of nonlinear ecological dynamics nor any independent external mathematical audit has been established.
