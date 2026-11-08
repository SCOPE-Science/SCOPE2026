---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-02.md",
      "INDEPENDENT_AUDIT_2026-11-02.json"
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

For compact intrinsic graph with one edge L and m>=2 equally short edges s<=L, the long+one-short circle is isometric: traversing any other arm does not shorten its distances. Mapping each off-circle center to its corresponding point of the selected short edge cannot enlarge distances to the circle; p circle arcs force radius q=(L+s)/(2p). For L>=(p-1)s, exact long-edge centers t_j=(L-(p-1)s)/(2p)+j(L+s)/p cover the entire long edge and all short arms through A or B. For L<(p-1)s, q<s/2; any off-circle center covers <2q of the circle, forcing all p equality centers onto it, but an omitted short-arm midpoint remains distance s/2>q. Compactness yields strictness. This addresses real lengths, all p>=1, equality boundary and all edge interiors. Recomputed independently with exact rational endpoints and obstruction identities; the 344-case/414723-check package log alone was not used as proof.

## originality

PASS

Best-of-knowledge after comparing the exact claimed quantifiers and mathematical implication with original papers, full relevant primary sections, and semantic published-finding searches. Positive evidence of independent coverage was not found; negative searches do not establish priority. Tamir 1987 full text was inaccessible via OA/preprint search and authorized Oxford request returned vpn_disconnected (job bea59b9cb1ec9ffd0fb7fe305720c54d). Its abstract alone cannot rule out an equivalent special case or example; residual historical-priority risk, not an automatic originality failure.

## value

PASS

A sharp equality/strictness threshold for the natural isometric-cycle lower bound on nontrivial metric multigraphs, stable under arbitrary extra parallel equal arms, gives precise structural information beyond generic p-center algorithms. The exact threshold L=(p-1)s and unrestricted center placement are useful for metric network location; it does not purport to solve the exact strict-side radius.

The dated certificate retains the supplied scientific assessment, sources and limitations.
