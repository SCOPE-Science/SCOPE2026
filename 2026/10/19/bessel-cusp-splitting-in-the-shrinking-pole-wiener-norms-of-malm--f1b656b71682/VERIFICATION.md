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
# Verification
The derived Wiener-algebra expansion is proved analytically, not inferred from computation. The optional `CHECK.py` program independently samples the centered rational function at 8192 equispaced phases, takes a discrete Fourier transform, and compares Fourier absolute sums with a Bessel series and its first correction. It also isolates the positive roots of the signed mode coefficients for orders 0 through 3 at sample sizes 80, 160 and 320 and tests the predicted root displacements. This program requires NumPy and SciPy. Discrete Fourier transforms and finite computations cannot establish the all-order theorem, and the proof's local uniqueness applies only to the specifically named modes. The 2017 and 2026 primary mathematical papers were compared through their full publicly available HTML versions; the classical Bessel facts were checked against the NIST reference.
