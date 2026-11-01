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

# Reproducible verification and limits

The mathematical proof is contained in `RESULT.md`. Run `python3 verify_spherical_gap.py` from the folder containing the extracted files. Standard Python checks the critical point and differentiation identities. Optional SciPy integration compares the two exact finite-exponent Bessel moment integrals with the two-term asymptotic expression; finite quadrature is illustrative, not an infinite theorem. The tested elementary identities and numerical profile checks completed successfully.

Core mathematical verification: the norm and sharp modal-gap identities are those of [1, Theorems 1.2--1.4] with the explicit Fourier/surface normalization. The peak \(r_*\) exists uniquely in \((\pi/2,\pi)\) by the derivative-sign argument. Beyond radius four, the tail bound forbids a competing maximizer. Strict uniqueness plus the power-law radial tail permits standard Laplace localization with the stated relative errors. Expanding the \(2/q\) power yields the complete displayed \(q^{-1}\) term. The proof is analytic; the script does not provide formal machine certification.

Independent audit: not performed.
