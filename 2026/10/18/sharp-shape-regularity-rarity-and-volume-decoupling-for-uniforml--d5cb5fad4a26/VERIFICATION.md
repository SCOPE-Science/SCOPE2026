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
# Reproducibility and scope

Run `python verify.py` with Python, NumPy and SciPy installed. The executed checker tests exact rational covariance identities in dimensions \(2\) through \(8\); a reproducible direct simulation of the uniform-query length-bias transformation; one-dimensional Fourier inversion against a Gamma-ratio density identity; rational three-dimensional polytope-volume decomposition; and covariance determinant/rare-event constant consistency. The complete source code is embedded in the same package.

The program completed with all tests passing. The analytical steps establishing infinitely many depths use the classical multidimensional local limit theorem under verified nonlattice, nondegeneracy and spread-out conditions. Simulations and finite-dimensional checks are supporting diagnostics only. The probability is annealed in both query and random cuts, and the result does not establish fixed-query or growing-dimensional statements. Publication priority has not been independently audited.
