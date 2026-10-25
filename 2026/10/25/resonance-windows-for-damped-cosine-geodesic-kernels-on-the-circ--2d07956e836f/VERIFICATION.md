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

# Reproducibility and verification

The proof itself is in RESULT.md. The executable `check_coefficients.py` is an optional, standalone standard-library diagnostic for its rational Fourier coefficient formula, the four-inequality rule, and the asymptotic window scale. It intentionally does not present finite sampling as proof of the infinite Fourier statement. It prints the count of deterministic parameter checks, maximal quadrature residual, and frequency-window scalings. Run with `python3 check_coefficients.py`.

The coefficient algebra was also separately simplified symbolically: for \(X=a(1-\sigma q\cos(\pi\omega))\), \(Y_\sigma=\sigma q\omega\sin(\pi\omega)\), and \(R=a^2+\omega^2\), the combined numerator is \(X(R+n^2)+Y_\sigma(R-n^2)\), with strictly positive denominator for \(a>0\). The proof's parity conditions and strict-boundary argument are exact. No computation certifies all infinite modes independently.

**Scientific limitations.** There is no claim for higher-dimensional spheres, vanishing damping, or asymptotic uniformity in damping. One plausibly relevant 2016 thesis could not be inspected in full. Independent audit has not been performed.
