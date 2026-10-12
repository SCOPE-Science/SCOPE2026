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
# Reproducibility and checks
Run `python3 verify.py` in the directory containing this file and the bundled verifier. Only the Python 3 standard library is needed.

The finite verifier reports `VERIFY_OK 36055 checks threshold 0.069955209282968`. It uses exact rational arithmetic for the high-variance endpoint-atom moments and squared-CDF integral and for low-variance rational-width uniform laws. It also tests 16,000 symmetric and 10,000 asymmetric randomly chosen finite-atomic laws with exactly fixed mean one half against the global lower envelope. Three endpoint consistency checks and four critical-threshold checks complete the test count. The fixed seed makes the finite experiment reproducible.

The infinite and all-variance result is established by the explicitly displayed nonnegative variational remainder in RESULT.md, not by Monte Carlo. No proof of global protocol optimality, multihop/percolation correlation structure for overlapping swaps, or unrelated quantum systems is included. The proof uses the existing two-link minimum rule as a hypothesis. No independent external audit or validation has occurred.
