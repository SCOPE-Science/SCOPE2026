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

# Reproduction of the finite nilpotency-index census

Execute `python3 nilindex_six_binary.py` using any Python 3.9+ interpreter (standard library only). The checker enumerates all \(32768\) binary strictly upper triangular six-by-six matrices and computes the first vanishing power twice by separate exact \(\mathbb F_2\) span/product implementations.

Expected exact output:

```
COUNTS [(2, 1), (3, 1329), (4, 574), (5, 9760), (6, 352), (7, 1584), (8, 96), (9, 11648), (10, 64), (11, 192), (13, 512), (17, 5632), (33, 1024)]
FIRST_MASK_WITNESSES [(2, 0), (3, 1), (4, 579), (5, 33), (6, 5217), (7, 4675), (8, 22565), (9, 545), (10, 26145), (11, 21601), (13, 21059), (17, 4641), (33, 21025)]
INDEX_VECTOR_SHA256 31661b0672ffe4caf7417840c56b7d5b9b69a20f91d7b51ff2674843fae737f6
TWO_INDEPENDENT_RECURRENCES_VERIFIED 32768
VERIFY_OK
```

Every index is computed from the defining nonassociative power recurrence, not from matrix powers. The search bound of \(33\) comes from the established maximal nilpotency-index theorem, while the exact histogram is a finite exhaustive calculation. The digest records the ordered one-byte-per-mask index vector, with mask numbers \(0\) through \(32767\). The verifier also checks the known maximal-index row by an independent condition on five immediate superdiagonal entries.

Limitations: exhaustive verification is for binary triangular presentations in dimension six only. It is not a proof for arbitrary infinite fields and does not count isomorphism classes. Literature-priority risks are addressed in the scientific review.
