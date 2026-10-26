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

The reproduction command is `python verify.py` with SymPy as specified in `requirements.txt`. The program checks the symbolic quartic numerator, the same-part and cross-part matrix entries, the three exact positive-polynomial certificates (using nonnegative coefficients after transformations on complementary half-lines), three strict rational witnesses, the universal scalar lower bound and derivative, and seven exact rational graph-matrix instances.

The checker's successful completion prints `VERIFY_OK all exact sign, symbolic, and direct rational identities`. This is a deterministic algebraic check, not an infinite-case exhaustive enumeration, proof assistant certificate, or independent assessment. The proof for all integers and all positive real timesteps is in RESULT.md. No external audit has been performed.
