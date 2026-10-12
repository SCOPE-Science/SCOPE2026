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
# Reproduction of the analytic checks

Run `python3 verify.py` in the directory containing this file. The script uses only the Python standard library. It prints `VERIFY_OK 56` after 56 groups of checks.

The coefficient identity is independently checked by enumerating all positive compositions at lengths from 3 through 24. The finite-capacity formula is checked against direct exhaustive enumeration, without reusing the coefficient formula, of all four-element node sets, the three perfect matchings, and every Bernoulli edge mask for chain sizes \(4\le N\le8\), at exact rational link probabilities \(0,1/3,1/2,2/3,1\). The fixed-link loss constant and critical-window integral are evaluated against finite-size sums for selected parameters; these numerical convergence checks test implementation rather than prove limits.

The analytic all-size correctness argument is in `RESULT.md`. No independent external audit, hardware experiment, or numerical certification of an infinite-size statement has been performed.
