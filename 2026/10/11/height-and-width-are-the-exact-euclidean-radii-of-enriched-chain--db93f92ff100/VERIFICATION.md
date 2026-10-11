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
The all-poset theorem is proved symbolically in `RESULT.md`.

Critical verified premises and deductions:
- The selected source defines the enriched chain polytope as the convex hull of signed antichain characteristic vectors.
- The complete facet theorem gives one facet for every maximal chain and every sign pattern, with right-hand side \(1\).
- A maximal-chain facet normal has squared norm equal to the chain cardinality.
- Maximizing over its sign patterns converts the translated-ball condition exactly into a sum of absolute center coordinates.
- A longest chain therefore determines the global inradius bound, while the origin attains it.
- Maximum antichains give antipodal points of norm \(\sqrt{w(P)}\), and every generator has norm at most that value.
- Equality in the Euclidean triangle inequality classifies the complete outer contact set.

`verify.py` enumerates antichains and maximal chains for several representative finite posets, checks all signed generator/facet incidences, and confirms the stated height, width, contact counts, and longest-chain-cover uniqueness criterion. The finite replay is corroborative only and does not establish the arbitrary-poset theorem.
