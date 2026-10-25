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

The claim's quantifiers, Lindblad normalization, zero-real-part spectral characterization, exceptional fluxes, Fourier pair involution, congruence counting, and site-weight character sums were checked against the complete proof in `RESULT.md`. For the finite-dimensional contraction generator, spectral decay on the dark subspace's orthogonal complement follows from strict negativity of all complementary eigenvalue real parts, not from numerical evidence.

Reproduce finite calculations by running `python verify.py` with Python, NumPy, and SciPy in the same directory as the supplied files. Execution completed successfully: 1,151,916 exact modular pair and numerical Fourier-weight comparisons for all \(3\le N\le120\) and all listed locations and flux classes; 9,471 direct Hermitian spectral projector comparisons across \(3\le N\le24\) and generic-flux cases; maximum recorded projector-weight difference \(9.992007221626409\times10^{-16}\); and 24 direct dissipative propagations with unequal positive sink rates. These are finite checks and cannot by themselves establish the theorem for all sizes or all parameters.

The source comparison covers primary arXiv:2605.08056v1, arXiv:1906.08112, arXiv:2011.13794, and arXiv:0812.3452, with attention to the distinction between single-versus-double sinks and continuous Lindblad absorption versus repeated projective detection. Some general graph-observability literature may be stronger than the inspected materials. Independent audit has not been performed.
