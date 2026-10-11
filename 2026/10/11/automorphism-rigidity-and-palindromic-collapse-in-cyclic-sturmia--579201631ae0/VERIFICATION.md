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

# Reproduction and limits
Run `python3 verify.py` with Python standard library. The checker enumerates exact rational mechanical codings with slopes `89/144` and `71/171`, alphabet sizes 3, 4, 5 and 7, and word lengths 1 through 15. It independently checks counts of distinct words and palindromes, the constant-palindrome cutoff and permitted adjacent increments, with 4,920 checks. Successful output: `FINITE_RATIONAL_CHECKS_PASS 4920`.

The checker is an **exact finite consistency test** for the combinatorial argument. It does not computationally establish strict ergodicity, spectral purity or the complete automorphism group at irrational slopes. Those are established analytically in `RESULT.md` using the factor map and dense irrational rotation. No numerical approximation to an irrational rotation is relied on in the theorem.
