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

## Verification record

The included `verify.py` was executed from the packaged path using only the Python standard library. Its output was:

`VERIFY_OK 1023 assertions; exact rational normalization N<=30; exhaustive threshold assignments N<=7; tail coefficients at three cutoffs`

The checks include exact rational normalization and the exact full-cascade mass for every \(N\le30\) and every \(1\le s\le N\); exhaustive enumeration of all nonseed threshold assignments for every seed count through \(N=7\); and numerical tail-coefficient checks at three fixed cutoffs for \(N=1600\) and \(s\in\{1,2,3\}\). These checks do not prove the all-\(N\) theorem or the asymptotic limit; those follow from the combinatorial count and analytic proof in `RESULT.md`.

The proof uses the generalized parking-function count, the exact ratio to the one-seed mass, Stirling's formula on compact subintervals, and a bound controlling the endpoint near \(x=1\). The model's finite-population endpoint \(k=N\) is handled separately. No external or independent validation was performed.
