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

# Reproduction

Execute `python3 verify.py` using Python 3 and its standard library, from a directory containing the embedded `verify.py` file. The program uses exact integer polynomial products, path-matching dynamic programming, and separate brute-force weakly order-preserving map counts.

Successful output: `EXACT_OK path_cases=1023 independent_counts=381 zero_linear=[(2, 1), (3, 3)]`.

The checks cover every consecutive-edge subset for each size \(1\le n\le10\), and 381 direct small evaluations. The all-dimensional theorem is proved by the matching extension injection and Ferroni–Morales–Panova's published hereditary linear-coefficient criterion; finite checks cannot certify an unbounded quantifier. No independent audit was conducted.
