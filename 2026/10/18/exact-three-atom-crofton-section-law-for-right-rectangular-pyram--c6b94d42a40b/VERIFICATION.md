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

# Reproducibility and verification
Run `python3 verify_rect_pyramid.py` using Python 3.9 or newer and the standard library. This evaluates the complete law at 11 right rectangular pyramid shapes, checks two angular integral identities by 10,000-panel midpoint quadrature, and compares the exact 3-, 4-, and 5-sided frequencies with 75,000 random intersecting plane draws per shape. A uniform sphere normal is drawn, an offset is drawn uniformly across the support interval for that normal, and each sample is importance-weighted by the support width. This corrects for the otherwise nonuniform orientation distribution conditional on meeting the body.

The recorded completed check produced:

`CROFTON_RECTANGULAR_PYRAMID_OK 11 cases 825000 orientation-offset samples maximum_discrepancy 0.00440773`

All computed integral comparisons satisfied absolute discrepancy under \(2\times10^{-8}\) and all frequency checks satisfied absolute discrepancy under \(0.013\). The random simulation has sampling error and does not certify any infinite quantification. The analytic argument is supplied in `RESULT.md`. Independent mathematical audit has not been performed.
