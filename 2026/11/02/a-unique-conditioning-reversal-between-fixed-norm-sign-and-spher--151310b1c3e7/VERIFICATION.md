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

The exact theorem appears in `RESULT.md`. Run `python3 verify.py` (Python 3.10+, standard library only); successful output starts with `VERIFY_OK`.

The checker has two exact-rational strict sign certificates for the sign-change function at \(x=0.7778\) and \(x=0.7779\), each carrying a rigorous series remainder bound. It also computes independent deterministic angular quadratures for nine values of \(\kappa\) and compares mean and squared-error quantities, checks the analytic Rademacher bias, and tests which probe wins at \(\kappa=128\) and \(256\). Forty assertions run. No stochastic simulation is used.

The finite checks do not prove all-parameter uniqueness; the complete analytical proof in `RESULT.md` uses absolutely convergent Fourier series, derivative monotonicity, limits and the strictly increasing condition-number transformation. Independent mathematical audit is not performed.
