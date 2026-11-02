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

The bundled `verify.py` was executed from its package directory. It independently constructs the source algorithm's update matrices and exact probabilities, expands the quartic moment operator, verifies the determinant factorization and the \(r=1\) characteristic polynomial, and checks 36 exact finite-path second- and fourth-moment identities. It also checks the critical algebraic root and samples the spectral regions numerically. Output: `VERIFY_OK: exact quartic operator, determinant, r=1 eigensystem, 36 exhaustive finite-path moment identities, sharp crossing samples`. The proof's continuity, positive eigenquartic and asymptotic claims are mathematical arguments; finite checks alone do not establish them. No independent external audit was performed.
