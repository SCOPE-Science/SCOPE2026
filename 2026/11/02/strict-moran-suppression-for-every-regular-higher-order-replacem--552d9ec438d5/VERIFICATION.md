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

# Reproducible mathematical checks

The theorem is proved analytically by expanding the two possible mutant-count changes contributed by each hyperedge and identifying the exact sign of their total exponential drift. Edge cardinality at least three makes the sign strict when the edge meets both types. Finiteness and connectedness justify absorption and stopping.

Run `python3 verification/verify.py` from the package root, using Python standard library only. The script independently solves rational finite-state Markov systems for four edge families, tests every nonabsorbing configuration at \(r=1/2\), \(1\) and \(2\), checks \(486\) exact positive mixed-edge drift examples, and reconstructs the originating paper's \(N=4\) expression. The script is not a general machine proof: it corroborates the finite computations and formula only. No simulations are used to justify the infinite-family conclusion.

The equivalence and broader-literature assessment is limited to the explicitly read primary texts and searches documented in the self-review. Independent audit and independent validation are not performed.
