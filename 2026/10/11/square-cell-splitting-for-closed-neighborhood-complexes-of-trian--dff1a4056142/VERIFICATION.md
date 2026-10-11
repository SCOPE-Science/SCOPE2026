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

# Reproducibility and limits

Run `python3 VERIFIER.py` using the Python standard library. The program enumerates complete simplicial complexes and verifies elementary free-face collapses and the exact residual face set on 118 finite graph instances; 90 instances are reproducibly seeded random admissible connected graphs. The mod-two homology checks compare the original complexes and a square-filled model with the predicted extra four-cycle sphere count. The direct universal proof is in `RESULT.md`, not in the finite enumeration. No integral Smith normal form or independent human validation is claimed.
