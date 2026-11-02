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

# Reproduction and limitations

The self-contained analytical derivation and the exact rational three-dimensional example are in `RESULT.md`. Run `python CHECKER.py` with NumPy and SciPy installed to independently compare the closed signed-area rate against the matrix-exponential covariance solution and exercise the generic interpolation construction for dimensions three and four. The checker passed when run from the package staging path.

The proof of the infinite family uses exponential Chebyshev zero counts and analytic positive-definite perturbations. Numeric interpolation at finitely many dimensions is confirmatory only; it cannot certify all dimensions. The theorem does not claim unknown historical priority as independently established. Exact zeros in the three-dimensional example are algebraically specified, not inferred by root-finding.
