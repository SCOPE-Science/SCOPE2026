---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-07.md",
      "INDEPENDENT_AUDIT_2026-11-07.json"
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

Every induced P4 in the two-clique matching graph uses two vertices on each shore and one selected matching bridge as its middle edge. This proves the exhaustive cograph criterion: no full bridge, or selected shore size <=1, or precisely two whole matching pairs (induced C4). Combinatorial generating functions count the no-bridge choices, singleton-shore choices with their overlap correction, and double-bridge choices. Single-vertex extension maximality gives all two-bridge four-sets, a fully selected opposite clique plus one bridge singleton, or bridge-free orientations with exclusions when a=t or b=t. Hence exact M(z) coefficients and rook graph gaps, with endpoints t=3 and absent bridge-free contributions handled. Independent direct adjacency P4 and addition-maximality enumeration for small parameter triples confirms both coefficient arrays; finite checks are not the universal proof.

## originality

PASS

Brosse et al. 2020/2024 give polynomial-delay enumeration of maximal induced cographs on arbitrary graphs, and Cao provides general hereditary-subgraph enumeration algorithms; they do not state the all-parameter symbolic cardinality polynomials in material checked. Co-bipartite matching and matching-deleted complete bipartite graph names identify the same family; Resultary non-CIS pair count is a different invariant. Relevant full graph enumeration article was inaccessible this run, a residual risk.

## value

PASS

These are exact cardinality distributions of a natural hereditary class on a canonical connected graph family, not arbitrary small-instance counts. The exact boundary terms classify all inclusion-maximal subsets, while vertex-transitive rook graphs exhibit unbounded gaps in possible maximal-set sizes and asymptotic concentration.

The dated certificate retains the supplied scientific assessment, sources and limitations.
