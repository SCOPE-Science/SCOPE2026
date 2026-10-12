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

# Verification record

The exact verification is the four-step integral argument in `RESULT.md`: the free module decomposition, the prime-order cokernel, the Smith normal form, and fixed-point-to-cycle telescoping. The accompanying `verify.py` independently enumerates all states in bounded cases; the saved output appears in `verification_output.txt`.

The finite checker reports 102 complete parameter cases involving 865,158 states and 600 further sampled vectors. It is deliberately separate from the infinite proof and does not establish general correctness on its own. No independent audit has been performed.
