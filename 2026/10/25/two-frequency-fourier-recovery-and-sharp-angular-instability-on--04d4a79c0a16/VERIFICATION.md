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
# Verification record

The theorem is proved analytically by exact spherical-harmonic reduction, a sign-definite logarithmic derivative obtained from the Bessel canonical product, and a fixed-argument large-order Bessel expansion. No finite experiment is used to infer the sign in infinitely many channels or to claim a uniform inverse.

`checker.py` is a standalone high-precision numerical regression check. Its actual output is retained in `checker_output.txt` and its sole external dependency is `mpmath` as documented in `requirements.txt`. Run from the extracted artifact directory using `python checker.py`. The script checks dimension \(2,3,5\) matrices with specified strict low-frequency configurations, degrees \(0,1,2,6,12,24,36,48\), all negative determinants and asymptotic leading constants at degree \(48\), and five independently quadrature-evaluated spherical plane-wave coefficients in dimension \(3\).

The numerical checks test normalization, determinant sign in sampled cases, and limiting constants. They do not validate arbitrary real radii by enumeration, quantify finite-data noise performance, or provide external independent certification.
