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
# Verification and reproducibility

Run `python verify.py` using Python 3.8 or newer. No external Python dependencies are required. The program evaluates both recurrence maps directly, without preloading stored trajectories. It compares large-time vectors at \(t=100000\) against the formulas obtained from the adjacency Perron eigenvector on a single edge, triangle, and three-vertex path, with deliberately unequal initial infection probabilities. It also checks the exact quadratic coefficient difference, closed formulas for regular-graph degree values, and the exceptional full-recovery endpoint on two vertices.

All finite computations completed successfully. The worst relative discrepancy among the six numerical asymptotic checks is below \(0.00019\); this is consistent with subleading terms. These numbers do not prove uniform or infinite-time convergence. The analytical proof in `RESULT.md` supplies that conclusion by strict Perron-mass decay, transverse spectral contraction, and a one-dimensional asymptotic difference equation. No independent audit has been performed.
