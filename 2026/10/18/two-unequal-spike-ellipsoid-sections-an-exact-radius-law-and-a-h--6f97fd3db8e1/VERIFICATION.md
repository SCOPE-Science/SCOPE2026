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

# Reproducibility and limits

Run `python3 check_two_spike.py` with Python 3. No external modules or data are required.

The fixed-seed checker generates hyperplanes in dimensions three, four, six, and eight and evaluates the smallest eigenvalue of the full restricted ellipsoid quadratic form by independent orthonormal-basis construction and Jacobi rotation. It compares those radii with the analytical two-by-two reduction for 420 configurations, checks the determinant-event description and coordinate-normal boundaries, and evaluates a Gaussian critical sample and the supercritical tail coefficient by deterministic Simpson integration. Its successful execution ends with `VERIFY_OK`. Numerical tests do not certify a uniform bound, a distributional limit, or exact originality; those conclusions are supported by the analytic derivations in `RESULT.md`.

All hyperplanes are through the ellipsoid center. The infinite mean describes only the limiting scaled random variable, not any finite ellipsoid section. Historical priority beyond the inspected sources has not been independently established.
