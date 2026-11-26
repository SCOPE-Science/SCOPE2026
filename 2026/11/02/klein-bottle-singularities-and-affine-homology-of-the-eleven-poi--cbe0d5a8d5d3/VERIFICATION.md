---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
    ],
    "status": "passed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---
# Verification of Paley-11 local links

Run `python3 paley11_checker.py` with the Python standard library. The checker applies the source-deletion test to all subsets of sizes one through five, tests purity and the tetrahedron incidences and adjacency, and constructs the entire link at zero. It checks the triangle list, connectedness, all edge incidences and the six-cycle link at every link vertex, and the sign product along the displayed closed dual walk. Translations preserve the arc predicate and give the other ten links. The expected success marker is `PALEY11_KLEIN_BOTTLE_LINKS_OK`.

The program verifies finite combinatorial inputs to the proof. The surface classification and the conclusion about manifold neighborhoods use the mathematical argument in `RESULT.md`. The checker does not compute any global homology, group representation, quotient invariant, or statement about other tournaments.
