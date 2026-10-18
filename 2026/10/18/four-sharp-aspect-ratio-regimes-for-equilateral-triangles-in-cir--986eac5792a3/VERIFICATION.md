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

# Verification of the exact cylinder profile

Run `python3 verify.py` using a standard Python 3 installation. The checker requires no external libraries.

The checker recomputes direct coordinate witnesses for 2,000 positive-height ratios. It verifies all three Euclidean side lengths against the claimed sharp value, membership in both cylinder end caps, and membership in the transverse disk. It separately evaluates minimum enclosing circles of projected triangles on a finite grid, compares 132,000 independently seeded spatial orientations against the formula, and checks exact algebraic branch substitutions using `fractions.Fraction`.

On successful execution the program prints `VERIFY_OK` with the checked counts. The checker does not enumerate every real parameter value or establish an infinite theorem; that role is played by the displayed Heron identity, acute/obtuse circle classification, rational derivative sign, monotonic envelope, and explicit sharp constructions in `RESULT.md`. Its use of a factored area expression avoids catastrophic cancellation for nearly axial (nearly collinear projected) triangles.

The first-source publication date is taken from the original arXiv v1 header, 2010-10-08. Source comparisons and historical uncertainties are documented separately. Independent external scientific validation has not been performed.
