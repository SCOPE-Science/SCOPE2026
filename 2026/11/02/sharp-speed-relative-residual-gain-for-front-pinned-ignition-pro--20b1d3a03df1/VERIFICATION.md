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

# Reproducibility

The proof is self-contained in `RESULT.md` and establishes the exact norm and the limiting constant without relying on numerical sampling. Run `python3 verify.py` (standard Python 3 library only) to reproduce the root locations, norm values, derivative comparisons and limiting coefficient.

Observed checker output: 3,139 supplementary checks passed for eleven integer reaction orders and the limiting scalar equation. Derivative comparisons use finite differences, and the limiting integral uses deterministic composite Simpson quadrature. These calculations verify numerical illustrations; no finite numerical output proves uniqueness or the limit, which are instead supplied by the stated derivative and monotonicity arguments.

The result does not independently test a discretized Chebyshev collocation matrix, a nonlinear residual-error bound, or unweighted forcing norm optimality. The independent audit channel remains unperformed.
