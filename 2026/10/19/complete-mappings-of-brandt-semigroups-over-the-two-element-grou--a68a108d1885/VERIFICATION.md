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

# Reproducible finite checks

Run `python3 verify.py`. The script independently (1) enumerates candidate local blocks of size four and counts all valid block pairs, and (2) exhausts every permutation of the eight nonzero elements of \(B_2(C_2)\). Both calculations return exactly 32. The reduced block calculation returns 16 possible first blocks, each with two followers. The construction check verifies the mapping and induced product bijection for indices \(n=2,4,6,8,10\).

These finite computations corroborate, but do not replace, the unrestricted even-index construction proof and parity argument in `RESULT.md`. They do not enumerate the number of complete mappings at higher indices, and no independent external audit has been performed.
