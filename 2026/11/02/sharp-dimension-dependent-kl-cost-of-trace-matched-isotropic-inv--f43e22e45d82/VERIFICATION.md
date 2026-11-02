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

The proof is entirely analytic in `RESULT.md`. The available `verify.py` uses Python 3 standard library arithmetic (`fractions.Fraction`, `math`, `random`) with a fixed pseudorandom seed, making finite consistency tests repeatable. Execute `python3 verify.py` in the directory containing the extracted file.

Recorded checks on the packaged source: 2,600 strictly positive rational curvatures; 4,180 random SPD spectra checked against the endpoint formula with equality-attaining endpoint cases; 207 unimodality/integer-localization cases. Total: 6,987 passed. It also outputs four explicitly calculated dimension/contrast benchmarks. These samples cannot verify all real matrices, all dimensions or all contrasts. The universal quantifiers follow from the displayed separate-convexity proof and exact endpoint reductions.

The claimed sharpness is for arbitrary SPD spectral data and the specified ordered KL, not for a finite Lanczos discretization, numerical conditioning or Monte Carlo reliability. Earlier equivalent mean-inequality expressions cannot be ruled out by search alone. No independent mathematical audit or independent validation has been performed.
