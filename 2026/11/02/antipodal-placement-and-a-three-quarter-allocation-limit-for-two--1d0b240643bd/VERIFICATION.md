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

# Reproduction and limits

Run `python3 CHECK.py` with Python 3. The script uses only the standard library and prints a PASS summary if all checks succeed. It constructs the killed cycle generator as an exact rational matrix and separately computes its inverse action on the all-ones vector using rational Gaussian elimination. The result is compared to the two-arc formula in 270 exact test configurations with \(3\le n\le14\). The seed for 6,750 nonoptimal placement/rate diagnostics is fixed in the script. Further boundary checks verify that either placing all reactivity at the starting trap or splitting the budget equally yields lifetime \(n/K\), independent of trap spacing. Weak/strong-budget diagnostic limits are also included.

These tests do **not** certify the all-parameter optimum: that is proved by exact derivatives and maximizing \(d(n-d)\) over integers in `RESULT.md`. There is no Monte Carlo uncertainty in the rational matrix checks. Numerical global comparisons are sampled, not exhaustive. No independent audit has been performed, and the historical originality assessment is limited to the materials actually accessible.
