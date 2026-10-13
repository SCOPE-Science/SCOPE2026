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
# Mathematical and numerical checks

The result is proved analytically by a normalized Fock expansion, a generating-function derivation of the Weyl characteristic, Laguerre-Gaussian Fourier inversion, exact integration over the negative intervals, and a positive derivative bound for the ratio of two Laplace integrals. The proof establishes the continuous three-parameter domain; numerical experiments cannot establish universal monotonicity or exact uniqueness.

Run `python verify.py` after installing the versions in `requirements.txt`. In the provided environment, this executed successfully:

`VERIFY_OK input_fock_characteristic=36 independent_hankel=40 integrated_volume=12 ratio_samples=200 thermal_phase_pairs=12 crossing=0.301380551722202`

The Fock-characteristic comparison uses a truncated sum of 240 terms with checked omitted probability mass below \(10^{-12}\) in each tested case. Hankel integration independently reconstructs the Wigner values at several phase-space radii, including a nonzero thermal bath and both positive/negative Wigner regimes. Negative-volume quadratures integrate the exact disk and annulus intervals. The root check uses a floating-point solver and is not a certified interval proof; analytical endpoint inequalities and global derivative positivity are the proof of existence and uniqueness. The sampled ratio monotonicity is a diagnostic only. The theorem excludes squeezing, arbitrary channels, imperfect additions and energy-matched comparison.
