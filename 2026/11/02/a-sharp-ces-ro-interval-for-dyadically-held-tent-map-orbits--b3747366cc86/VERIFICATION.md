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

Run `python verify.py` with Python 3; only the standard library is required. The program uses `fractions.Fraction` throughout and reports 71,844 passing exact rational consistency checks. It evaluates the time-sum bound across rational seeds and complete dyadic blocks, tests the affine calibration at exact rational points, verifies the right inverse-branch identities, and evaluates its finite discounted sums using a separate closed expression.

The proof in RESULT.md supplies the crucial infinite argument: a two-branch affine inequality telescopes for every time horizon, an explicit right-branch backward orbit has discounted mass exactly \(4/5\), and dense forward orbits shadow finite pieces of that backward orbit and the zero fixed point at arbitrarily late times. The continuum of subsequential Cesàro limits follows from vanishing successive average increments. The checker does not establish uniformity for all real initial conditions, almost-sure density, or the infinite limits by finite enumeration.

No independent audit or third-party certification has been performed. Historical novelty is based on compared accessible scientific sources, not an exhaustive search of all published and unpublished work.
