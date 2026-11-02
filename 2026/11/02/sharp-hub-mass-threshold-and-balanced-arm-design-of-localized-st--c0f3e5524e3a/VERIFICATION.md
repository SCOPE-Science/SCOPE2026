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

The statement concerns a dimensionless generalized stiffness–mass eigenvalue. The infinite chain's upper band edge is \(\lambda=4\). Reproduce the finite numerical checks with \`python3 verify.py\`, using Python, NumPy and SciPy. The program independently constructs the Laplacian matrix and diagonal mass matrix, checks the number of eigenvalues above \(4\), tests exact rational thresholds at equality, compares balanced and most unequal top eigenvalues, and checks the arm transfer equation at the numerically determined root.

Recorded diagnostics: 218 edge checks, 1308 mode-count comparisons, 254 balanced/extreme checks, 616 root comparisons, and 24 long-arm convergence checks. This program is only a finite diagnostic suite, not an exhaustive verification of all integers and continuous mass ratios. The complete infinite claim is supported by the Schur complement, strictly decreasing scalar junction function and strictly decreasing discrete marginal increments proved in RESULT.md. No independent validation has been performed.
