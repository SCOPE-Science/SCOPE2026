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

# Reproducibility

From the directory containing this file, run `python3 artifacts/check_pmorph.py` with Python 3 and no third-party dependencies. The script computes the stated recurrence independently of an exhaustive test of all set functions. For each function it verifies surjectivity and the complete successor-set equality for every source point.

The expected output is `PASS: 687 exhaustive pairs; 6 anchors`. The exhaustive cross-check spans every enumerated pair of nonempty source and target level-size vectors of heights at most three, each level size in \(\{1,2,3\}\), source cardinality at most seven, target cardinality at most six, and target cardinality no larger than the source cardinality. Six additional non-exhaustively checked parameter anchors stress the recurrence for larger heights.

The symbolic proof in `RESULT.md` is necessary for the unrestricted claim. Finite testing alone does not establish correctness for unbounded heights or level sizes. No independent audit has been performed.
