---
{
  "schema_version": 1,
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-01.md",
      "INDEPENDENT_AUDIT_2026-10-01.json"
    ]
  },
  "lean_verification": {
    "status": "unknown",
    "evidence": null
  },
  "expert_attestation": {
    "status": "unknown",
    "evidence": null
  }
}
---

# Independent mathematical audit

## correctness

PASS

The proof was reconstructed from the frozen RESULT.md and checked against the actual exhaustive verifier for all bicliques of total order at most seven and cliques through K_8. In a complete bipartite graph, every non-tree edge of a DFS tree must join ancestor and descendant; because every cross-part pair is an edge, this forces an alternating spine, with surplus vertices of the larger part appearing as leaves at the terminal opposite-part spine vertex. The return-cut loads reduce to the displayed concave profiles g_i=i(a+b-2i)-1 and h_i=i(a+b+2-2i)-b-1; the leaf envelope is dominated by a spine cut, and rooting on the smaller side adds b-a to the competing profile and cannot improve the optimum. Maximizing the concave quadratic gives the balanced/intermediate floor formula until b=3a-2 and the endpoint formula from b=3a-1 onward, with the balanced odd parity correction. For K_n, every DFS tree is a Hamilton path and the cut load i(n-i)-1 gives floor(n^2/4)-1. The finite verifier is supporting evidence only; the all-parameter proof is structural.

## originality

PASS

The primary KLX paper was inspected in full for its definition and stated structural results; it introduces KLX/DTC and develops small-KLX structure, treewidth bounds and recognition, but no exact clique or complete-bipartite formula was located. Resultary searches under KLX, kissing-loop crossing, DFS-tree congestion, complete graph and biclique returned the audited record as the only exact hit. Classical spanning-tree congestion allows arbitrary spanning trees and therefore does not imply the DFS-restricted phase transition here.

## value

PASS

Cliques and bicliques are canonical benchmark families for a new DFS-congestion parameter. The exact formulas expose a nontrivial balance-to-imbalance phase transition and quantify the penalty imposed by the DFS constraint relative to ordinary spanning-tree congestion. This is a natural complete classification on fundamental graph families, not an arbitrary small-order census.

The dated certificate retains the supplied scientific assessment, sources and limitations.
