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

The analytic proof determines the switched graph exactly, so the universal theorem does not depend on finite computation. The bundled `verify.py` is an independent finite stress test: it constructs adjacency sets, performs the switch edge by edge, recognizes complete bipartite outputs by traversal and direct adjacency checks, tests the identity criterion and counting formula, and checks the explicit nonclosure witness.

Final replay output:

`ALL CHECKS PASSED; parameter_cases=33; selectors=7684; iss_selectors=2790; a,b_range=1..6 with a+b<=10`

The computation covers all selectors for the stated finite range only; it is not used as an infinite proof.
