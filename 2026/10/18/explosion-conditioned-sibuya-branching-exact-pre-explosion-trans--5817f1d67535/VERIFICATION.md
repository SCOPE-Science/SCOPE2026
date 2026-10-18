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

# Verification of the explosion-conditioned Sibuya transform

Run `python verification.py` after installing the `mpmath` Python package. The script was executed from the final candidate's exact source code. It checks the pgf normalization, the density-based one-particle coefficient, the conditional-mean derivative, the independent branching-semigroup expression, the exact square-root mixture, and convergence of the two next-order coefficients on three successively smaller \(u\) scales for five \(\alpha\) values, three \(T\) values, and three positive Laplace arguments. The execution passed 453 finite high-precision checks.

The limiting \(\Gamma(\alpha,1)\) transform, three-regime expansion, and measure-representation threshold are established analytically in RESULT.md. No numerical finite test alone proves these statements. The computation uses arbitrary-precision floating-point arithmetic, not a formally certified interval arithmetic proof. Only the specified family and bounded Laplace arguments are covered. Independent audit has not been performed.
