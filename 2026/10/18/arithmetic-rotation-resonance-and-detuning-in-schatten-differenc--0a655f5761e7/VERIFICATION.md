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

# Reproducibility and verification limits

The exact singular spectrum is obtained by differentiating the normalized monomial basis and observing mutually orthogonal images. The one-dimensional decay sum gives the uniform boundary reduction. Rational detuning is checked by splitting the series into residue classes, and irrational/rapid detuning by Fourier approximation with geometric-sum cancellation. The explicit quartic example follows by integrating its finite Fourier polynomial. All of these are analytic steps stated and proved in `RESULT.md`.

The bundled `checks/resonance_check.py` runs with Python 3.10+ and the standard library. It checks 36 monomial coefficient identities, five scaled finite sums against their limiting integral profiles (including noninteger \(p<1\)), exact rational/irrational quartic limits, and the closed quartic crossover evaluation. Numerical agreement at finite contraction is not by itself proof of any limiting theorem. No independent audit has been performed.
