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

# Verification notes

The standard-library program `verify.py` independently implements the neighbour-count update on every labelled configuration for sizes \(3\) through \(9\), thresholds \(1\) through \(N+1\), and computes eventual primitive periods by detecting repeated configurations. It checks the four claimed orbit categories, exact counts, the exhaustive partition of \(3^N\), and the sharp existence criteria for three-cycles and two-step transients. The full run completed with `PASS: 280449 vertex-level states across all threshold tests.`

The analytical proof, not the finite experiment, establishes universality. The probabilistic statement follows from the standard two-dimensional multinomial central and local limit theorems. The covariance determinant is \(1/27\); the limiting Gaussian density at the origin is \(3\sqrt3/(2\pi)\). The small-window triangle has area \(9\delta^2/2\), giving the coefficient \(27\sqrt3/(4\pi)\). At the exact integer boundary \(N=3m+r\), there are \(\binom{r+2}{2}\) admissible near-balanced count triples, giving the stated three arithmetic amplitudes.

No claim is made about independent audit or verification by an outside party. No large-system enumeration is represented as exhaustive beyond the tested sizes.
