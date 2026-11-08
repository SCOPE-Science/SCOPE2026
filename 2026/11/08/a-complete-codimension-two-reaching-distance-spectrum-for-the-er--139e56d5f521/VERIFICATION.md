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

# Reproducibility and scope

Run `python3 artifacts/verify_reaching.py` from the package root. The checker uses standard-library Python only. It separately implements all image-subset transitions and breadth-first distances for each \(3\le n\le15\), tests every target with exactly two missing states, constructs and replays an optimal normal-form word for every pair, and checks every predicted multiplicity. A separate sweep through \(3\le n\le140\) checks the all-letter 1-Lipschitz potential inequalities for every rank-relevant subset.

The recorded execution in `artifacts/verification_output.txt` reports `BFS_PASS`, `POTENTIAL_TRANSITION_PASS` and `VERIFY_OK`. The finite tests are not a substitute for the universal proof in `RESULT.md`. The proof handles arbitrary nondecreasing sequences of missing sets and therefore permits all words (not only those containing exactly two merging letters). Nothing beyond the stated labeled automata or codimension-two targets is asserted.

Independent scientific audit: not performed.
