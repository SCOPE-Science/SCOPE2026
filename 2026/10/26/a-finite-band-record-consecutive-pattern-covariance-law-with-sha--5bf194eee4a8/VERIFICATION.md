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

The standalone Python script `verify.py` enumerates all permutations through \(n=8\), using exact rational arithmetic. For every \(2\le k\le\min(5,n)\), it compares the directly enumerated covariance of total record count and each of the \(k!\) consecutive-pattern counts with the closed finite sum in the proof. For \(n\le7\) it also compares every positional record-indicator/pattern-indicator covariance, including predicted off-band zeros. For each tested length it verifies the limiting formula's unique maximizer, minimizer family, and extreme values.

Execution in a standard Python 3 environment returned exactly:

`VERIFY_OK 7472 exact finite covariance and extremal assertions, exhaustive permutations through n=8`

These experiments validate many small exact cases. They are not a proof for unbounded permutation lengths or pattern lengths; the order-statistic argument and harmonic summation in `RESULT.md` are the analytic proof. No source independence or publication priority has been externally certified.
