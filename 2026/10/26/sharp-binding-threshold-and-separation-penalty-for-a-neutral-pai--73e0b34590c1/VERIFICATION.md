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

The analytical chain has been reconstructed with the normalization \(\varepsilon(k)=2\sum_{j=1}^3(1-\cos k_j)\). The free band is \([0,12]\); the two-site determinant is \(1-\lambda^2(G_0^2-G_r^2)\). Each factor \(G_0\pm G_r\) is a strictly decreasing positive Fourier integral, so at most one eigenvalue lies below the band. The reflection-and-staggering identity transfers this result to the upper band. A threshold null vector has a nonzero zero-momentum numerator, which is integrable but not square integrable after division by \(\varepsilon\). The local Green singularity gives \(G_0(0)-G_0(\kappa)\sim\sqrt\kappa/(4\pi)\), and the far-field Fourier transform gives \(G_r(0)\sim(4\pi\lVert r\rVert_2)^{-1}\). The stated quadratic onset and inverse-square penalty follow algebraically.

The included Python file `checks.py` is standalone and standard-library-only. It computes heat-kernel Bessel integrals, checks the exact nearest-neighbor Green identity within numerical tolerance, and prints corroborating near-edge and distance scalings. Reproducibility command: `python checks.py`. These finite computations are not used to establish existence, uniqueness, or the limits. The result intentionally excludes embedded eigenvalue classification, scattering data and multi-defect configurations. Independent assessment has not been performed.
