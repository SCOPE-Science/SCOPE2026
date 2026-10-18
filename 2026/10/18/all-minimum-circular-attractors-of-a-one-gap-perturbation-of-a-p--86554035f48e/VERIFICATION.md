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

The executable `checker.py` is self-contained Python 3 and requires no external input, data download, or third-party package. Run `python3 checker.py` from this directory. Its expected exact stdout is `check_output.txt`.

The checker generates each word literally and constructs the coverage bitmask of every distinct circular factor, using **all** start positions and all lengths from one through the word length. It checks for each mask that one of the four listed witness factor masks is contained in it, independently enumerates all two-position subsets, compares the entire admissible set to the formula, checks the cardinalities, and excludes one-position solutions by disjoint letter-coverage masks.

Ranges: \(2\le m\le7\), \(1\le q\le6\), \(1\le s\le7\). The output records 252 parameter triples, 79,142 distinct factor instances totaled over the triples, and 2,604 optimal pairs totaled over the triples. The hand proof, not these finite checks, establishes all unbounded parameter cases. No external independent audit has been conducted.
