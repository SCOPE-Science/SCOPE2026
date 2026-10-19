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

# Verification procedures and limits

Run `python artifacts/verify.py` after installing `artifacts/requirements.txt`. The program builds the finite tight-binding Hamiltonian and independently solves the matrix Lyapunov equation for left and right sinks. It checks every entry of the explicit absorption effect, its residual, positivity, and complete absorption across several finite sizes and nontrivial asymmetric rate triples. It separately performs exact-rational checks of the symbolic entry identities and tests the unique maximizer. The extracted verifier returned `VERIFY_OK 309 matrix/effect checks + 24 exact rational identities`. The exact theorem for arbitrary finite length is proved by the identities in `RESULT.md`, not by finite test counts or numerical precision.

No external independent audit or formal proof certification has occurred.
