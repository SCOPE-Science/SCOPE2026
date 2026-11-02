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

For n≥2, a chosen rook-vertex set induces a forest exactly when its K_{n,n} edge set is a linear forest: a degree-three vertex would give a line-graph triangle and any K_{n,n} cycle would survive. At size 2n−1, a linear spanning tree is an alternating Hamiltonian path, uniquely described by a pair of permutations, giving (n!)². Cutting a path edge and joining opposite-component endpoints gives 1 replacement at even cuts and both odd boundary cuts, and 3 at the n−2 interior odd cuts: degree 4n−5. Two neighbors of P are adjacent exactly when they share removed or added edges, giving 3(n−2)+binom(2n−1,2)=2n²−5 triangles through P. Legal prefix reversals and a final suffix-three reversal generate all row and column permutations, hence connectivity. Independent direct edge-set enumeration recovered graphs for n=2,3,4 with vertices 4,36,576, degrees 3,7,11, edges 6,126,3168 and triangles 4,156,5184; this is bounded corroboration, not proof of all n.

## originality

PASS

Best-of-knowledge original versus closest accessible statements, with real Resultary and primary-source comparisons; failed search is not novelty proof and uninspected plausible literature is recorded, not declared noncovering.

## value

PASS

The natural maximum induced-forest/feedback-vertex-set solution space of a balanced rook graph is not described by its scalar optimum alone. Showing all optima connected by size-preserving one-cell exchanges, with exact universal degree and triangles, supplies a structural reconfiguration invariant and benchmark; it is not a routine computation of only a tiny example.

The dated certificate retains the supplied scientific assessment, sources and limitations.
