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
The proof is analytic. `verify.py` provides exact-rational supplementary replay. It checks the finite integer maximization against the floor/ceiling candidate rule for many dimensions and rational condition numbers, checks the continuous Kantorovich-type envelope, and verifies the exact equality witness \(A=I+\tfrac12\mathbf1\mathbf1^{\mathsf T}\) in dimension four. The finite sweep is not used to infer the universal theorem. Schur--Horn attainability and the one-variable endpoint argument are mathematical proof steps, not numerical certificates.
