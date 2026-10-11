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

# Analytical and reproducibility verification

The proof concerns the Yablonskii planar quadratic vector field given in `RESULT.md`, with \(0<a<b<3a\) and \(0<c<c_*\). All time integrals use original physical time. The parameter boundary \(c=c_*\) is analyzed only as a one-sided limit.

Run `python3 verify.py` with Python 3 and no additional dependencies. The checker constructs exact rational-coefficient polynomials in all five formal indeterminates \(a,b,c,x,y\). It verifies the full identity \(P f_x+Q f_y-kf=0\) coefficient by coefficient, rather than checking a sample of parameter values. It also performs independent angle-regularized Simpson quadrature for \(a=1\), \(b=2\), checking the zero-parameter closed form, monotonic samples, the sharp critical coefficient, and the half-time Cauchy-window prediction. Recorded output:

```
EXACT_POLYNOMIAL_IDENTITY_OK
PERIOD_QUADRATURE_OK
MONOTONIC_SAMPLES_OK
ENDPOINT_ASYMPTOTIC_SAMPLE 1.799926802072 1.800779682234
SCALED_CAUCHY_UNIT_WINDOW_SAMPLE 0.50024067 (limiting 0.50000000)
CHECK_OK
```

The polynomial check supplies exact evidence for invariance; the finite quadratures supply only reproducibility cross-checks. They cannot independently establish an all-parameter inequality, an infinite-parameter limit or weak convergence. Those conclusions follow from the signed branch flow, exact derivative \(F'(x)\), strict quadratic minimum, and neighborhood/tail estimates in the analytical proof. The originality assessment retains a priority risk from older uninspected full texts. Independent audit has not been performed.
