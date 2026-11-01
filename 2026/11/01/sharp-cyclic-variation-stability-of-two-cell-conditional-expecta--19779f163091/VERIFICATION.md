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

The proof in `RESULT.md` is analytic. Its critical equalities can be checked by expanding both class means and applying cyclic summation by parts. Extremizers are proper interval indicators, so no infinite-dimensional limiting or unproved optimization step is used.

Run the standalone checker with `python check.py` using the standard Python 3 library. The checker performs exact-rational comparisons of the prefix-walk norm and the maximum over every proper cyclic-interval indicator for 2010 color/weight instances; it tests balanced-run rigidity, the sharp six-point example, and concentration toward the nonattained upper boundary. A passing finite enumeration is supplementary evidence only.

For any integer \(n\ge3\) and positive masses, the general proof depends only on: (i) two class-mean outputs and exactly \(2r\) color-changing edges; (ii) the zero-sum cyclic gradient identity; (iii) the sharp midpoint estimate for the signed prefix-sum pairing; (iv) equality of positive and negative run increments; and (v) continuity in strictly positive masses. Independent audit has not been performed.
