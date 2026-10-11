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

Use Python 3 without external packages. Place `verify.py` next to this file, then execute `python3 verify.py`. The script constructs the simplices of the rank-span-two complexes from bitmasks and performs independent exact arithmetic. For each integer \(4\le n\le8\), it calculates the full triangle-boundary rank over \(\mathbb F_2\) using bitset Gaussian elimination. It separately counts face vectors, enumerates fixed simplices for all permutation conjugacy types, and checks the closed cycle-type character formula. Expected output: degree-two ranks \(1,19,91,321,981\), 60 checked cycle types, 10,146 total simplices, and final status `VERIFY_OK`.

The theoretical proof, not this finite enumeration, establishes the infinite-family results. No independent scientific audit or validation is asserted. The rational character does not certify an integral representation decomposition. The available primary literature evidence leaves the originality risk stated in `RESULT.md` and `REVIEW.md`.
