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

# Reproduction and limits

Run `python verify.py` with Python, SymPy, NumPy and SciPy available. The checker is self-contained: it constructs the individual-edge grounded Laplacian rather than trusting the three-class eigenvalue formula as an input. The saved output in `verification_output.txt` is from a successful execution of this same code.

The checker verifies exact rational weighted-spanning-tree determinants, budget identities, and full unrestricted edge-by-edge KKT gradients for 42 combinations of graph size \(4\le n\le9\) and positive price values that include both sides of, and equality at, \((n-1)/(n-2)\). It additionally runs 240 asymmetric feasible comparisons and 40 independent constrained optimizations in the full edge-variable space, for graph sizes four through seven.

**Limits:** Finite tests and numerical solvers are not a proof of global optimality. The global result instead relies on the strict concavity of the log determinant, injectivity of the edge-to-grounded-Laplacian map, the exact Laplacian eigenspace decomposition, and exact verification of all KKT inequalities, as developed in `RESULT.md`. Numerical optimization tolerances do not certify an infinite domain. Independent audit: not performed.
