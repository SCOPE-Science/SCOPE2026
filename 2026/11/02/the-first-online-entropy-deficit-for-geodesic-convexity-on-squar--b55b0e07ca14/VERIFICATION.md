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

# Verification instructions and scope

With Python 3.9+ and no third-party dependencies, execute `python3 verify.py` in a directory containing this file and `verify.py`. Successful execution ends with the exact marker `SQUARED_PATH_CONVEXITY_ALL_CHECKS_PASS`.

The checker enumerates the entire asserted family of empty, interval and parity-progression hypotheses. For orders up to eleven it also directly enumerates every graph vertex subset and tests geodesic convexity against breadth-first-search graph distances, not against the asserted classification. For orders up to twenty it enumerates every triple support and verifies the alternating-parity trace criterion. Its exact online solver recursively considers every vertex query in every reachable version space, using memoization and a cardinality-based pruning condition that cannot remove a better split. A different Boolean feasibility recursion verifies the computed rank and rejects the next larger depth for all orders up to twelve. For order ten, a depth-five complete shattered tree with 32 distinct terminal concepts is constructed and all answer paths are checked.

The claimed finite ranks are deductions from the complete mathematical recursion plus an exhaustive finite evaluation by the embedded executable checker. No finite run proves the all-order asymptotic statement: that statement has a separate mathematical argument in `RESULT.md`. No data file, package from another run, remote checker, or privileged service is required.

These are self-review methods. Independent scientific audit and historical-priority validation have not been performed.
