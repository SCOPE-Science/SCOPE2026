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

# Reproducibility and checks

Two complete enumerators are included as `enumerate_cumulative.cpp` and `independent_check.py`. The C++ program assigns every subset an image by cardinality-increasing backtracking, checking every interval condition imposed by the outcast axiom, then checks all pairs for Or and all 24 permutations for fixed-point counts. The Python program instead propagates each top-down choice simultaneously along its whole Boolean interval, rejecting incompatible assignments, and applies representative permutations for the five conjugacy classes. Both have been run on the complete 16-input choice-function domain.

Expected C and P totals: 336852, 596. Expected per-element fixed-point vectors for the five conjugacy classes: C = [336852, 3312, 484, 141, 20] and P = [596, 56, 16, 8, 2]. Burnside orbit counts: 14976 and 44.

Compile with `g++ -O3 -std=c++17 enumerate_cumulative.cpp -o count` and execute `./count`; separately execute `python3 independent_check.py`. The Python program raises an assertion error if its enumerated counts differ.

The induction on the backtracking state, not timing or partial data, establishes exhaustive coverage. A program failure would void the numerical certificate; neither finite check proves any claim for languages with more than two propositional variables. Publication-priority uncertainty is scientific, not a computational discrepancy.
