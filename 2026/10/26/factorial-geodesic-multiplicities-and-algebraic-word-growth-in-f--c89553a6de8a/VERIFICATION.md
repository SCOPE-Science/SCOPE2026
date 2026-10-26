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

Run `python3 verify.py` using Python 3 and its standard library. The program exhaustively enumerates all words of length zero to eight on four letters (total 87,381) and independently constructs each Munn tree, endpoint, R-root tree, inverse L-root tree and D-translation class. It checks the observed shortest length and total number of shortest word representatives for each observed element or class against the explicitly stated formulas.

A separate truncated formal-power-series implementation expands the recursive rooted-excursion equation and compares the resulting length counts against those obtained by direct word enumeration, degree by degree. Additionally, independent enumeration for rank one through length twelve and rank three through length six verifies the algebraic-series predictions outside rank two. The observed rank-two count is `1, 4, 16, 60, 228, 840, 3132, 11496, 42528`. Expected terminal lines:

```
VERIFY_OK enumerated_words=87381 H=54590 R=35558 L=35558 D=12176 rank=2 max_length=8
RANK2_GEODESIC_SERIES [1, 4, 16, 60, 228, 840, 3132, 11496, 42528]
AUXILIARY_VERIFY_OK 1 12 [1, 2, 4, 6, 10, 12, 18, 20, 28, 30, 40, 42, 54]
AUXILIARY_VERIFY_OK 3 6 [1, 6, 36, 210, 1230, 7140, 41550]
```

This is bounded validation, not a proof for higher rank or greater length. The complete proof is in RESULT.md. No independent audit has been performed.
