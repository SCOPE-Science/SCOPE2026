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
# Reproduction and scope

Run `python3 verify.py` and compile and run `verify_independent.cpp` using a C++17 compiler; both must report their `VERIFY_OK` or `VERIFY_CPP_OK` lines without errors. The Python implementation recomputes the exact perfect matching recurrence and explicit exhaustive matching list; enumerates both complementary two-factor types, the 1440-element automorphism action, one-factorization census, and the all-factorization symmetry orbit. It writes the exact orbit/factorization witnesses in `representatives.csv`. The C++ implementation independently enumerates matchings by bipartite injective assignments and factors by bitwise disjointness, without importing the Python program's data.

The vertex labeling is explicitly defined in `verify.py`. The graph is finite with exactly 30 vertices and 45 edges, so enumeration of every matching and factorization is exhaustive. There are no probabilistic approximations, timeouts interpreted as proofs, or claims about larger families. No independent external audit is asserted.
