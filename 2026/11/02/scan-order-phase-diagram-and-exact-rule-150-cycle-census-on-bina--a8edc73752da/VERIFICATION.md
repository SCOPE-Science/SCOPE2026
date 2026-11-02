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

# Reproducibility checks

Run `python3 verify.py` in this directory, using Python 3 and no third-party dependencies. `verification_output.txt` is the captured successful standard output for the included exact code.

The verifier directly composes binary site updates, derives the complete scan matrices, checks all relevant nullities of \(F_\pi^t-I\) against the formula, and confirms the exact full-scan order for 12,310 scan/dimension cases. It exhaustively enumerates all 5,910 scan permutations on dimensions \(3\) through \(7\) and all 695,472 states in these scan cases, checking primitive periods and all fixed-power populations. It also confirms the Eulerian class frequencies and checks sampled orders in dimensions \(8\) through \(25\). The console terminates with `ALL_CHECKS_PASSED`.

These finite tests are not an infinite proof. The general theorem depends on the local edge-swap identity, the reduction to canonical scans, the exact two linear return constraints, and the order argument in `RESULT.md`. The code does not evaluate other asynchronous elementary rules, multi-visit schedules, or extension fields, and supplies no independent audit.
