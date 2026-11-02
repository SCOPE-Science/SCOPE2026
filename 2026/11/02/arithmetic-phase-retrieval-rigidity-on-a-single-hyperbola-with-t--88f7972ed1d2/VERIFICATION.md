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

The proof in `RESULT.md` supplies the all-degree rational invariant-field argument; it is not inferred from finite numerical tests. Run `python verify_hyperbola.py` with Python 3 and SymPy. The test performs exact symbolic identities for four rational-angle hyperbolas, explicit modulus collisions and the Laurent sampling degree bound, and checks one rational-coefficient nonresonant angle. It does not independently certify the originality of the theorem or its general proof. No independent audit has been performed.
