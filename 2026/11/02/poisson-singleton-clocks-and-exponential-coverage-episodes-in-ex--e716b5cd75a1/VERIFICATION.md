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

# Verification record

Run `python3 verify.py` with Python 3.10 or newer in the directory holding the packaged file. It uses only standard-library modules and has no external data dependencies. The saved `verification_output.txt` records **403 passed deterministic exact assertions** on \(2\le n\le4\), \(n\le M\le n+2\), short future strings, and applicable short survival horizons. The checks verify the entrance Palm distribution, exact Stirling-number mean, exchangeability of singleton positions, singleton-number formula, and finite-time survival inequalities.

The proof in `RESULT.md` establishes the infinite \(n\to\infty\) conclusions. In particular, the zero-truncated-Poisson conditioning and local estimate bound single-color probabilities; a concentration calculation produces a Poisson singleton-position point process, and a union bound excludes replacement-coupon rescue and multiple-copy expiry in a bounded scaled interval. The exact mean is obtained by stationarity and an independent asymptotic exit-hazard calculation. No finite computation proves a functional limit or historical originality.

The self-review status is passed; independent audit has not been performed and no external certification is claimed.
