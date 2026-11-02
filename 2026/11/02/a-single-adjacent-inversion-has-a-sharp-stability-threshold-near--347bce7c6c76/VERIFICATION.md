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

# Reproduction

Execute `python verify.py` with ordinary standard-library Python. It enumerates each participant, each adjacent swap position and each perfect matching independently, and searches explicitly for blocking pairs. All outputs for sizes four through ten have been reproduced with exact integer comparisons. The exhaustive case counts are \(8,24,48,80\); numbers without any stable matching are \(1,2,3,4\), and changed unique matchings also number \(1,2,3,4\), respectively.

The proof establishes the infinite family. The finite checker cannot certify higher sizes. No external or independent audit is asserted.
