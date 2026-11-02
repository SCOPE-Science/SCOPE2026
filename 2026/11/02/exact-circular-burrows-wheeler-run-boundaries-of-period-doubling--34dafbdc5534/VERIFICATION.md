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

# Reproducible finite verification

Run `python3 checker.py` in a directory containing the standalone file. It requires Python 3 only.

The checker (1) generates substitution iterates and verifies odd counts of ones, (2) builds the circular Burrows–Wheeler transform by cyclic suffix-rank doubling, (3) independently reconstructs rotation sorting by direct string comparison through rank 9, (4) exhaustively enumerates circular bispecial factors through rank 7, and (5) computes exactly the longest common prefixes of each pair straddling a BWT run boundary through rank 14. It compares these with the two recursively specified factor families and checks the run formula at each rank.

Every assertion passed in the executed checks. Exhaustive finite tests do not establish the unrestricted result; the proof in RESULT.md handles arbitrary ranks. No proof assistant or independent mathematical audit was used.
