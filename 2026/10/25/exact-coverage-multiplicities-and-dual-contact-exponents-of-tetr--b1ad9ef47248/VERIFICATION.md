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

# Analytic and numerical checks

The theorem uses the fixed radius domain \(0\le r\le\pi\), unit sphere area \(4\pi\), and tetrahedral dot products \(-1/3\). The spherical cap lens, cover threshold, threefold obstruction, fourfold obstruction, probability-vector inversion and antipodal complementarity are proved in `RESULT.md`.

To reproduce the supplementary finite calculations, run `python VERIFY.py` with Python 3 and no third-party dependencies. The script checks fifteen radii, expected cap-incidence counts, the lens area at covering and hemisphere thresholds, an 80,000-point deterministic spherical quadrature for several radius values, and numerical contact exponents. Its angular quadrature is finite and is neither an exhaustive enumeration of the sphere nor a substitute for the analytic proof. The asymptotic constants come from the local curvature integral and the three-normal equilateral contact geometry, not extrapolation from the finite samples.

No computer algebra system, interval-arithmetic certificate, external independent audit, or theorem prover is asserted.
