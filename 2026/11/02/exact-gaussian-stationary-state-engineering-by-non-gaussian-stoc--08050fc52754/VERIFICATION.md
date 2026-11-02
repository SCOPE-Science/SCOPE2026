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

# Verification notes

Run `python verify_gaussian_reset.py` with NumPy, SciPy, and SymPy. The program was executed from the supplied standalone script and printed `PASS: 71 deterministic Gaussian quadrature, generator, matrix and symbolic checks`.

Checked identities: source-density normalization, predicted source mean and second raw moments, exact steady-state generator equations for all bivariate monomials up to degree five, minimum quadratic tilt, stationary lag-covariance derivative, a rank-deficient semidefinite boundary, the isotropic minimizer, and unattained threshold examples. Two positive-definite numerical test systems include an unsymmetric stable drift with correlated diffusion.

These checks are finite corroboration. The all-dimensional result rests on explicit Gaussian differentiation, universal polynomial nonnegativity, Markov resetting resolvent uniqueness, and an exact derivative sign argument. No formal proof assistant or independent scientific validation was used.
