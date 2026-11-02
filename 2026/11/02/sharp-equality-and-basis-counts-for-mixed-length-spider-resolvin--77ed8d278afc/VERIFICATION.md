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

# Reproduction and limits

Run `python3 verification/check_spiders.py` from the package root. The script constructs each graph, independently calculates BFS distances, enumerates every subset for \(0\leq p\leq5\) and \(2\leq q\leq5\), and checks both domination and distinct distance signatures for vertices and edges. Its expected output ends in `PASS: 24 graphs; 171360 vertex subsets checked against original definitions`. This is finite corroboration only. The unlimited-parameter theorem follows from the constructive proof in RESULT.md.

The mathematical assessment is a self-review; no independent audit or external validation has been performed.
