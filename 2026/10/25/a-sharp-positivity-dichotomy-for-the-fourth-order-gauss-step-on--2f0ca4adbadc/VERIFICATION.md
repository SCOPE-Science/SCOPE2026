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
# Verification of the weighted three-site Gauss positivity classification

Run `python artifacts/verify_gauss_three.py` with `sympy==1.14.0` installed. Successful execution produces a deterministic `VERIFY_OK` confirmation.

The script symbolically verifies the characteristic polynomial and polynomial quotient in the proof, extracts the three off-diagonal numerator expressions, constructs the zero-sum Laplacian inverse, and checks its off-diagonal signs against the stated Green formula. It then constructs 672 exact rational Gauss matrices from 112 connected nonnegative conductance triples at six rational timesteps and checks direct inverses, row sums, symmetry, diagonal signs and off-diagonal numerator signs. A symbolic weighted-path calculation tests the sharp positive root and signs on each side.

The infinite parametric result is established algebraically in `RESULT.md`, not by finite samples, numerical approximations or the number of tests. External independent audit is not performed. No claim about stage positivity, nonlinear systems, larger graphs or floating-point implementations is verified.
