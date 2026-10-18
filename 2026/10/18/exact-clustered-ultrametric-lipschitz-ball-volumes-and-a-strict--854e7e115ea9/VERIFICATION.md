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

# Reproducible mathematical checks

The analytic identity is proved without relying on finite computation. The included `verify_ultrametric.py` uses only exact `fractions.Fraction` and integer arithmetic from the standard library. It enumerates lattice points in each scale of an anchored difference-constraint polytope after a common-denominator scaling. The incidence constraint matrix is totally unimodular: hence integer edge-length constraints yield integer vertices. The highest forward finite difference of the Ehrhart counting polynomial is the dimension-factorial times the volume of the integer-scaled polytope. This obtains coordinate volume by a route distinct from differentiating the cluster-range formula.

Run `python3 verify_ultrametric.py`. The observed terminal output is:

```
EXACT_EHRHART_VOLUME_PASS 20 configurations (including 6 nonuniform radii)
STRICT_BALANCING_CHECK_PASS 5350 transfers
```

The tests cover cluster counts two through four, sizes including singleton and nonsingleton clusters, rational common radii, and six configurations with nonidentical cluster radii. The strict inequalities are also checked over all directed nontrivial balancing transfers of compositions for tested values of \(N\), using rational radius \(2/3\). The displayed counts were obtained by executing the actual code. Passing finite tests cannot prove an infinite-dimensional assertion; the measure-theoretic derivative estimate and transfer identity in the proof provide that assertion. No machine-formal proof or independent audit is asserted.
