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
# Computational verification and limits

Execute `python3 verify.py` using the Python standard library. The checker builds the finite field and its scalar Alexander-quandle multiplication table directly, enumerates every coefficient vector, verifies the quandle-algebra idempotent equation coefficientwise and compares all observed counts with the character-resonance formula. Successful output ends in `VERIFY_OK`.

The eight exhaustive parameter pairs are \((3,2),(4,2),(4,3),(5,2),(5,3),(5,4),(7,2),(7,4)\). Observed counts are \(4,17,17,6,6,6,8,50\), with zero nonzero augmentation-zero idempotents. Additional field-arithmetic tests cover prime orders \(11,13,17,19\), checking Frobenius-resonant exponents. The source code is part of this package; no external corpus, dependencies, or datasets are required.

All direct tests passed in this self-review. Exhaustive small examples cannot prove a universal claim. The unrestricted theorem depends on the finite group-algebra augmentation-ideal proof and Maschke's theorem. No independent audit was performed.
