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

# Reproducibility checks and limits

Run `python3 verify.py` in the directory containing the standalone code. It requires Python 3 and no third-party packages.

The verifier independently enumerates all set partitions on finite quotients of the arithmetic overflow semiring, checks the definition of a semiring congruence against addition and multiplication tables, and compares the complete accepted sets to two independently generated normal-form families. Twelve absorbed-quotient instances and nine periodic-quotient instances were checked. Additional exact index formula checks cover overflow-chain lengths \(1\) through \(6\) and quotient sizes \(1\) through \(15\).

The observed terminal markers were `VERIFY_OK`, `QUOTIENT_VERIFY_OK`, and `INDEX_VERIFY_OK`. Finite quotient enumeration is exhaustive for each tested finite carrier but is not exhaustive over all finite quotient sizes or the infinite semiring. The proof of all-parameter classification is the symbolic argument in RESULT.md. The indexed-literature comparison does not rule out unindexed precedents.
