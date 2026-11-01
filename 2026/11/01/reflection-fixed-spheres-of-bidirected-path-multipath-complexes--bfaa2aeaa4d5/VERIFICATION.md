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

The theorem proof identifies directed-arc compatibility, all reflection orbit types, the precise band-graph fixed triangulation, and a uniform neighborhood-containment collapse. The rank-one integral reflection sign follows from the Euler characteristic of the fixed sphere and the independently established ambient sphere theorem.

Run `python verify.py` using Python 3 and only the standard library. The program directly enumerates every proposed fixed-orbit subset for \(n=3,\ldots,13\), reconstructs actual multipath legality from indegree/outdegree and directed two-cycle constraints, verifies predicted orbit adjacency and all Euler characteristics, checks 120 symbolic folding instances, and checks the empty boundary cases. The program printed `PASS` with 3,600 verified fold deletion pairs.

Finite enumerations do not constitute a proof for unbounded \(n\), and the independent audit remains unperformed. No claim is made about the full equivariant homotopy type of the ambient multipath complex or about other automorphisms.
