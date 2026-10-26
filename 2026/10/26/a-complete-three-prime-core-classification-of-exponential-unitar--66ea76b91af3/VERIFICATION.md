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
# Verification information

The accompanying `artifacts/verify.py` performs independent direct exact-arithmetic checks of exponential-unitary divisor sums over all positive integers through \(500000\), 150444 eligible prime-power parameter cases on the first nine primes, and 2682 local inequalities. It produced:

`VERIFY_OK direct_full_interval_N=500000 perfect_count=4338 cores=[36, 1800, 2700] exact_powerful_parameter_cases=150444 local_inequalities_checked=2682`

The infinite classification is proved by the explicit local upper bound and finite logical case analysis in RESULT.md. Exhaustive finite tests do not establish an unbounded theorem. The publication-priority assessment does not constitute independent mathematical validation, and relevant inaccessible or unindexed prior publications may exist.
