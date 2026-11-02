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

## Executed checks

The included `check_clone.py` requires only the Python standard library. It constructs endpoint-minimal polynomials by exact rational Gram elimination; verifies the degree-dependent local Gram coefficients; independently inverts the complete-bipartite nodal matrices for all \(1\le p,q\le6\) and \(1\le d\le8\); and checks identical scaled vertex reproducing kernels at seven rational edge coordinates. The actual run reported:

```
PASS: independent exact Gram inversions and edge-kernel cloning in 4032 rational cases over degrees 1 through 8
```

## Analytic limits

Finite computations do not establish the infinite-degree theorem. The all-degree proof uses exact Legendre endpoint kernel sums, an explicit block-matrix inverse, and an elementary triangle-inequality monotonicity argument. The result concerns vertex evaluation and does not establish that any original vertex maximizes the full spline projection norm over all interior metric points. Independent audit is not performed.
