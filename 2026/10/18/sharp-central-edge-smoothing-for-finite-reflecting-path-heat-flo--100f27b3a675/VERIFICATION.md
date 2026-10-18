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

Run `python check.py` using Python 3 with NumPy and SciPy installed. It reconstructs vertex and edge Laplacians directly, checks the exact gradient intertwining and row norms against independent matrix exponentials, separately evaluates Dirichlet spectral formulas, checks row unimodality, tests the sharp Bessel time optimizer and sample diffusive limits. The captured result is **PASS assertions 4029**.

Finite tests use sizes 2 through 16 and several positive times; additional sizes 50, 100 and 200 appear in diffusive scaling checks. Floating-point comparisons use stated explicit tolerances. The tests neither prove infinite-size limits nor replace the argument in RESULT.md. The exact theorem is proved symbolically using tridiagonal operators, total nonnegativity, a symmetric Gram representation, the cycle-image heat equation, Bessel calculus and dominated convergence. Independent audit has not been performed.
