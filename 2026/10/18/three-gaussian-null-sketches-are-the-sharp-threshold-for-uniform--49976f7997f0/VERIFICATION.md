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

# Mathematical verification

The proof reduces every Gaussian \((n-1)\)-row null vector to \(v\propto A^{-1}u\) for an isotropic random unit vector \(u\). The exact independent beta coordinates \(T_j\) yield the identity \(R_{\kappa,K}=\kappa^2/[1+(\kappa^2-1)\max_jT_j]\). The near-zero density of that maximum is proportional to \(t^{K/2-1}\), so the inverse-\(q\) moment is finite exactly for \(K>2q\). Dimension three further reduces to a maximum of independent uniforms and yields \(K/(K-2)\) exactly. These are the analytical certificates of the stated claim.

`verify.py` uses only the standard Python library. Executing `python3 verify.py` produced:

```
VERIFY_OK exact_fraction_witness=1 exact_n3_formula_quadratures= 15 limit_checks=3 threshold_integrals=4 random_matrix_sketches=105000 mc_mean= 2.1289949 theory= 2.1109245
```

The cross-product identity was checked directly using both Gaussian rows and their products with the diagonal matrix. An exact integer-matrix example produces relative squared residual \(5\). Fifteen quadrature comparisons check the three finite-contrast formulas; independent Gaussian-matrix trials check the distributional construction. Numerical checks are **not** proofs of the all-dimension, all-contrast moment cutoff.

The theorem assumes independent real Gaussian sketches, exact unit null vectors, an equal-high-singular-value population, and exact comparison using unsketched residuals. It does not validate any particular Krylov solver, numerical SVD implementation, or optimal runtime strategy. Independent audit has not been performed.
