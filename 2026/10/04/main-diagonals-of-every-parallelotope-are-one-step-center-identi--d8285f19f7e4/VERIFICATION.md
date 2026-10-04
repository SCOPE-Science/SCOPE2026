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

The proof is analytic. In normalized cube coordinates, permutation symmetry reduces the dual MinCE problem to one parameter \(y\). Differentiating its strictly concave log-determinant yields
\[
(n+1)t y^2+(1+t^2)y-(n-1)t=0.
\]
Substitution into the published exact center map reduces the next-coordinate numerator to the negative of this polynomial, so the next center is exactly the cube center.

`verify.py` is a finite numerical replay of the closed-form root and cancellation for several dimensions and positive and negative interior starts. It uses only the Python standard library and prints `VERIFY_OK` on success. Finite replay is not an exhaustive proof and is not used to justify the universal quantifiers.

The second iteration uses only the exact symmetry fact that the unique minimum-volume covering ellipsoid of \(\operatorname{conv}\{\pm e_i\}\) is \(B_2^n\). Affine covariance then transports the result to every full-dimensional parallelotope.

No verification is claimed for approximate MinCE solves, floating-point implementations, or off-diagonal starts.
