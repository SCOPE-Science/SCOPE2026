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
# Reproduction checks

This document records reproducible computations supporting, but not proving, the all-length theorem. The proof's essential steps are in `RESULT.md`: cyclic run compositions, the exact marked-transition double count, two ratio identities, and Stirling's formula.

Run in a working directory containing the supplied files:

```bash
python3 verify.py
c++ -std=c++17 -O2 crosscheck.cpp -o crosscheck
./crosscheck
```

The Python checker uses only the standard library. It evaluates every feasible integer profile and its binomial fiber count for all lengths 1 through 200, checking all maximizing parameters and ties, and independently enumerates all \(2^n\) indexed binary words for lengths 1 through 19. The C++17 checker separately enumerates full four-entry pair matrices for every word at lengths 1 through 20 and matches the maximum values and matrices. It does not reuse the Python binomial-profile enumerator.

Observed verification outputs from the supplied sources: `PARAMETER_OPTIMA_OK`, `DIRECT_WORD_CENSUS_OK`, `VERIFY_OK`, and `CROSSCHECK_OK`. Full-finite search does not imply an infinite statement: the rigorous proof is the symbolic argument in `RESULT.md`. No external independent scientific audit has occurred.
