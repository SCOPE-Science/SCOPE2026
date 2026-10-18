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
# Verification notes

## Analytic checks
The entire claim follows from the two exact displayed identities in `RESULT.md`: the geometric-sum expression minimized on the disk boundary for a homogeneous kernel, and the support-function Bellman recurrence for horizon-specific adaptive control. The second-order stationary asymptotic is justified by uniform localization near \(t a=\log t\). The adaptive limit follows from exact reciprocal increments tending to \(r/2\). The corner \(a=b=0\) and the strict stochasticity radius bound are included explicitly.

## Standalone finite checks
Run `python verify.py` using Python 3; no third-party packages are needed. The script verifies direct finite Markov propagation at horizons 1–10 against the analytic stationary formula, and a fine angular-grid support maximization for the first six adaptive recursions. For \(r=1/4\), the output at \(t=10000\) and \(t=100000\) is:

```
t=10000:  stationary gap=0.00189660127;  t*gap-2*log(t/2)=1.931626332; adaptive gap=0.00079447463; t*adaptive gap=7.944746314
t=100000: stationary gap=0.00023628594;  t*gap-2*log(t/2)=1.989037862; adaptive gap=0.00007992789; t*adaptive gap=7.992789271
```

The numerical values are approximations and **do not** certify limits for all horizons or all radii. The proof, not these finite checks, establishes the quantifiers in the theorem. No independent external review has yet been performed.
