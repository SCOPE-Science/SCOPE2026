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

# Reproducible checks and limits

The analytic result is derived from an exact decomposition of the Gaussian surface measure into coordinate-facet contributions. The derivative sign is controlled globally by the strict concavity, for positive translation, of \(t\mapsto(a-\Lambda)\tanh(at)-t\). Both boundary cases and the sharp quartic transition were checked symbolically from that derivative.

Execute `python3 verify.py` using a Python 3 standard-library interpreter. The tested program reports `PASS: 3046 checks; Gaussian facets, derivative, global phases, and critical scaling.` It includes direct numerical quadrature of the Gaussian density over individual facets of two- and three-dimensional boxes, finite-difference derivative checks, 280 seeded random dimension-and-halfwidth configurations, and near-critical scaling tests. Root finding uses bracketed bisection; close-to-machine-precision boundary cases use the limiting endpoint when the distinguishable positive root merges with it numerically.

Numerical checks have finite scope and floating-point error. They do not establish uniqueness or infinite-dimensional extrapolation: uniqueness for each finite \(d\ge2\) follows from the analytic proof. No independently performed audit, historical-priority certification, or external proof assistant check is asserted.
