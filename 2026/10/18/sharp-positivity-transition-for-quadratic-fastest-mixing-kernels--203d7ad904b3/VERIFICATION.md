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

# Reproduction and scope

Run `python verify_quadratic_biclique.py` from this package with Python 3, NumPy and SciPy available. The program prints the assertion count and aborts on any failed test. On the prepared package it reported 14,188 passing assertions. Assertions cover rational coefficient formulas and spectral values for \(2\le p\le18\) and \(p\le q\le100\), independent SciPy linear programming solutions for these instances, full symmetric-Laplacian matrix construction for \(2\le p\le7\) and \(p\le q\le13\), and a two-factor comparison for selected larger imbalances.

Exact formulas are proved in RESULT.md; numerical programs alone cannot establish the theorem for arbitrary graph sizes. No independent audit or external validation has been performed. The stated code dependencies are NumPy and SciPy, not a specialist proof environment. The scientific result optimizes a fixed family of quadratic polynomial kernels, not every Markov kernel allowed on the squared graph.
