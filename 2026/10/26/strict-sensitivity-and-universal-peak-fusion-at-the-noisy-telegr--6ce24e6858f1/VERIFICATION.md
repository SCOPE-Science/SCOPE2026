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

## Analytical checks

The displayed Kummer equation is obtained by differentiating the exact hypergeometric beta integral and substituting \(G_q(z)=\sqrt z F_q(z)\). At any stationary point the sign of \(G_q''\) is strictly negative for \(0<q<1\), which establishes both unique simple critical curvature and a strictly positive implicit-function denominator. Differentiating the beta-tilted law gives the covariance numerator, which is strictly negative. Heat evolution gives the exact fourth-derivative sign and the constant \(\sqrt3\).

## Numerical checks

Run `python check.py` with NumPy and SciPy. The script tests six positive switching rates, four peak-splitting offsets, and five rates for analytic sensitivity against finite differences. Its final endpoint-log covariance integration uses an endpoint-adapted quadrature, rather than an inaccurate polynomial quadrature against a singular logarithm. Observed sensitivities were negative in all five parameter tests; the maximum absolute finite-difference discrepancy was below \(6\times10^{-8}\).

## Limits

Finite quadrature and solver success is not an infinite-domain proof. The claimed quantifiers are supplied by the analytic argument in RESULT.md. No external independent scientific audit has been performed.
