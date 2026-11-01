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

# Verification

The standalone Python checker `verify_weighted_c4.py` requires Python 3 and SymPy and was executed successfully from this package. It forms all supporting facet planes through triples of generating points using rational arithmetic, determines the exact facet sets, and constructs the linear edge-parallel deformation equations. Its printed result is:

`PASS: exact supporting faces, deformation ranks and two-equality face tables`

For eight-vertex rational samples, the summand-vertex deformation-space dimensions, including three translation directions, are 4 in the generic and one-quadrilateral-pair cases, 5 in both distinct two-quadrilateral-pair samples, and 6 in the all-equal case. The checker separately verifies six-vertex collapse samples and the full four triangular/four quadrilateral facet lists in the two-pair cases.

These finite exact calculations are diagnostics for the analytical theorem, not proof by sampling. The universal correctness argument uses explicit inequalities, the facet sign equations, the classical connected-triangle criterion, and the decomposition formula.

Independent mathematical audit is not performed. Independent publication-priority certification is not claimed.
