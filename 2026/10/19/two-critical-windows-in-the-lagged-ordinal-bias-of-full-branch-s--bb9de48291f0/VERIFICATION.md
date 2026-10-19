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

The theorem is established analytically through an exact inverse-cylinder identity, a convergent branch-mode expansion, an explicit exponential remainder bound, algebraic comparison of the two dominant spectral radii, and parameter-window Taylor limits. The published accompanying `verify.py` has no external dependencies and uses Python's exact `fractions.Fraction` type.

The following command was run against the packaged source file:

`python verify.py`

It returned:

`VERIFY_OK: 54 exact rational cylinder-to-three-mode bounds; 36 independent finite-k power-series estimates; symmetric exact probabilities and resonant inequalities`

The 54 cylinder checks enumerate all two-branch itineraries through length nine for six different rational parameters. The 36 comparisons additionally test a separately evaluated 100-term inverse-branch series against its rigorous geometric truncation bound. Exact closed formulas are checked at the symmetric parameter and at the resonance. Results are finite tests and do not constitute exhaustive proof over the real parameter space or over all lags; the analytic proof in `RESULT.md` carries those quantifiers.

Literature priority remains subject to independent examination, particularly possible specializations of general methods for computing interval-map ordinal distributions and an unavailable 2022 full text on periodic points of skew tent maps.
