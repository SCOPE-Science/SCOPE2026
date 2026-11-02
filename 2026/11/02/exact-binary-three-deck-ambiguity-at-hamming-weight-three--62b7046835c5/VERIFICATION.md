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

The complete theorem is proved in `RESULT.md` by gap-count formulas, an exact factorization and a generating-function bijection. To reproduce the finite consistency check, run `python3 verify_deck3.py` with standard Python 3. The script independently enumerates all binary length-\(n\) words of Hamming weight three for \(3\le n\le16\) and calculates all eight three-subsequence counts by position triples, without using the gap-count formula for constructing the decks. It checks fiber sizes, both directions of the proposed involution, and the unrestricted-in-\(n\) coefficient expression at each tested length. The actual recorded output appears in `verify_deck3_output.txt`.

These finite tests do not establish the infinite theorem; the proof's symbolic identities and counting bijection do. Independent mathematical audit status remains not performed.
