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

The standalone `verify_branch.py` uses symbolic exact arithmetic and checks the Jacobian, monic integrality relations, resultant, quartic discriminant factorization, specialization at \(a=0\), and simple branch values on the monodromy witness line. It is executed using a fresh extraction from the final record.

The finite-degree, irreducibility, singular-locus, and monodromy assertions also require the written algebraic arguments; a symbolic run alone does not prove these global assertions. No independent audit has been performed.
