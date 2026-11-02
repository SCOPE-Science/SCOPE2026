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

# Reproducibility and proof boundaries

Run `python3 checker.py` from this package directory. It uses no external packages and regenerates the complete Cantor words, enumerating distinct palindromes by direct center expansion rather than by the saturation proof. It then builds the predicted canonical representative sets and compares exact sets at every positive length for all levels from 1 through 8; it also verifies the total \(3^k\) distinct nonempty palindromes. The recorded run passed at lengths 3, 9, 27, 81, 243, 729, 2187, and 6561.

Finite enumerations do not certify an unrestricted theorem. The all-depth proof is in `RESULT.md`; its critical steps are explicit occurrence of the auxiliary centered palindrome, difference of zero-gap centers, parity obstruction for even palindromes, and exact saturation of the universal distinct-palindrome bound. The exact cutoff is asserted only for the specified \(C_k\), \(k\ge1\). The ordinary rich-word total is already known. Independent scientific audit has not been performed.
