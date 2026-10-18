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

Execute `python3 verify.py` in this directory. The standalone verifier enumerates the complete required word sets for lengths 3 through 13, builds and checks Eulerian covering cycles from the theorem's explicit bijection, checks that each built cycle contains the forbidden triple, and compares independently optimized shortest-path assignment costs through length 10. It also computes the rational generating-function coefficients by integer recurrence. The execution in this package's preparation returned:

`VERIFY_OK cyclic_hosts_k=3..13 independent_assignment_optimality_k=3..10 generating_function_coefficients=3..13`

The infinite claims are supported by the proof in RESULT.md. Finite checks cannot establish them alone. Independent scientific audit has not been performed.
