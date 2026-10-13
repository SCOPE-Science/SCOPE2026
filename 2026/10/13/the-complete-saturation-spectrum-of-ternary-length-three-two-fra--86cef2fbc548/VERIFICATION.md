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

# Reproducible finite checks

Execute `python3 verify_python.py` and compile/run `verify_cpp.cpp` as described in `RESULT.md`. Both compute the complete ternary length-three two-frameproof feasible subset family, test every candidate extension for maximality, and reproduce the exact size distribution. Python explicitly generates all 972 forbidden unordered triples; C++ independently uses base-three digit masking. Both emitted catalogues are checked byte-for-byte and contain 1,092 rows. Python also verifies nine full isometry orbits and that all 108 feasible eight-word codes are distinct deletions of the 12 nine-word codes.

Python outputs `VERIFICATION_OK: complete maximality, histogram, 9 isometry orbits, unique eight-word completions`; C++ outputs `VERIFICATION_OK: 14584 feasible codes, 1092 maximal codes`. The complete code catalogue has SHA-256 `e9e663390cc753c2789547540be9174e2075f3b11b9b2b316f35a450610e7728`.

These checks establish the *finite* theorem only; they do not imply results for other alphabets or word lengths, nor constitute an independent external audit. Literature originality remains subject to additional full-text comparisons for inaccessible older sources.
