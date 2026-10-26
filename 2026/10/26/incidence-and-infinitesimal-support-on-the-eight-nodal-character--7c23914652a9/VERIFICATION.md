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

# Computational verification

Run `python3 verify.py` using the Python 3 standard library. Expected final marker: `VERIFY_OK`. The program enumerates all 7462 distinct two-dimensional F9-subspaces in reduced row-echelon form, tests all points on each line, independently checks the quartic formula, computes the eight F9 singular points, enumerates line intersections and graph degrees, and differentiates five quartic restriction equations in each Grassmannian chart to obtain exact tangent nullities. A second point-pair census provides a differently indexed exhaustive check of the 48 lines. Assertions check the 7-to-1 split among eight two-node lines and uniquely identify `x0=x2=0`. All computations are finite, field operations exact, and no extension-field uniqueness or geometric line completeness is inferred solely from these counts. Independent audit has not been performed.
