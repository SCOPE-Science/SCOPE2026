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
Run `python checker.py` using Python 3 standard library. It independently constructs words and enumerates all positioned even-length circular segments through rank 8; the output ends with `CHECKER_PASS`. It checks the parity Gray identity on every prefix and compares both even-Parikh and abelian-square occurrence sets against the claimed exact family. The counts are \(0,1,3,7,15,31,63,127\) for ranks one through eight. There is no external proof certificate. Full correctness for arbitrary rank follows from the symbolic proof in RESULT.md, not from a search cutoff.

The original objects use distinct literal alphabet symbols; cyclic factors have at most one full traversal. Published originality has been checked against named primary sources but cannot be globally certified. Independent mathematical audit has not been performed.
