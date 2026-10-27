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

# Verification

Execute `python3 checker.py` using only the Python 3 standard library. The script solves the positive-definite circulant tridiagonal systems in exact rational arithmetic, verifies their residual equations, and checks both strict edge-orbit norm comparisons for each integer \(7\le n\le35\). It additionally derives the electrical-current columns directly from grounded graph Laplacians for both edge types at each size \(7\le n\le12\), without using the spectral factorization.

Expected completion line: `EXACT_SQUARED_CYCLE_OK finite_sizes=29 direct_graph_columns=12`.

The analytical proof independently establishes the inequalities for all \(n\ge36\). The finite certificate cannot justify any unenumerated size; the large-size argument covers those. The first asymptotic correction follows from summable alternating geometric Green-kernel tails, with their exact positive-entry counts. No independent mathematical audit has been performed.
