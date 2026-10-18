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
# Reproducibility and limits

Run `python check_ball_quadratic.py` with Python 3, SymPy, SciPy and NumPy. The reference execution passed 308 checks: exact integrated reproducing identities in dimensions 2–5 and multiple rational weights, exact center sign factorizations, independent quadrature of beta integrals, Gamma absolute-deviation coefficients, and finite-dimensional sampling sanity checks. All stochastic checks use the explicit fixed seed in the source.

These tests are finite and cannot establish a dimension limit. The analytic evidence is the explicit polynomial kernel, the Beta–Gamma and spherical Gaussian couplings, convergence in \(L^1\) uniform in radius, and optimization of the convex limiting radial function in RESULT.md. The checker does not independently certify the entire proof, bibliographic novelty, or any claim beyond the specified scope. Independent audit has not been performed.
