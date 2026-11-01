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
The proof of the covariance identity reduces the perpendicular cross-sectional moment by integration by parts with vanishing boundary terms. The strict monotonicity uses the negative covariance between the size-biased coordinate and a strictly decreasing logarithmic score. Both steps hold for every real separation \(0<a<1\) and every integer dimension \(n\ge2\). The endpoint constants are derived from beta integrals, not from numerical extrapolation.

Run `python verify.py` with Python 3.10+ after `pip install -r requirements.txt`. Its numerical integrations use 65-digit `mpmath` arithmetic; exact-rational dimension-three computations use Python's standard library. It checks the direct perpendicular-section moment separately from the integration-by-parts expression and reconstructs the three-dimensional polynomial coefficients. On the packaged code the observed output was: `PASS: 412 exact-fraction and high-precision analytic-quadrature checks.`

These checks supplement rather than certify the analytic proof. Numerical comparisons do not establish universal inequalities, originality, or independence. All claims outside the domain of congruent-ball intersections remain unproved. No independent audit has been conducted.
