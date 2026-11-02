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

The bundled `verify_torsion.py` uses exact symbolic arithmetic and returns `VERIFY_OK` after checking the quartic-cover discriminant, its degree-four residual factor, the parameter-discriminant factorization, common roots of the two cubic generators, and the quartic invariant controlling fiber types. It also checks several exact parameter specializations. The script was run successfully before packaging. No automatic finite experiment establishes the infinite family, and no independent audit has been performed. The infinite exclusion of odd and order-four torsion is supplied by the stated geometric height argument.
