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

# Verification evidence and limits
The package includes `verify_normal_conic.py`. Its standard-library rational polynomial implementation checks two identities (the determinant relation and the completion-of-squares relation) without floating point arithmetic, and checks the relevant weighted degrees. The checker was executed from its actual package file, and returned `VERIFY_OK`.

The decisive infinite statements are proved mathematically in `RESULT.md`: irreducibility by Gauss's lemma and a monic polynomial quotient, and nonsquareness by rational field parameterization and independence of the two quadratic square classes. A program checking polynomial identities alone does not prove irreducibility or monodromy. No independent audit or external certification has occurred.
