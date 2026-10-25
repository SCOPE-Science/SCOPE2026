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

The standalone `verify_complete_bipartite_strong_morse.py` uses only the Python standard library. It enumerates all orders and the corresponding descending-dominated vertices of the one-dimensional complete bipartite graph, reconstructs the complete simplicial complex, and confirms the proposed facets are exhaustive. It then performs legal elementary simplicial collapses, checking unique immediate cofaces before each removal; it verifies the final graph's vertex and edge counts and connectivity. Finally it computes signed simplicial Lefschetz traces for every tested group action and compares them to the proposed first-homology characters.

Verified cases: \((m,n)=(2,2),(2,3),(3,3),(3,4),(4,4)\). The respective numbers of nonempty simplices are 20, 47, 96, 193, 344. Elementary collapses are 0, 8, 24, 64, 128, totaling 224. Signed character comparisons are 8, 12, 72, 144, 1152, totaling 1,388. No counterexamples were found. The two cases with a part of size two test boundary consistency and are not included in the new theorem's novelty claim. The general proof is analytic and combinatorial for every \(m,n\ge3\); the finite tests do not establish its universal quantifiers by themselves.

The original 2026 reference was inspected through its available HTML introductory definitions and theorem overview; later sections could not be fully retrieved. No external independent audit or formal-proof certification is claimed.
