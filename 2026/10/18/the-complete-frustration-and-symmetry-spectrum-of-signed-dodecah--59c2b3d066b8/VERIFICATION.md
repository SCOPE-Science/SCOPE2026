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

# Reproducible checks and limits

Run `python3 code/verify_bfs.py` and `python3 code/verify_pairing.py` with Python 3 and no third-party packages. The first computes the 2048 even-face parity state distances by a breadth-first traversal, writes all cases to `data/frustration_distances.csv`, enumerates the 120 generated graph symmetries and writes the 46-orbit table to `data/icosahedron_orbits.csv`. The second defines the dual graph independently, obtains its shortest-path metric and exact minimum-pairing recurrence, and compares all 2048 distances against the certificate. It also computes 125 perfect matchings by subset recurrence and checks the refined distribution by number of negative faces.

Expected console transcripts are `data/bfs_output.txt` and `data/pairing_output.txt`. Each is deterministic. Finite exhaustive enumeration here constitutes an exact proof for the fixed graph when the independently stated reduction is valid; it is not evidence for arbitrary graph orders. The minimum-frustration/T-join equivalence and graph automorphism bound are mathematical proof steps explained in `RESULT.md`, not empirical assumptions. No independent external scientific audit has occurred.
