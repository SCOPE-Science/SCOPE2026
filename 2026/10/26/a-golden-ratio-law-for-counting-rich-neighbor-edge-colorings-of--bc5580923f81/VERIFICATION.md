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

# Verification scope

The accompanying `verify.py` uses only standard Python modules. It reconstructs the definition of the 24-state transfer matrix and checks strong connectivity from all states, exact integer characteristic-polynomial equality via Newton identities, coprime closed-walk lengths three and five, and independently enumerates all named palette assignments for cycles of lengths three through ten. Its recorded output is `verification_output.txt`; the final line is `VERIFY_OK`.

The unrestricted trace identity follows from a direct sign-word bijection, not finite extrapolation. Perron–Frobenius plus the characteristic factorization gives the infinite asymptotic. The checks do not establish bibliographic priority or independent mathematical validation.
