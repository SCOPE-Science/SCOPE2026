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
# Finite verification and its limits

The standalone source `verify_projection.py` was run with Python 3, NumPy and SciPy. Its checks passed: 1,960 exact rational identities between the rank-two characteristic polynomial and the event inequality; 76 comparisons of the dimension-four elementary CDF and independent angular quadrature across four anisotropy choices; 700 independent random full-dimensional matrix-compression eigenvalue computations; 24 Gaussian-direction empirical CDF comparisons; and six strictly ordered CDF threshold tuples over dimensions 3, 4, 6, and 9.

The tests verify the *projection* radius: an orthonormal numerical basis of the random hyperplane is constructed and the largest eigenvalue of its compressed ellipsoid support matrix is compared with the analytic two-by-two formula. They do not compute random central sections.

The proof in RESULT.md, not finite experiments or a numerical tolerance, establishes the general law, positivity of mixture coefficients, monotonicity and asymptotic limit. Historical originality is provisional and independent mathematical audit remains unperformed.
