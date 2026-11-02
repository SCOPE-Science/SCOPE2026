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

The finite certificate is reproduced by running `python3 verify.py` in the directory containing the companion `chords.txt`. Exactly 1017 orders, \(8\le n\le1024\), are tested, and every target in the range \(1\le s\le n(n+1)/2\) is checked by integer-bitset membership. The chord certificate is read from the actual local file path and validated in full. The checker also directly enumerates connected vertex subsets at three small orders as a consistency crosscheck.

The lower bound of one extra edge follows from the published incompleteness theorem in Marotti–Needleman, arXiv:2610.08889v1. The computation proves no assertion beyond the specified finite bound; it is not a symbolic proof of a universal conjecture. Independent external audit has not been performed.
