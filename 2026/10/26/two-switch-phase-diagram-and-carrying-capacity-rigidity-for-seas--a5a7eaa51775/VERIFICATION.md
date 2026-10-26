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

## Reproduction and limits

Run `python3 verify.py` with Python 3.10+; there are no third-party dependencies. The program checks 12,000 randomized direct-composition/log-ratio identities, 2,500 exact open-wedge root bracketing cases, 6,000 shared-positive-equilibrium sign checks, the algebraic exact two-root witness, the near-tangency square-root scaling, and 2,000 Beverton--Holt structural comparison cases. Executing this finite test cannot prove a universal inequality or establish priority; the proof rests on the elementary analytic derivative, convexity and Taylor arguments in `RESULT.md`.

Direct boundary checks: at the lower open-wedge boundary the function has a zero only at the excluded point of zero initial abundance and one additional positive zero. At the upper boundary it has a positive tangency and no negative interval. Positive asymptotic output values may be arbitrarily small numerically, which is why the analytic sign proof uses their log ratio. The statement is about positive real initial abundance and precisely two deterministic updates; no uncertain observational or infinite-orbit conclusions are claimed.
