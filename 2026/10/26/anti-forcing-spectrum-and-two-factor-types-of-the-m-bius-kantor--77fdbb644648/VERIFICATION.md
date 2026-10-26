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

# Reproducibility
Run `python3 mk_antiforcing_verify.py` (Python 3, standard library only). A successful run ends with `VERIFY_OK`. The 16-vertex graph and the full set of 24 edges are generated without input data files. Every perfect matching is enumerated by vertex recursion and checked against a second bipartite permutation enumeration and an exact permanent count. The graph automorphism group is searched exhaustively, and each matching is assigned an orbit and complementary 2-factor type.

For each matching, the anti-forcing number is computed as an exact minimum feedback-arc set via a full eight-vertex subset recurrence. For each of the three orbit representatives, a separate explicit deletion search tests every smaller size and finds a deletion witness, while a directed-simple-cycle enumeration finds a matching-sized arc-disjoint packing witness. Printed masks refer to edge and cycle ordering generated inside the same script and are reproducible there. No heuristic or external solver is required.

This exhaustive computation certifies the stated finite cases only. It is not an independent external audit, and it does not establish an infinite-family theorem.
