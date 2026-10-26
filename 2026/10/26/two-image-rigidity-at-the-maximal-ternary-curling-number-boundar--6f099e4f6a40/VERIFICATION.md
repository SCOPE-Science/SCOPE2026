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

# Reproducibility and limits

From this directory run `python3 verify.py`, then compile `check_fast.cpp` as a C++17 program and run the executable. The Python program regenerates each admissible normalized prefix from length \(1\) through \(85\), compares the count table and every listed terminal word, and checks the exact transform-image fibers. It verifies the complete branching classification of length-\(83\) prefixes and the final source-letter condition.

On each listed terminal source the Python implementation also evaluates the *definition* of the curling number on all \(84\) prefixes, rather than trusting the square-suffix shortcut used to construct the search. It tests overlap-freeness of all source and transform factors from scratch. The C++17 implementation performs a separately written exhaustive search using byte-block comparisons.

The certificates use exact comparisons of finite strings, not estimates, sampling, or non-exhaustive time-limited searches. The global labeled count follows by the three initial-symbol choices, and every terminal source is confirmed to use all three letters. No assertion beyond the stated finite lengths is checked or claimed; independent scientific validation has not been performed.
