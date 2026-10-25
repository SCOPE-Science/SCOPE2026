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

# Reproduction

Run `python3 verify_ladder.py` using the Python 3 standard library. It builds the geodesic triple hypergraph directly from Manhattan distance equality, solves the smallest-color instances by backtracking for ladders with one through five columns, and checks explicit colorings with a separately implemented enumeration of all shortest paths of up to five edges on ladders through 32 columns. The embedded `verify_ladder_output.txt` records the expected lines.

The infinite lower bound follows from the analytic five-column geodesic comparison, not from backtracking. The infinite upper bound follows from the proof that every shortest path of length at most five is either a horizontal segment or a monotone two-row path with exactly one rung. Finitely repeated tests do not certify the all-order claim on their own. No independent audit has occurred.
