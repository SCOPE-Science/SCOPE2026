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

# Reproducibility and verification

The accompanying `verify.py` script computes nearest feasible corrections via a rational water-filling solution to the weighted simplex constraint, and checks the analytical distortion bound. An independently constructed near-extremal nodal configuration validates sharpness numerically while exact rational inequalities validate finite inputs. The LGL specialization is separately checked for node counts \(2\) through \(10\) using standard Legendre differentiation and quadrature weights.

At preparation, the standalone program passed 2,100 seeded exact-rational nodal cases (including near-boundary families) and nine LGL checks. These checks test code and formulas; no finite enumeration establishes the universal result. The proof's essential analytic steps appear in `RESULT.md`. The method compares only nodal positivity and the weighted \(\ell_2\) distance. It does not independently certify scientific originality, formal-prove the mathematics, or assert validation by a separate reviewer.
