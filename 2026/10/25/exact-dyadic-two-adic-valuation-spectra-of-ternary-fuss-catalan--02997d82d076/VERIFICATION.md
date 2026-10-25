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
# Reproducibility and verification

Run `python3 verify.py` in the directory containing this file and the bundled verifier, using Python 3. No network access or non-standard dependencies are required. The program independently calculates factorial-based valuations for \(n<2^{12}\), checks 120 exact integers from the binomial quotient, builds transfer-matrix histograms, checks the rational recurrence through binary length 26, and checks oddness, extreme multiplicities, and exact means through length 12.

Observed completion: `VERIFY_OK: 120 exact Fuss--Catalan integers; 8191 factorial-valued indices; 13 exhaustive dyadic histograms; 24 exact polynomial recurrences; 13 sharp parity/extremum/moment checks`.

The 8191 quantity is the cumulative count of valuation evaluations over dyadic histograms with lengths \(0\) through \(12\); values of \(n\) repeat across these intervals. The matrix-histogram computation is logically separate from the factorial-valuation enumeration but both share the mathematical definition. The verifier does not algorithmically establish an infinite identity or provide external audit. Formal-power-series algebra, exact Fibonacci language counts, and the simple analytic eigenvalue argument supply the universal reasoning in `RESULT.md`. In particular, no finite sample alone certifies the Gaussian limit.
