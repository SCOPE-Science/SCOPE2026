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

The local reproducibility check runs `python3 verify_eop.py` without third-party dependencies, reproducing `VERIFIER_OUTPUT.txt`. It verifies all selected edges and every pairwise compatibility condition for explicit witnesses of sizes 12 and 24. A complete exact bitset search of the edge-compatibility graph, with a proper-coloring upper bound and an edge-transitivity reduction, proves no witness of size 13 or 25 exists. The checker visits 59 and 54,111 search nodes respectively.

Proof-critical preconditions: the two edges of a selected pair are compatible precisely when there is no *third* endpoint-joining edge; because hypercubes are triangle-free, incident selected edges are compatible. Every cube edge can be mapped to `(0,1)` by an automorphism. Each greedily constructed color class is independent, so it bounds maximum clique size; the reversed candidate recursion visits all possible cliques unless a sound bound excludes them. This justifies exact finite exhaustive proof, not a heuristic or timeout.

No general assertion about \(Q_n\) for \(n\notin\{5,6\}\) is certified. No independent audit or validation has been performed.
