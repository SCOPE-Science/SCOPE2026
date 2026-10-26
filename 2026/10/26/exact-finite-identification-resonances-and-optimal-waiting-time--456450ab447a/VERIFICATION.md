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

# Reproduction and limits

Run the bundled `verify.py` using `python verify.py` (standard library only). It should print `VERIFY_OK 192`. The check carries out actual exact-rational iterations in three coordinates and verifies four distinct resonance settings, several nonresonant multipliers, persistence of the absorbing state, and the rational waiting-time optimum. The theorem for arbitrary dimensions and infinitely many Bernoulli steps depends on the mathematical proof in `RESULT.md`; finitely many executable examples alone would not establish it. No independent audit or external certification has been performed.
