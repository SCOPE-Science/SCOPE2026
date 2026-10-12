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

# Reproducible checks

Run `python3 verify.py` with Python 3 and its standard library. This recomputes \(a(n)\bmod8192\) for \(0\le n\le145\) independently by (i) multiplying the defining exponential-generating-function factors with binomial convolution, and (ii) computing the integral ordinary series \(H(y)\) and applying a Stirling transform. All 146 values agree. Fifteen initial OEIS coefficients, the first eight \(H(y)\) coefficients, both eight-entry finite-difference rows, 705 parity-sensitive half-shift tests, and eventual-period checks for \(r=5,\ldots,10\) are reproduced using exact integers.

The observed standard output is embedded as `verify_output.txt`. This is finite evidence only; the all-exponent theorem is established separately by the finite-difference proof in `RESULT.md`. Neither this checker nor that proof establishes a least initial preperiod or an exact period for general odd moduli. Independent audit is not performed.
