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
# Analytical and computational verification

The stated theorem is proved in `RESULT.md` by explicit evaluation of two complementary three-way order events and recovery of the other four from stationary two-point marginals. The proof covers all integer degrees and lags; `verify.py` is only a supplementary finite independent check.

Run `python3 verify.py` using Python 3 and the standard library. The direct cell-by-cell rational subdivision yields:

`VERIFY_OK: 68 exactly integrated degrees; six ranks, lag-one/two pair laws, temporal reversal and both finite-sum identities`

The checked degrees are 2 through 64 inclusive, together with 72, 81, 96, 125 and 128. For each case the checker integrates all six events exactly, tests total probability one and marginal comparisons, tests the two analytic finite-sum identities, and tests the time-reversal total variation. Finite enumeration by itself makes no claim concerning degrees or lags not listed; that conclusion rests on the general symbolic-arithmetic proof. Independent audit has not been performed.
