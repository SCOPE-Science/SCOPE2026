---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-16.md",
      "INDEPENDENT_AUDIT_2026-10-16.json"
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

For every connected Ferrers/chain graph with 1≤d1≤…≤dp=q, a labelling has a unique first empty A index i∈{1,…,p+1} and unique last empty B index j∈{0,…,q}. Their local type words E/P/F characterize exactly which vertices must be empty/nonempty/free. Nested neighbourhoods collapse ALL empty A constraints to the earliest A-empty vertex, and ALL empty B constraints to the latest B-empty vertex. The two opposing colour-cover conditions are independent once (i,j) is fixed; inclusion-exclusion over missing colours gives Φ, and disjoint summation over (i,j) proves the full polynomial for all finite connected chain graphs. Independently implemented polynomial and literal adjacency union checks agree for 19 complete small Ferrers degree profiles p,q≤3, giving P4 coefficients 12,48,52,28,8,1 (weights3..8) and C4 coefficients 4,24,62,56,28,8,1 (weights2..8). The general proof is combinatorial, not extrapolated from enumeration.

## originality

PASS

Closest published full 2-rainbow enumeration is on complete multipartite graphs, which intersects the claim only at complete bipartite chain graphs. Other published connected-chain full polynomials count ordinary domination subsets or three-label Roman functions, and the total-2-rainbow algorithm counts optima under different constraints. They do not imply all four-label ordinary rainbow weight coefficients for arbitrary noncomplete Ferrers patterns such as P4. Best-of-knowledge originality PASS, allowing for historical unindexed chain/Ferrers formulations.

## value

PASS

The full weight enumerator is a natural graph-polynomial invariant for every connected chain graph, not merely its minimum. Its extremal-empty formula gives an explicit polynomial-arithmetic evaluation and distinctions among nonisomorphic Ferrers shapes; exact coefficients can be required by counting, randomized labeling, and generating-function research. It genuinely extends the complete-bipartite known case to the whole nested-neighbourhood class.

The dated certificate retains the supplied scientific assessment, sources and limitations.
