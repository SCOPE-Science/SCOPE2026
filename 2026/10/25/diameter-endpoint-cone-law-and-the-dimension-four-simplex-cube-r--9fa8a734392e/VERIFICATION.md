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

The analytical proof controls the complete class of fixed full-dimensional convex polytopes: finite diametral vertex pairs, cone-cap positivity and compactness, a uniformly bounded blow-up, a Dirichlet integral, and exact shape coefficients. The accompanying `verify.py` contains independent coordinate reconstructions and seeded importance-sampling checks for the regular tetrahedron and cubes in dimensions three and four. Executing the code produces `ALL_DIAMETER_TAIL_GEOMETRY_CHECKS_OK` after all assertions.

The comparisons `R_3=32/27` and `R_4=45/64`, and monotonicity for every integer dimension from two upward, are proved algebraically, not inferred from numerical samples. Finite sampling does not independently certify the limiting theorem or historical priority. Formal independent audit is not performed.
