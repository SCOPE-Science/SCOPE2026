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

The standalone checker `verify.py` uses only Python's standard library. It constructs all orderings of the labeled vertices of every cluster graph with component orders given by integer partitions of the vertex count, for every size from 2 through 7. It tests, for all pairs of domain vertices, whether adjacency and nonadjacency are preserved by the one-step path shift, and checks the resulting counts against the proposed explicit formula. Four eight-vertex cluster graphs additionally test uniform and nonuniform components, including a nonexistence case. Total 47 instances.

Executed command: `python3 verify.py`.
Observed output: `VERIFY_OK cluster partial-automorphism nilpotents: 47 exhaustive configurations`.

Mathematical checks reconstructed without relying on the finite computation: a nilpotent partial injection of index equal to the vertex count is one spanning path; the induced-graph isomorphism is equivalent to shift-invariant adjacency; the minimum repeated-label separation forces the period; residue-count arithmetic gives the exact counts. No enumeration is offered as a proof for unbounded vertex counts. No independent external audit or certification has been performed.
