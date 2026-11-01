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

The accompanying `check.py` uses Python standard-library `Fraction` arithmetic and deterministic finite sums. It proves nothing beyond the tested instances. Running `python3 check.py` returned `PASS: 228 exact rational assertions`: six expected-gap identities and 222 fixed-horizon stochastic-order comparisons. The infinite stochastic order is established by a log-concavity argument in the result text, and the logarithmic asymptotic by Poisson-clock comparison plus localized Gamma central limits and inclusion--exclusion.

Exact expectation differences checked for \(n=2,3,4\) are \(4/3\), \(52/35\), and \(724/455\), respectively. The last four exact rational values and their decimal approximations appear in checker output. The proof's stochastic comparison assumes the same fixed initial vertex in both processes. Quantitative uniform error bounds in the asymptotic and a constant-order correction are not claimed. Independent audit and historical priority certification have not been performed.
