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

The standalone Python 3 standard-library file `artifacts/verify.py` implements the finite-tree polar weight recurrence directly, with finite depth chosen larger than every tested iteration. It independently compares transformed root weights with the closed formulas, verifies the exact Euclidean/operator root-column error, tests every listed rate regime and tuned cancellation, and checks the all-equal-tail boundary. A deterministic run completed with **PASS 6800 deterministic scalar checks**.

The mathematical proof is analytic. The exhaustive algebra for the finite set of branches yields the log-mass recurrence, then a summable-forcing argument proves the infinite-iteration limit and asymptotic constants for arbitrary positive parameters. Finite-depth tests and a finite number of floating-point samples do not establish universal continuum inequalities or infinite-dimensional convergence. No independent mathematical audit has been performed.
