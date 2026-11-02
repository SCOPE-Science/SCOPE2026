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

The complete analytic proof is in `RESULT.md`. Reproduce the deterministic diagnostics with:

```sh
python3 verify.py
```

Observed output:

```text
PASS 61766 deterministic assertions
CDF P(S<1) = 0.56807221928743
E[S] = 0.98435062160765
E[S^2] = 1.05179979026464
```

The program independently checks the covariance identity and signed-rotation covariance with exact arithmetic, the Dirichlet eigenmode integral, two distinct convergent spectral/image series, monotonicity, the first two moments and boundary asymptotics. All computations use only the Python standard library. Finite checks do not prove continuity, all-threshold identities, infinite moment formulas, or the Haar factorization; these are demonstrated in `RESULT.md` by the heat-kernel, theta transform, Tonelli integral, Gaussian covariance and no-ties arguments. Exact historical originality remains subject to external review.
