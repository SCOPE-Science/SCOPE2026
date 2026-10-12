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

# Reproducibility and proof boundary

Run `python verify.py` with Python 3's standard library. The script evaluates \(I_0(2\lambda)\) and \(I_1(2\lambda)\) from the defining nonnegative power series using 72-digit `Decimal` arithmetic. It independently sums the two-sample Poisson maximum's mass \(F(j)^2-F(j-1)^2\) to recover its first two moments at 16 intensities \(0.01\le\lambda\le8\), compares both results with the analytic formulas, and bisects the parent-variance threshold.

The replay printed `VERIFY_OK direct_max_cases=16 max_abs_difference=7.890E-68` and brackets the critical intensity between decimal values beginning `1.166797401918403650866561825466743804328` and `1.166797401918403650866561825466743804330`.

The check uses a fixed finite summation truncation and finite precision; it is not a proof for every intensity. For universal correctness and uniqueness use the exact Bessel recurrences, the displayed positive logarithmic derivative, and the small- and large-intensity limits in `RESULT.md`. No independent external verification has been performed.
