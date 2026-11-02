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

The file `verify.py`, included with the result, is a standard-library-only exact checker. It tests every labeled orientation on 21 small multicycle instances (491320 individual orientations), compares independent direct all-good EFX evaluation with the transfer trace, and verifies two claimed characteristic factorizations using integer Newton identities. Its expected terminal marker is `VERIFY_OK direct_cases=21 exhaustive_orientations=491320 charpoly_cases=3`.

The mathematical proof is the cyclic-local-constraint bijection and finite characteristic polynomial computation. Finite exhaustive checks cover their stated cases only; the general formula for unbounded cycle length and multiplicity relies on the proof. No independent validation or external certificate has been performed.
