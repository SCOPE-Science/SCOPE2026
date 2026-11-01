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

# Verification and scope
The included `verify.py` was run on the exact package's included executable content with Python and SymPy. It printed:

`VERIFY_OK symbolic_2nd_and_4th_moments, Heron, inversion, exact_equal_area_example`

It checks the nine ordered side-pair integrals separately for degrees two and four, symbolic equality to the symmetric-polynomial formulas, Heron's relation, both inverse identities, and an exact algebraic pair of noncongruent triangles sharing the perimeter, area and second moment but not the fourth.

The universal proof is given analytically in RESULT.md: conditional edge integrals, symmetric collection, Heron's formula, and the fundamental theorem of algebra for the side-root polynomial. Program checks verify the symbolic algebra, not mathematical originality or independence. No external mathematical certification has been performed.

The denominator of the inverse formula is nonzero only for positive area; no degenerate or finite-sample claim is made. The supplemental source comparisons and their limitations are documented in REVIEW.md and AUDIT.json.
