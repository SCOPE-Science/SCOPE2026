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

The proof in `RESULT.md` contains direct offset-interval classification, elementary angular integration, a strict Jensen equality analysis and a compact-moment inversion argument. No numerical data are used in place of a proof of the infinite-dimensional conclusions.

Executable corroboration: `python verify.py`. Tested configurations: unit disk, \(2\times1.2\) rectangle, ellipse with semiaxes \(1.4,0.7\), and two positive-curvature harmonic support-function examples. At three heights, independent normal-integration agrees with the closed probabilities within \(3.5\times10^{-4}\); weighted Monte Carlo with 420,000 samples per configuration agrees within \(0.006\). Explicit equality of the height profiles for two nonequivalent harmonic examples and strict comparison with the constant-width disk are checked. The first two even width moments are checked against the large-height expansion. These finite checks do not prove originality or historical priority.

Limits: the inverse profile determines the distribution of widths, not the base up to congruence; exceptional tangential planes are null. No independent mathematical audit has been performed.
