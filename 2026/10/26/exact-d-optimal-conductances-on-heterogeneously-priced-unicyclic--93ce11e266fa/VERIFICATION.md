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
# Reproducibility checks

Run `python3 verify.py` using Python 3. The source has no third-party dependencies and produces the deterministic output reproduced in `checks.txt`.

The independent determinant calculation uses exact rational Gaussian elimination on the grounded weighted Laplacian. It matches the weighted spanning-tree polynomial for four five-vertex examples: equal cycle prices, a positive exceptional-price interior solution, the exact deletion boundary, and strictly above the boundary. Each example has a triangular cycle and a two-edge tree attachment. All exact budget equalities are separately checked. A seeded numerical sweep checks the allocation, budget and KKT equations for 168 other randomly priced unicyclic configurations (3 to 8 cycle edges and 0 to 3 bridges) and compares 6,720 independently sampled feasible allocations.

Sampling and determinant computations are finite correctness checks, not a proof of global optimality over all graphs and real-valued prices. The analytic matrix-tree/KKT/strict-concavity proof establishes that extension. External independent audit remains not performed.
