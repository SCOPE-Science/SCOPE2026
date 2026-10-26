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

# Reproducibility and checks

Execute `python3 verify_three_cliques.py` with Python 3.9 or newer, in a directory containing the script. No third-party packages are needed. The expected transcript is supplied in `verification_output.txt`.

The checker constructs the original graph adjacency and tests the defining 1-fair property for each unselected vertex. It validates each candidate partition using actual pairs of blocks. It exhaustively enumerates every set partition of graphs with clique orders \((3,3,3)\) and \((3,3,4)\), then performs a distinct exhaustive enumeration of partitions with deficit at most three for nine parameter profiles. Outputs report both the optimum block number and the exact optimizer count.

The finite tests cannot establish an all-size claim; the proof in `RESULT.md` establishes the universal bound, construction, classification and count. No independent audit was performed, and priority beyond the inspected literature is not independently certified.
