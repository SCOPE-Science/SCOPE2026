---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-30.md",
      "INDEPENDENT_AUDIT_2026-10-30.json"
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

An induced horizontal edge consumes one row and two columns, and a vertical edge consumes two rows and one column; distinct edges cannot reuse any consumed coordinate because an endpoint would be adjacent to an endpoint of another edge. Conversely disjoint coordinate packets yield induced matchings. Choosing ordered row/column coordinates and pairing gives exactly m!n!/[2^(h+v)h!v!(m-h-2v)!(n-2h-v)!], with h+2v<=m and 2h+v<=n. Existence of h,v for t=h+v reduces to max(0,2t-n)<=v<=min(t,m-t), giving t<=min(m,n,floor((m+n)/3)). In a strong total cover selecting vertex set X, unselected U, required internal edges and one crossing edge for each isolated U vertex force cost>=|V|-|U|+|E(G[U])|+isolates(U). Each nontrivial component contributes <=1 to |U|-edges-isolates; one edge per component is an induced matching. Equality yields the known general minimum |V|-alpha_ind. For the two-row family n>=4, equality forces two disjoint induced K2 components in different rows with four distinct columns and no U isolates; choosing two disjoint column pairs gives binomial product. For width 2 and 3, enumerate U induced path and isolates, obtaining 8 and 45. Independent raw-graph enumeration confirms six polynomial instances plus two-row n2..7 cover counts, but infinite proof is combinatorial.

## originality

PASS

Aprile–Ferrarini 2026 establishes the general strong-cover/maximum induced matching identity; this is correctly treated as antecedent, not a novel theorem. The new work is the full two-parameter induced-matching enumerator and exact minimum-cover multiplicities for R_{2,n}, not generic covering duality. Other available results treat matching bounds, Hamming graph homology or complete bipartite hosts, without the same polynomial. Historical risk remains for an older rook-graph induced 1-regular-subgraph enumerator.

## value

PASS

Rook graphs and induced matchings are canonical in extremal and covering graph theory. A uniform all-coefficient formula solves more than a maximum bound; the sharp two-row minimum-cover census identifies a structural rigidity transition and exceptional small widths. These exact counts are natural invariants relevant to the newly formalized strong-total-cover problem, not arbitrary parameter slices.

The dated certificate retains the supplied scientific assessment, sources and limitations.
