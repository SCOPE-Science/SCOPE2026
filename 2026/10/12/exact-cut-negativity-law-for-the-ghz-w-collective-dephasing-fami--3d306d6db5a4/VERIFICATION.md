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

The universal proof is analytic and is given in `RESULT.md`. The finite replay in `verify.py` constructs representative states, partially transposes one qubit, diagonalizes the real symmetric matrix with a standard-library Jacobi routine, and compares the resulting trace-norm negativity with the closed formula. It also checks the exact discriminant identity and positive derivative on representative interior points.

Finite replay is supplementary and is not used as an infinite proof. The result concerns ordinary one-versus-two negativity only; genuine multipartite negativity is not computed.
