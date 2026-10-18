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

The analytic proof derives the exact diagonal of the orbit-frame operator in the orthonormal monomial basis, then bounds the ratio between adjacent insertion and pre-insertion degrees. Gamma-ratio regular variation converts this into the sharp generator-density inequality. An explicit geometric generator-degree sequence supplies equality for every prescribed positive condition ratio above one; the dyadic ordinary-Bergman example also verifies the global frame bounds directly.

For supplementary finite diagnostics, execute `python bergman_orbit_checker.py` with Python 3 standard library. The script compares exact finite weighted-orbit sums and cumulative monomial weights for twelve parameter settings, then tests 4,095 dyadic coordinates. These finite checks cannot establish asymptotic optimality, completeness, or infinite-dimensional frame bounds; those require the written arguments.

Publication-priority caveat: the relevant Hardy orbit paper, the general frame-index theorem, and the other operator-orbit constructions were inspected to the extent described in the review. Unknown abstract weighted-shift frame-density theorems could yield an equivalent implication. Independent audit and independent mathematical validation have not been performed.
