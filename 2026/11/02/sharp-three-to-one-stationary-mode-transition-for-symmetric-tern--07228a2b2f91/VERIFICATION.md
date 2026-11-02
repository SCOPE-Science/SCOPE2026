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

Run `python checker.py` with Python 3, SciPy, and standard library packages. In the reviewed package the output was `PASS: 4677 exact and finite numerical checks`. The program uses `fractions.Fraction` to check exactly the stationarity of all test functions \(\mathbf1_{\{S=i\}}\prod_jW_j^{n_j}\) with \(0\le n_j\le5\) for six exact concentrations, checks the exactly evaluated variance \(2/[3(3a+1)]\), and applies finite quadratures and grid diagnostics on both sides of the sharp boundary. It is source code for diagnostics, not an independent audit.

The infinite-parameter proof is in RESULT.md, using Dirichlet integration by parts and strict log-convexity. Numerical quadrature is not used to infer absence of extra modes. There is no independent scientific audit or external formal certificate.
