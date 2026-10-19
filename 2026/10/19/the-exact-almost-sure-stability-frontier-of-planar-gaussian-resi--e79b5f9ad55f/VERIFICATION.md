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

# Verification of the planar Gaussian recurrence

The included `check.py` independently computes the exponent by direct, split integral quadrature; locates the unique stationary point and unique zero; verifies that the first derivative changes sign across the stationary point; checks a monotone upper/lower Riemann-sum gap at the unit step; and performs 70,000-step normalized Gaussian recursions at four step sizes with a fixed seed. The formula and numerical tests are accompanied by a mathematical proof using exact angular averaging, independent log increments, a strictly monotone derivative ratio, the strong law of large numbers, the law of the iterated logarithm, and Gaussian fourth moments.

The proof's almost-sure statements are not numerical certifications. Integral approximations alone would not prove uniqueness, and finite trajectories alone would not establish almost-sure convergence or critical oscillation. The theorem assumes stationary, noiseless updates in precisely two dimensions. There has been no independent audit.
