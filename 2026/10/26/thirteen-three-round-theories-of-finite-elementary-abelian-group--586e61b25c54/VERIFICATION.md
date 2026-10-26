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

The accompanying `verify.py` recomputes every rank-three type from the full row-reduced-echelon subspace lattice for each small prime and dimension 1, 2, and 3. It evaluates exact one-point-extension sets and checks all 13 resulting classes. A separately implemented direct interpretation of group elements verifies 100 ordered comparisons over ten representative small groups. The code also regenerates the thirteen exceptional rational slopes and checks the determinant bound of 15.

The infinite stabilization step is proved mathematically in `RESULT.md`: all possible third-move atomic diagrams depend on ten explicitly listed expressions, every prime of size at least 17 supplies a generic scalar slope, and every allowed third-move diagram has a witness. Finite tests on several larger primes are diagnostic, not a substitute for this proof. No independent audit or certification has been performed.
