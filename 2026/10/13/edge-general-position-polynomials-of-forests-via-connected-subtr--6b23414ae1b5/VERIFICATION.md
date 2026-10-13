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

# Reproducibility and verification

Run `python3 verify.py` using Python 3 with its standard library; no third-party package is required. Compare output to the embedded `verification_output.txt`. The implementation independently checks graph geodesics by literal vertex-pair paths and enumerates each edge subset; this is separate from the rooted recurrence computation. It also enumerates connected induced vertex subsets and tests the boundary correction, the leaf-arm maximum count and forest component multiplicativity.

The recorded execution passed 19,254 exhaustively/sampled labeled trees and 1,429,023 candidate edge subsets, with 3,039 direct boundary comparisons and 16,251 leaf-arm tests. All labeled trees through seven vertices were exhaustively generated; larger orders use deterministic samples, not an exhaustive census. The proof in `RESULT.md` establishes the theorem for all finite trees; computational tests are finite checks only. No independent audit or validation has been performed.
