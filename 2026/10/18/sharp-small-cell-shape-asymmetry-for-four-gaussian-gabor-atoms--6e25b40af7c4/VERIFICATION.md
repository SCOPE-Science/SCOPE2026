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

The executable `verify.py` uses SymPy for a symbolic four-by-four determinant identity and mpmath with 65 decimal digits for seven independent normalized coherent-kernel Gram determinants. It also reproduces the unique positive scalar root numerically, tests five shrinking-cell parameters, verifies the square and elongated scaling regimes, and tests three direct aspect-ratio grids. These finite checks ran successfully against the exact files included with this result.

The theorem's infinitely many parameter values, the supremum over all aspect ratios, uniqueness of the scalar maximizer and the convergence of maximizing shapes are established analytically in `RESULT.md`; no computation is presented as exhaustive proof. Exact coefficients depend on the specified Weyl and Gaussian normalization.
