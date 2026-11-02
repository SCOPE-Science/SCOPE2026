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

# Reproducibility checks

Run `sh run_verification.sh` with Python 3 from this directory. The script replays the two independent programs, whose saved console output is in `verification_output.txt`.

`verify_direct.py` constructs all vertices and complete atomic diagrams for ordered triples of vertices in graphs with factor counts 2 through 7, deriving the exact three-round EF root type by two successive extension-set recursions. It observes three distinct root types for counts two, three and four, followed by equality of the root type for four through seven.

`verify_structural.py` derives the ordered-pair extension patterns from the four Venn-region cardinalities for counts four through twelve. It exhausts all finite pairs of cardinality types, verifies every row's set of allowed third-vertex adjacency patterns, and verifies the possible pair classes by initial-vertex cardinality category. All printed tests pass.

These finite computations are corroboration. The infinite classification is proved independently by the explicit uniform pair-response table and the three-round strategy in RESULT.md. No independent mathematical audit or certification has taken place.
