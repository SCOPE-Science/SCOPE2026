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

# Verification of the mathematical claim

Execute `python3 verify.py` in the same directory. The only dependency is Python 3 standard library. The checker rebuilds the 37-letter sixth substitution iterate, compares all 17 length-eight factors against the displayed list, and verifies closure of the 17 factors under all 119 length-eight windows of their substitution images. It then exhaustively derives the reflected-factor sets for all lengths one through eight, the palindrome counts, and the exact reflection-complexity table.

The induced-factor closure and non-erasing-image argument in RESULT.md proves the length-eight set for the entire infinite word. Reversal exclusion at length eight then holds for all greater lengths. Prefix checks at additional substitution depths are corroboration only, not an infinite proof. The final closed numerical formula for high lengths additionally assumes the established factor-complexity result of arXiv:2206.01776, Theorem 1.

The checker is a finite exact implementation of explicit algebraic word substitutions, not a probabilistic search or numerical approximation. No independent scientific audit is asserted.
