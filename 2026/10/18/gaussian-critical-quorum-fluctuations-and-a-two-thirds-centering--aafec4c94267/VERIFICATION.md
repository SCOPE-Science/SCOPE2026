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

# Verification

The complete analytic proof is in `RESULT.md`. The supporting program `verification/verify_critical_zipf.py` is executable using Python 3.9 or later with only standard-library modules. From the root of the extracted package, run:

```sh
python3 verification/verify_critical_zipf.py
```

It numerically solves the *exact* deterministic mean equation for several thresholds and sizes, tests the theoretical derivative and variance constants, checks the finite-size centering correction including the critical two-thirds value, and separately simulates independent first-arrival times with a fixed seed. The code asserts its numerical tolerances and prints an assertion count and finite Monte Carlo summary.

Finite tests do not prove convergence or priority. The proof of the Gaussian limit requires the explicitly stated Lindeberg bound, the exact \(1/(2A)\) leading variance and the monotone stopping-time inversion; each is derived in the analytic argument. Convergence is for fixed quorum threshold and independent Poisson-split first-arrival processes.

No external independent assessment, certification, or machine-checked infinite proof has been performed.
