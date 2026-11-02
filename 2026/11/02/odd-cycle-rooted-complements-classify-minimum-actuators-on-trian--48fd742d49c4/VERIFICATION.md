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

# Reproduction and limits

Run `python verify.py` with Python 3.9 or later and no external dependencies. The actual tested command returned:

```
VERIFY_OK 6600 finite_check_groups sharp_census {5: (162, 162), 6: (2520, 2530)}
```

The first number in each census pair is the number of controllable minimum actuator sets; the second is the number of odd-unicyclic complementary edge sets before the exceptional exclusion. The script constructs the Laplacian of the line graph directly and evaluates its three known PBH eigenvalue ranks over the finite field of prime order `1000003`. It compares these results to independently computed unsigned-incidence ranks and to a graph-component test. Direct Kalman-matrix ranks are also replayed for the explicit small-order optimizers and the exceptional pair of triangles.

The \(n=5\) and \(n=6\) complementary-edge-set searches are exhaustive. For \(n=7\) and \(n=8\), only deterministic samples are checked; the all-dimensional classification instead follows from the symbolic incidence/PBH and extremal-density proof in `RESULT.md`. The generating-function coefficients are checked by rational truncated-series arithmetic for orders five through eight. These computations are checks, not independent verification or an exhaustive search over every larger order.
