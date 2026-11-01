---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-31.md",
      "INDEPENDENT_AUDIT_2026-10-31.json"
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

Reconstructed Ehrenfeucht–Fraïssé equivalence of adjacency-only rook graphs R_{a,b}=K_a□K_b for every q>=1. If both factor sizes agree after q-truncation up to swap, Duplicator prolongs separate partial bijections on row/column coordinate values through all q moves, preserving equality and edge relation. Conversely rank2 existence of a nonedge distinguishes 2D factors from complete cases; for rank s>=3, s-clique existence detects max(a,b)>=s, while universal requirement of s−2 common neighbors for every edge detects min(a,b)>=s. Complete cases are counted by existence of distinct vertices, handling q=1,2 explicitly. Therefore exact q-type count is q(q+1)/2 and largest least rook-family representative is q². Independent recursive EF game checks passed 55 graph pairs at q=1 and q=2 and 21 pairs at q=3; the all-q proof is symbolic.

## originality

PASS

Best-of-knowledge: adjacency-only two-factor Hamming/rook graphs are natural; standard finite-graph EF theory and Hamming structure are prior but do not provide the family-specific all-rank cutoff classification and type count in checked material. Resultary related logical-depth profiles concern different graph classes. An elementary folklore result remains possible.

## value

PASS

Rook graphs are a canonical family of finite 2-factor Hamming graphs and line graphs of K_{a,b}. The adjacency language hides the coordinate sorts; exact recoverable dimensions at each FO quantifier rank, type count q(q+1)/2, and sharp least-representative order q² give a complete family-specific logical-complexity invariant, not an arbitrary finite example.

The dated certificate retains the supplied scientific assessment, sources and limitations.
