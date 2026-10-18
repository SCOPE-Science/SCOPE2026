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

# Finite verification and proof boundary

Run `python3 checker.py` in the directory containing `checker.py` and `checker_output.txt`. The checker has no third-party dependencies. It constructs an independent graph for each \(3\le n\le40\), calculates shortest distances by reverse breadth-first search and numbers of shortest paths by dynamic programming, and compares these independently calculated quantities against every claimed pair coordinate, minimum word, potential inequality and uniqueness assertion. It also replays each proposed shortest word and checks both its length and symbol counts. A successful run prints exactly the line stored in `checker_output.txt`.

The finite replay covers \(10{,}659\) pairs. The proof for all \(n\ge3\) is the explicit potential-and-descent argument in `RESULT.md`; enumeration at bounded \(n\) does not prove the infinite theorem. No independent audit has been performed. Publication priority is not certified by computational replay.
