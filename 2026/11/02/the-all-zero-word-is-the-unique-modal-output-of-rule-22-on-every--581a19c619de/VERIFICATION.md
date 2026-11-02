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

Use `python3 verify.py` in the package directory. It checks the matrix-count identity, recurrence and envelope, plus every input-output fiber for ring lengths 3–16, and prints `VERIFY_OK`. To reproduce via independent direct bit operations, compile and run `crosscheck.cpp` with a C++17 compiler (`c++ -O2 -std=c++17 crosscheck.cpp -o crosscheck && ./crosscheck`); it exhaustively enumerates inputs through ring length 22 and prints `CROSSCHECK_OK`.

These finite checks corroborate the formulas and implementation. All-order correctness rests on the elementary nonnegative-matrix envelope and exact recurrence proof given in `RESULT.md`. The complete multivariate fiber distribution, multiple updates, and independent historical-priority verification are outside scope.
