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

# Verification

Run `python verify.py` with Python 3 and SymPy installed. It should print `VERIFY_OK`. The script enumerates all 15 pair partitions, checks explicit vanishing and nonvanishing sextics, all 720 root relabelings of both examples, the nonalternation witness, simple vanishing, projective stabilizer, the Weierstrass equation and discriminant.

The computational checks are finite exact checks. They support, but do not prove by themselves, the classification, invariant descent, general fiber-type assertion, or birationality. The proof of these universal statements is in `RESULT.md`. No independent audit or certificate is asserted.
