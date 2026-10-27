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
# Verification details

The script `verify.py` builds the rook graph directly and for every enumerated vertex subset checks the induced graph for cycles using adjacency and graph traversal. This is independent of the line-graph/path characterization used in the proof. It separately computes the full polynomial through a first-designated-row-vertex recurrence for labeled bipartite path-component counts, and checks every inclusion-maximal subset against the asserted maximum size, then compares the maximum component counts to the factorial formula.

The ten checked board sizes are: 1 by 1, 1 by 4 (exploratory boundaries), 2 by 2, 2 by 3, 2 by 4, 2 by 5, 3 by 3, 3 by 4, 3 by 5, and 4 by 4. Exactly 104290 subsets were examined, and the recorded output says PASS. The cases with smaller shore one are outside the theorem and only test the checker recurrence boundary.

Reproduce using a standard Python 3 interpreter with `python verify.py`. The script uses only the standard library. Its deterministic stdout should match `verification_output.txt` byte for byte. This is an exact finite consistency check, not an exhaustive check for unbounded input size. No external validation or independent audit has occurred.
