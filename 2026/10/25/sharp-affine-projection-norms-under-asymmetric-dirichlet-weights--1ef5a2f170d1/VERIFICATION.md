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

# Reproducibility and verification

Run `python checker.py` with Python 3 and `mpmath`. No other files or data are needed. When checked, the script printed `PASS 394 deterministic assertions; universal theorem depends on supplied analytic proof.`

Checks include exact rational evaluations of integer-parameter incomplete-beta integrals, exact reproduction and symmetry of the degree-one Dirichlet kernel, monotonicity comparisons for nonintegral weights, numerical checks of the three asymptotic regimes, and direct two-coordinate kernel integration with strict interior-versus-vertex comparisons.

The mathematical proof of the all-parameter inequalities is entirely in `RESULT.md`, using Dirichlet moment identities, positivity of the weight, a strict conditional-Jensen coupling, and explicit convergence theorems. The computation does not establish or claim to establish an infinite-dimensional or all-real-parameter theorem. The code uses no unprovided external files, randomized input, or network access. Bibliographic priority and independent validation remain unperformed.
