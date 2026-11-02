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

# Verification record

The proof derives the rectangular lifted GMRES least-squares matrix directly from \(B=L_1L_0^{-1}\), constructs its one-dimensional orthogonal residual subspace, computes the exact physical recovery functional, and evaluates the geometric-series limits. The full proof is in `RESULT.md`.

`verify.py` uses the Python standard library's `fractions.Fraction` and rational Gaussian elimination on normal equations, without assuming the claimed least-squares solution coefficients. Execution returned `PASS: 288 exact-rational independent normal-equation and recovery checks` for eight iteration counts and all 36 combinations of the listed positive rational parameters and coefficients. It tests both exactness resonance and nonresonance, and parameter values below, at, and above one.

The finite test cannot certify arbitrary parameter values, an unbounded number of iterations or the asymptotic limits; these follow analytically from the projection argument and geometric series. Physical and lifted residuals are distinguished throughout. No floating-point error bounds, generic higher-dimensional guarantees, or external independent validation are asserted.
