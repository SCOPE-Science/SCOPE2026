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

Run `python3 verify_star.py` with the Python standard library. The checker enumerates all admissible best-response successors from every possible center coalition for 8,404 discrete nonsymmetric local-additive cases on two to six vertices, and 7,578 arbitrary monotone discrete hub set-functions on two to five vertices, checking the claimed length bound. It separately reconstructs and checks every strict recipient-consensual best-response step in the quadratic IR witness for three through sixteen vertices, comparing its exact length against the formula.

All these checks completed successfully from the packaged verifier. The proof in RESULT.md, not the enumeration, establishes the theorem for every finite star, arbitrary preference orders and unbounded real utilities. The enumeration does not claim an exhaustive infinite parameter census. Independent validation has not been performed.
