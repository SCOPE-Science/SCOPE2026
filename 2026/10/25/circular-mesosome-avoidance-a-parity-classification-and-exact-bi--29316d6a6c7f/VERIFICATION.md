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

# Reproducibility and limits

Execute `python3 check.py` in the same directory. It scans every circular factor of each binary word at lengths one through 15 and detects a mesosome only when two equal-length halves differ but are conjugate. A separately written run-condition routine tests the theorem, and a rotation canonicalizer compares both counts. The observed terminal line is:

`CIRCULAR_MESOSOME_PASS tested_words=65534 n_range=1..15`

The tested set is finite; it cannot establish the theorem for arbitrary length. The unrestricted proof is in `RESULT.md`, relying on the previously published and cited linear run lemmas. Those lemmas were inspected in the author's public arXiv version; no independent expert review has been performed. No source states that finite one-turn avoidance implies avoidance of factors of arbitrarily long periodic repetitions.
