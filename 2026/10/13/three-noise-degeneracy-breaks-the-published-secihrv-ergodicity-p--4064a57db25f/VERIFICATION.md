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

The verification is algebraic and exact. The bundled checker reconstructs the three diffusion columns of system (4) with nonzero rational amplitudes, forms the covariance matrix \(A=GG^\top\), and confirms that the fifth and sixth coordinate vectors have zero quadratic form. This certifies that no positive uniform-ellipticity constant can exist for the displayed covariance.

The same checker implements the published Lyapunov form and evaluates it on points differing from the endemic state only in \(x_5\); the value is exactly zero for arbitrarily large positive displacement. It also instantiates the Eq. (50) level set with fixed constrained coordinates and arbitrarily large positive \(x_3\) and \(x_5\), confirming that the purported ellipsoid is unbounded.

The package does not test existence, uniqueness, irreducibility, Hörmander brackets, or support properties of the full diffusion. Those remain outside the claim.
