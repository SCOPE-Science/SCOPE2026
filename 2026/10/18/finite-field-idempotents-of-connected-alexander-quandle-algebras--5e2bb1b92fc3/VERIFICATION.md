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
The proof in `RESULT.md` is independent of computation. Reproduce numerical controls by installing the explicitly declared requirement in `requirements.txt` and running `python verify.py`. The verifier constructs integer Smith matrices for cyclic connected Alexander data, computes the predicted finite-field idempotent counts, and separately exhausts each original multiplication table over the coefficient field. Cases cover 14 cyclic prime-field configurations and a nonscalar two-generator Alexander action over a binary field. An additional direct characteristic-two polynomial-field implementation tests midpoint quandles over orders four and eight. Expected terminal marker: `VERIFIED_ALL`.

Limits: finite enumerations do not prove the theorem for arbitrary groups or fields; the proof must be checked separately. No independent mathematical review has been performed.
