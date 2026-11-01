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

# Reproducibility and scope

The accompanying `verify.py` is complete Python 3 standard-library source. Run `python3 verify.py` to recompute exact rational Gram inverses, strict positivity, the exact Landau polynomial relation, the sharp constant, and finite complex phase–shape identities. The saved artifact was executed and reported `PASS 1120 supplementary exact and numerical assertions`. Complex floating-point equalities are checked with stated relative tolerance. The proofs of all-order strict positivity, universal equality classification and the deficit identity are mathematical arguments in `RESULT.md`; finitely many program tests do not establish them. No external proof assistant or independent audit was used.
