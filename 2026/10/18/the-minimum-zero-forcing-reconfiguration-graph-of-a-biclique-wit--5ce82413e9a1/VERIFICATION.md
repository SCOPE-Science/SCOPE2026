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

# Verification

`verify_two_deleted.py` constructs the labeled bipartite graph independently from edge deletions, exhaustively simulates the ordinary blue-neighbor color-change rule on every initial set for all \(3\le a,b\le8\), and derives the solution-exchange adjacency by symmetric difference. It checks that no zero-forcing solution leaves five or more white vertices, tests every four-white signature, tests the predicted number of minimum sets, regularity, edges, connectedness, and all-pairs shortest-path diameter. The recorded successful result is in `verification_output.txt`.

This is a finite check of 36 graph instances and 254,016 initial blue sets; it is not an exhaustive check of all integer part sizes and cannot establish literature priority. The mathematical proof in `RESULT.md` supplies the all-parameter argument. No independent audit has been performed.
