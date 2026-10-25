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

Execute `python3 checker.py` from the directory containing `checker.py`. No external packages are required.

The checker constructs every word with exactly two `a` and two `c` symbols and between zero and fifteen `b` symbols. It directly counts the three scattered-subword entries of the Parikh matrix, independently computes the cut representation, and checks every reachable signature against the closed support formula and the total count. It also runs 2,500 reproducible randomized cut-configuration tests up to ninety middle symbols. The recorded local run reported:

`CHECK_OK direct_words=93024 complete_slices=5456 random_slices=2500`

The general result rests on the grid-interval lemma and the proof in `RESULT.md`. The finite checker alone does not establish it for unbounded word length. Historical priority and strong matrix-equivalence counts are outside the proved statement. No independent audit has been performed.
