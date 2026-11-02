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

The result follows from the determinant identity, dihedral trace invariance and three exact four-season trace-difference polynomial identities stated in RESULT.md. The proof establishes the infinite parameter range analytically.

The bundled `verify.py` uses Python 3 and SymPy. It passed all three polynomial identities, every permutation for cycles of length one through three, 400 complete 24-permutation exact-rational stress tests, the half-dispersal identity, and the rational sign certificate in the example. Finite tests are corroborative rather than an exhaustive proof. No independent audit or external mathematical certification has been performed.
