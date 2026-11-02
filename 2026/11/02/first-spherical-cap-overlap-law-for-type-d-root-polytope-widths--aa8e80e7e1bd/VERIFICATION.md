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

## Reproducibility and scope
Run `python verify_width.py` with Python 3, numpy, scipy, and mpmath installed. The checker is standalone and uses no external downloads, private paths, or ancillary archived files. It evaluates the exact CDF on 13 points by a separate one-dimensional spherical-area quadrature, tests the three-dimensional upper-tail cap expression, compares \(n=3\) small-overlap coefficients by direct exact CDF subtraction, and uses the independent uniform-disk marginal for an \(n=4\) spherical-lens check. It also evaluates monotonicity on a 3000-step grid. A successful run prints one PASS line.

The general \(n\)-dimensional theorem is proved analytically in RESULT.md; neither the quadratures nor their numerical tolerance are an infinite proof. Full manuscript inspection of one closely related 2026 density-framework paper remains outstanding, so scientific-priority limits are retained despite the self-contained mathematical derivation. No independent scientific audit was performed.
