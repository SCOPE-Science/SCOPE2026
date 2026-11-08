---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-06.md",
      "INDEPENDENT_AUDIT_2026-11-06.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

For k=floor(1/φ), n≤k+1 implies every degree ≤k and every vertex with one active neighbor adopts, so connectedness forces full propagation before and after edge insertion. For φ>1/2, only degree-one neighbors of the single seed activate in the first step and cannot trigger further activation, so at most two active leaves are lost under one added edge; a star plus added edge between leaves attains loss 2. For φ≤1/2 and n≥k+2, the explicit gate tree starts full cascade through a degree-k vertex and degree≤2 path, while adding a single incident edge raises the gate to degree k+1, preventing any first adoption; loss n−1 is globally maximal. Checks address reciprocal thresholds and integer boundary cases; 25 independently simulated rational witnesses matched exact formulas. Proof is universal, not inferred from simulations.

## originality

PASS

Watts 2002 derives vulnerable degree floor(1/φ) and sufficient cascade concepts, but the inspected primary full text does not give the exact extremal single-edge inhibition loss, minimum graph order and φ=1/2 phase change. Other cited random-network cascade work considers different probabilistic aims; no stronger theorem implying this exact graph extremum found.

## value

PASS

A single positive tie can shut down almost every adoption below half-threshold but only two above it, a sharp and surprising structural counterexample to monotone effects of link addition. The explicit minimal network order and optimal construction are mathematically natural and interpretable.

The dated certificate retains the supplied scientific assessment, sources and limitations.
