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

# Reproducible mathematical checks

The two-run enumeration checks membership directly from adjacent bits. `check_two_runs.py` uses the exact, depth-indexed recursive shattering predicate. For sizes one through fourteen, it confirms existence at the stated depth and nonexistence at the next depth; its evaluated state counts include 802 at seven and 179260 at fourteen. `crosscheck_two_runs.py` independently enumerates literal binary strings and computes their numeric Littlestone ranks through eight.

`depth5_tree.json` records 31 internal nodes and 32 distinct leaf witnesses for a depth-five tree on seven points. `depth9_tree.json` records 511 internal nodes and 512 distinct witnesses for a depth-nine tree on fourteen points. The checker verifies the complete answer path to each leaf and validates that every witness has at most two positive runs. Exact full scans establish the upper bounds.

Reproduce with `python3 check_two_runs.py --full --certificate depth5_tree.json`, `python3 check_two_runs.py --full --certificate depth9_tree.json`, and `python3 crosscheck_two_runs.py`. These are finite-program checks, not independently audited mathematical publication, and they do not establish an unrestricted dimension formula or historical novelty.
