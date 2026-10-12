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

# Verification and limits

The analytical proof uses total-variation data processing twice, exact splitting over the four disjoint label cells, and a two-term signed-measure tensor telescoping inequality. These are valid on arbitrary measurable spaces. The three-symbol witness reduces both distances to exact finite sums and supplies the sharp limiting ratio.

Run `python3 verify.py` from the package directory using only the Python standard library. The script checks 398 distinct rational witness parameters and all 10,000 four-law quadruples from the three-category rational simplex of denominator three; it reconstructs both the lifted-label equality and the universal inequality with exact fractions. Its expected output is `VERIFY_OK: 31592 exact-rational assertions` (398 times four plus 10,000 times three). Computational checks are finite sanity tests, not proof of the universal result.

This document does not assert independent evaluation, authorship certification, or absolute publication priority. The theorem establishes only the optimal two-coordinate constant; the sharp problem for larger numbers of coordinates remains untreated here.
