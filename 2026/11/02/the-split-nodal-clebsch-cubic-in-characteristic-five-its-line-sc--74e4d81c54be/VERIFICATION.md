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

The proof derives the cubic normal form, the six-point blowup, the complete line list, the local Grassmann equations, finite flatness, and the rational-point formula. The companion `verify_clebsch5.py` checks the six rational base points, twenty-one line equations and Plücker keys, both local Jacobian ranks, the nonzero quadratic obstruction, and direct point counts over the fields of five and twenty-five elements.

The computation is exhaustive only for its stated finite checks. The all-extension zeta formula relies on the geometric blowup proof; the relative finite-flat conclusion uses local scheme lengths and the degree-twenty-seven generic fiber, not extrapolation. The local Fano scheme at each of the six singular-node lines has length two; these six supports are not twelve distinct lines. The independent audit remains unperformed.
