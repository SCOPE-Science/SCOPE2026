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

# Reproduction and bounds

Run `python3 code/posa_paths.py` and `python3 code/edge_subsets.py` using Python 3 standard library. The first uses only all vertex-simple eleven-vertex paths with a red initial endpoint; the second independently tests each of the \(43{,}758\) ten-edge subsets. Both construct all valid states and then perform complete graph searches from all states. Their asserted final values are 222 paths, 444 rotation/exchange edges, a single connected component, radius 8, diameter 9, and exactly 198 and 24 states at eccentricities 8 and 9. Compare stdout to `verification/posa_stdout.txt` and `verification/edge_stdout.txt` for the recorded results. All embedded file hashes and byte counts are checked separately by the envelope validator.

The programs prove the exact finite instance, not general results for other planar or bipartite graphs. They are independent constructions of the same undirected path space, not independent external scientific audits.
