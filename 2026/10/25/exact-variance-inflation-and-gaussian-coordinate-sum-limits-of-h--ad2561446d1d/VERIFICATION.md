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

The proof uses the original defining inequalities of the homogeneous cyclic chainlink polytope and a weighted inclusion--exclusion identity. A direct triangular integral supplies the previously uncomputed nonzero-tilt pair weight; the cycle matching characteristic equation gives an exact two-root transform. Taylor coefficients at zero imply the exact finite variance. Analytic dominance of the principal root proves the Gaussian limit, and the differentiable log-mgf proves the stated large-deviation law. The permissible real parameter boundary \(2\ell=a\) is included.

The standalone exact-arithmetic and numerical checker is `check_chainlink.py`, executed using Python 3 and NumPy. Successful output: `CHECK_OK matching_counts=32 exact_rational_moments=32 tilted_quadrature=3 monte_carlo=750000`. Its rational moment computation enumerates forbidden-edge matchings and integrates the second moment of each removed triangle independently of the eigenroot differentiation. The quadrature and Monte Carlo are numerical diagnostics, not mathematical certificates for arbitrary dimension.

Only the stated homogeneous-coordinate result has been reviewed. The prior zero-tilt volume identity and rank symmetry are credited. Equivalent results under different statistical-mechanical language have not been excluded exhaustively. Independent mathematical validation has not been performed.
