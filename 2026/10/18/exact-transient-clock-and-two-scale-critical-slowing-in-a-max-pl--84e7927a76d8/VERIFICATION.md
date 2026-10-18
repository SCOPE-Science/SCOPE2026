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

# Reproduction
Run `python3 verify.py` using only the Python 3 standard library. The script uses exact `fractions.Fraction` computations and checks the two-dimensional map's first original-time return or capture against the predicted piecewise formula; it then directly iterates the map to its first hit of the distinguished point and compares with a separate survivor-interval computation. It also verifies survivor lengths and left/right terminal mass ratios using exact arithmetic.

The completed package's `verify.py` passed 5,856 check units over six feedback strengths (\(11/10,5/4,3/2,2,3,5\)), three positive scales (\(1,2,7/3\)), grids and branch boundaries. It does not independently establish the infinite-parameter claim. The exact roof derivation, induction on survivor intervals, geometric-length identities, and asymptotic analysis are supplied in `RESULT.md` and are the bases of the mathematical conclusion.

No independent audit has been performed.
