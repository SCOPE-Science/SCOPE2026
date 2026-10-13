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
# Finite checks and symbolic proof boundary

Run `python3 verify.py` using only Python's standard library. Successful execution prints one `VERIFY_OK` line with counts of independent subset-BFS instances, inverse-interval cases, and large witness replays. Any discrepancy triggers an assertion.

The BFS computes true minimal reset lengths on all parameter pairs \(4\le n\le15\), \(2\le k\le n-2\), from the full subset of states. The interval tests check the two pieces of the mathematical argument — a useful inverse-collapse requires at least \(n-k\) rotations and preserves the anchored interval or reaches the empty set. Longer witness replays test attainment without using BFS. The code does not certify the infinite claim by extrapolation: the complete proof appears in `RESULT.md`, with explicit treatment of all parameters, nonexpanding steps, interval wraparound, and the boundary case. No independent audit is claimed.
