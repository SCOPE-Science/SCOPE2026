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

# Verification and limits

The independent of implementation steps within the same mathematical package are the universal second-jet kernel calculation, its symbolic nonzero minor, the exponent hexagon area/edge-length calculation, and a direct exact-polynomial check of the contact alternant for eleven small degrees. The accompanying `verify.py` runs these checks in exact SymPy rational arithmetic. The ring computations at generic boundary points and the infinite-contact factorization are justified by the printed semigroup and bialternant proofs in RESULT.md, rather than inferred from computations alone. The verifier's bounded degree checks are supplementary and do not establish uniqueness, prove literature priority, or constitute independent external audit.

For an ordinary reproduction install SymPy 1.10 or later and run `python verify.py`; expected terminal line is `VERIFY_OK`. All methods and source documents are identified in RESULT.md, without relying on ephemeral computational files. No Newton polytope claim about arbitrary other monomial surface families is made.
