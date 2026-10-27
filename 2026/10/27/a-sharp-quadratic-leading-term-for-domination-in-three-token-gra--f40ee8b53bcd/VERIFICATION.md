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

Run `python3 verify.py` using the Python standard library. `check_output.json` is the output of a successful local execution: every selected witness dominates the entire explicit three-token graph for \(4\le n\le18\), and the brute-force Mantel checks cover all simple graphs with \(2\le n\le6\). The verifier calculates adjacency by set symmetric difference and by checking that the exchanged vertices belong to opposite parts of the base bipartite graph.

The independent calculation checks finitely many inputs, not the quantified theorem for all \(n\). For the infinite statement, review the pair-projection lower bound, the elementary Mantel proof, and the three-layer upper construction in `RESULT.md`. The calculations do not claim exact domination numbers or exhaustive historical priority.
