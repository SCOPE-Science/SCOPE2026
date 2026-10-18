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

The symbolic certificate `kodaira_suluyer_checker.py` checks polynomial identities and factorization boundaries over \(\mathbb Z[a,t]\) with SymPy, not by numeric interpolation. It also checks the two cusp specializations over \(\mathbb Q(\sqrt3)\). The full geometric proof requires the ordinary-node/cusp local equations, simple-basepoint blow-up, and Kodaira fiber identification stated in RESULT.md. The parameter-degenerate boundary is excluded and not certified. Full historical uniqueness and independent validation have not been established.
