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

Compile and run `verify.cpp` with a C++17 compiler, for example `g++ -std=c++17 -O3 verify.cpp -o verify && ./verify`. The program generates all \(42\) graph edges and every valid face directly from the definition. It constructs the prioritized discrete-Morse matching, checks each of the \(61,837,314\) Hasse covers by a complete directed acyclicity topological sort, and computes integer gradient-path incidences. The final ten-by-ten minor uses zero-based columns \((2,53,49,72,20,87,148,166,17,16)\) and has determinant \(-1\). The expected terminal marker is `ALL_VERIFY_OK`.

Actual local execution produced `FACES_OK 7594361`, `MATCHING_OK pairs 3797088 critical (1,173,10)`, `ACYCLIC_OK visited 7594360 directed_covers 61837314`, `UNIT_MINOR_OK ... determinant -1`, `MATRIX_OK rows 10 cols 173`, `EULER 164`, and `ALL_VERIFY_OK`. Calculations use exact integer coefficients. The proof addresses one finite graph only; the checker does not verify any all-width conjecture. Independent audit has not been performed.
