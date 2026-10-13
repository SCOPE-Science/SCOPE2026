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

The analytic proof uses the decomposition of squared error into within-component distortion and a between-component variance penalty. At any proposed gap centroid, both component masses in the middle cell are strictly positive. The inequality \(AB/(A+B)\ge\min(A,B)/2\) combined with \(G\ge L/\sqrt2\) makes the penalty strictly exceed the smaller splitting gain, and the remaining gain is bounded by the best pure two-plus-one midpoint allocation.

The standalone script `verify.py` was executed from its actual package directory. It checks 2,187 rational test configurations exactly for unit support length and gaps \(3/4\), \(1\), and \(2\), plus an independent integral for a small-gap centroidal configuration. These finite calculations are sanity checks only; the universally quantified theorem is proved analytically. The certificate does not address gaps below the stated sufficient threshold, two-point quantizers, or arbitrary unequal component lengths.
