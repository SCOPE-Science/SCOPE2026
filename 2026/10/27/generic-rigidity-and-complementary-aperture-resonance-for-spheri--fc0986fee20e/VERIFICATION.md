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

# Reproducibility and scope

Run `python CHECK.py` using Python 3, SciPy, and standard math functions. The program checks the exact cap-multiplier identity against numerical Funk--Hecke integration (128 comparisons), the complementary-aperture parity formula (1,050 comparisons), finite negative-coefficient examples for irrationally related radii, the positive-coefficient complementary example with a negative mixing weight, and the high-frequency Darboux remainder in dimensions two, three, and four.

The maximal absolute discrepancies in both coefficient identity batches were below \(5.6\times10^{-17}\) in the stated floating-point evaluation. This is bounded numerical corroboration, not a validation of every dimension, radius, or harmonic degree. Infinity claims are proved analytically in `RESULT.md`, particularly the Weyl density limit and strict-positivity parity argument. No independent mathematical review has been performed.
