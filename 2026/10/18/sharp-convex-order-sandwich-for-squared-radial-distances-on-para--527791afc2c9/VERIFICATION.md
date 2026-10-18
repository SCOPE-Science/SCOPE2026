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

# Verification and boundaries

The exact edge-mixture representation, symmetric-spreading monotonicity, uniform collinear endpoint, CDF one-crossing and integrated-CDF convex-order steps are fully detailed in `RESULT.md`. The key numerical normalizations are \(\mathbb E Z_P=L^2/3\) and \(\mathbb E Z_P^2=L^4/5-\operatorname{area}(P)^2/12\), the latter also follows from the prior boundary-moment expansion in reference [3].

To reproduce finite cross-checks, install NumPy and run `python scripts/check_convex_order.py`. The checker uses deterministic 160-point Gauss--Legendre quadrature; checks 140 parameter tuples against five nonlinear convex observables and two exact moments; checks the square/rectangle CDF crossing at 7,540 thresholds; and checks hinge expectations on 360 further parameter/threshold tuples. An expected successful line begins `RADIAL_CONVEX_ORDER_CHECK_OK`. Numerical tests are not a proof of the all-parameter inequalities and do not establish priority. The analytical proof handles all positive side lengths, all noncollinear angles, arbitrary continuous convex tests, and the degenerate limit.

The purported sharpness for singular powers is limited to \(-1<p<0\), with integrable needle limit; no claim is made at \(p\le-1\). The theorem does not extend to arbitrary centrally symmetric convex bodies, noncentered sampling or Euclidean dimensions above two without additional arguments.
