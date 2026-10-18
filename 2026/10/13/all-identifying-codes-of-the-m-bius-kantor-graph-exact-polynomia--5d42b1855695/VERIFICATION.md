---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-17.md",
      "INDEPENDENT_AUDIT_2026-10-17.json"
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

For GP(8,3), with 16 vertices, graph adjacency specified by u_i u_{i+1}, u_i v_i, v_i v_{i+3}, closed-neighborhood signatures are nonempty and distinct exactly for identifying codes. Every subset is one of 65536 16-bit masks. A fresh independent enumeration of all 65536 masks produced 16229 identifying codes and coefficients 584,3840,5440,3888,1780,560,120,16,1 at sizes 8–16, zero below 8. Using the graph edges independently, a graph-automorphism enumeration recovered order 96 and orbit partition of 584 min codes into sizes 2,6,24,24,48,48,48,48,48,48,48,96,96, agreeing with the actual orbits.csv. Source verify.py also derives the 136 closed-neighborhood/symmetric-difference hitting constraints; 88 smaller 4/6-size constraints dominate all 48 eight-size ones. This is exhaustive finite certification for this graph, not an infinite-family claim.

## originality

PASS

Best-of-knowledge originality limited to the specifically unpreempted structural/classification content. There is no implication from the broader published structural incidence facts or an automorphism group alone to the exact 584 minima/13 orbit decomposition without analyzing every identifying subset.

## value

PASS

Identifying codes are standard selected-landmark locating structures for a highly symmetric, smallest cubic 16-vertex bipartite graph. A full size distribution, extremal count and classification into thirteen full-automorphism orbits are mathematically motivated exact invariants usable for small-graph benchmarks and symmetry tests, beyond an isolated optimum value. The finite full census is a complete proof for the explicitly fixed graph.

The dated certificate retains the supplied scientific assessment, sources and limitations.
