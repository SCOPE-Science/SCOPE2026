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

# Reproduction and verification limits

Execute `python check.py` with Python 3 and no dependencies beyond the standard library. Expected output: `ALTERNATING_CYCLE_RATIONAL_CHECK_OK 8`.

The program uses `fractions.Fraction` to recompute the optimal diagonal quadratic coefficients, the two exact dual-norm constraints, the two extremal endpoint energies, the closed squared-distance formula and reciprocity at eight rational weight ratios. It also compares the resulting minimum to a finite grid of other scalar parameters. The inequalities are exact over those rational values; this does **not** constitute exhaustive verification for all real parameters.

The continuous proof in `RESULT.md` relies on exact Lipschitz edge-difference coordinates, averaging over the full coordinate-sign isometry group, endpoint maximization of a convex quadratic, Cauchy–Schwarz duality, and a unique crossing of one increasing and one decreasing real rational function. No computational approximation or external theorem about unknown ellipsoids is assumed to prove the global optimum.

Bibliographic comparison is limited to the named accessible primary texts and the searched publicly indexed results. Independent mathematical and bibliographic review has not been carried out.
