---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-15.md",
      "INDEPENDENT_AUDIT_2026-10-15.json"
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

For connected simple undirected G, degree leaders maximize neighbor count and eigenvector leaders maximize the positive Perron eigenvector. The unique-maximizer qualifier excludes tied cases. The packaged exact method computes p(t)=det(tI−A), q_i(t)=det(tI−A with vertex i removed), and q_i(λ)=p′(λ)x_i²/||x||² at simple largest eigenvalue λ, comparing q_i(λ) via rational Sturm root isolation. Examined the actual verifier implementing these exact comparisons, and independently enumerated ALL connected unlabeled networkx Graph Atlas representatives of n=2,..,7 with counts 1,2,6,21,112,853; a separate symmetric eigensolver found no distinct singleton leaders through n=6 and exactly 5 seven-vertex classes with the five same edge-list representatives and leader pairs. Gaps in detected distinct-leader cases were comfortably away from numerical tie threshold; exact Sturm source method, not numerical approximation alone, supports precise ties. Explicitly enumerated all 7! vertex relabelings of those 5 representatives, confirming automorphism orders 12,2,2,4,2 and orbit sizes 420,2520,2520,1260,2520 totaling 9240. Graph Atlas completeness externally documented; atlas enumeration is finite exhaustive for order≤7, not an infinite graph theorem.

## originality

PASS

Best-of-knowledge priority judgment based on direct statement/implication comparisons with specified inspected sources, published semantic search and alias checks; neither the source names nor negative searches by themselves demonstrate novelty. Aliases highest degree vertex, hub, unique maximizer, singleton eigenvector leader were searched. Generic different rankings or non-singleton eigenvector ties would not establish the same sharp unique/unique frontier.

## value

PASS

Disagreement of eigenvector and degree centrality is known, but the first order where the two *unique* leaders differ and the complete first obstruction layer are natural sharp boundary invariants. The five-class/9240 labeled census gives researchers an explicit minimal test corpus for the difference, rather than a single anecdotal network or an arbitrary unlabeled subset.

The dated certificate retains the supplied scientific assessment, sources and limitations.
