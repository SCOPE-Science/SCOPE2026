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

# Reproducibility and limits

Run the self-contained Python 3 program `verify.py` from this directory. It needs only the Python standard library and uses exact integers throughout.

It independently constructs generalized binomial coefficients using factorial products; verifies divisibility of each numerator by its denominator; takes the gcd of all interior coefficients; and compares it with the ratio of consecutive prefix lcms. Cases include ordinary coefficients through row 72, Gaussian rows through 45 at bases 2, 3 and 5, Fibonacci rows through 75, and a non-linear strong divisibility sequence built from explicitly nested prime-power occurrence ranks through row 90. Prime-specific minimizing columns are separately checked for ten primes across four families. The final example is separately tested for the strong-gcd defining property on every pair of indices from 1 to 89.

Expected terminal output:

`VERIFY_OK: ordinary 72 rows; Gaussian 3 x 45 rows; Fibonacci 75 rows; synthetic chained-rank 90 rows and 7,921 independent gcd pairs`

These finite checks do not establish the theorem for all strong divisibility sequences or all indices. That is established by the rank-chain proof in `RESULT.md`, especially the construction of the prime-specific minimizing column. No third-party mathematical validation was performed.
