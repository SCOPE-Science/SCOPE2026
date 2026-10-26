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

# Verification and reproducibility

The analytic proof in `RESULT.md` is the source of the all-exponent theorem. With NumPy and SciPy installed, run `python verify_torus.py` in the directory containing the standalone checker. The program evaluates the exact separable endpoint coefficients, a normalized periodic FFT, and the analytic antipodal integral independently. It also displays a negative discrete Fourier coefficient on a finite sampling grid at one nonadditive exponent.

At damping \(a=1\), the exact even-axis coefficient constant for the Euclidean member \(p=2\) is numerically \(-0.00849361549034\). On a \(128\)-by-\(128\) uniform two-torus grid, the normalized frequency \((24,0)\) coefficient is approximately \(-4.35569586777\times10^{-6}\). The checker printed `ALL TESTS PASS` on the package script's actual path.

The numerical grid does not prove the uniform theorem, and small Fourier coefficients near \(p=1\) may remain positive at modest frequencies before the eventual negative asymptotic region. The strict positive-definiteness and nonadmissibility claims rely instead on exact Fourier factorization, absolute continuity of the radial marginal derivative, and the Riemann–Lebesgue lemma. No independent mathematical audit has occurred.
