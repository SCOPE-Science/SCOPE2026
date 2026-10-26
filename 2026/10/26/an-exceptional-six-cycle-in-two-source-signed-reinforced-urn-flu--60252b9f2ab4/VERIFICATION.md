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

The reproducible program `verify.py` uses Python 3 and NumPy, and tests the exact finite cyclic matrix identity, Fourier eigenvalue calculation, exceptional Gaussian sizes, and a uniform analytic inequality. It reports 74 successful checks; see `verification_stdout.txt`. The analytical proof supplies the infinite-time convergence, central limit, and nonzero martingale amplitude claims. The independent audit has not been performed.
