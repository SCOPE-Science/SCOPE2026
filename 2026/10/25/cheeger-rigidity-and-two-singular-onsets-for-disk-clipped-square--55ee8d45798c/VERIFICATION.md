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

# Reproducibility and scientific boundaries

Run `python verify.py` with `mpmath` installed. The checker tests the analytically derived eroded-square intersection area against independent numerical quadrature, solves nine Cheeger-radius equations with 60-digit arithmetic (including both endpoints and the constant plateau), and compares the two sharp onset coefficients across five shrinking scales. Its terminating line is `VERIFY_OK clipped-square Cheeger profile; inner area, quadrature and both asymptotic constants`.

The analytic argument uses the standard planar convex Cheeger inner-parallel characterization, the exact circular-segment integral, and local Taylor expansions near side tangencies and clipped corners. Finite tests support numerical evaluation only; they cannot independently certify the proof for all real radii, novel priority, or an external audit. The report is a self-review, not independent validation.
