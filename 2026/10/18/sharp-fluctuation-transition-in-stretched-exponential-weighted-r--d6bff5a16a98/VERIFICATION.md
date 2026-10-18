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
Run `python3 verify.py` with a standard CPython interpreter; it requires no third-party packages. The exact rational calculation enumerates every possible parent assignment for tree sizes three through seven with deterministic weights \(w_j=j\), computes total path length directly, and independently compares its exact variance with the martingale/variance recurrence. It also computes the exact-recursion variance for the stretched-exponential attachment model at \(\beta=0.55\), \(\beta=2/3\), and \(\beta=0.8\), at sizes 10,000 and 100,000. All enumerative assertions passed during packaging.

These finite checks **do not** prove infinite limits or asymptotic optimality. The analytic proof in RESULT.md establishes the \(2/3\) transition by deriving the asymptotic innovation variance and controlling the martingale remainder. The approximate large-size ratios converge slowly near the phase transition and are diagnostic only. No independent audit has been performed.
