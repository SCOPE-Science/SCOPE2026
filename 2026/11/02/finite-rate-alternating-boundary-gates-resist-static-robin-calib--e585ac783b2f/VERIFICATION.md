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

# Reproduction and boundaries

Run `python check_alternating_gates.py` with a standard Python installation containing NumPy. The checker constructs a two-state nearest-neighbor walk approximation with rate \(D/(L/N)^2\) on interior edges, reflecting-boundary rate \(2D/(L/N)^2\), Markov gate flips at rate \(\kappa\), and state-specific absorbing endpoints. It solves separate transient linear systems for lifetimes and left-exit probabilities and compares to the exact formulas for four physical parameter settings, two grids, and three starting positions per grid (24 comparisons of both observables). It additionally tests the two Robin calibrations for six positive rates.

The source-free original execution reported `PASS`, with maximum absolute lifetime error \(0.0008253853237484843\) and maximum absolute splitting error \(0.00025034048702898826\). The finite-mesh approximation is not an infinite-dimensional proof; full correctness instead follows from the backward-equation derivation in `RESULT.md`. This package does not include independently audited evidence or an external scientific certificate.
