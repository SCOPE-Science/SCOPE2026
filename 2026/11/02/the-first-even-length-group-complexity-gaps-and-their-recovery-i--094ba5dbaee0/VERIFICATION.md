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

The exact binary factors at lengths four, six and eight follow from the length-\(2^m\) uniform-substitution block argument and all four occurring binary bigrams. The standalone Python code enumerates all 24 and 720 permutations to exclude cyclic generators with a single identification, verifies explicit subgroup witnesses for all remaining listed values and checks the length-eight involution. An independently organized exhaustive C++ enumeration covers all 1,455 subgroups of \(S_6\) and agrees on its attainable spectrum.

Reproduce with `python3 verify_tm_even_group_spectra.py` and `g++ -O3 -std=c++17 verify_tm_six_subgroups.cpp -o verify_tm_six_subgroups && ./verify_tm_six_subgroups`.

Only finite lengths four, six and the specific length-eight witness are asserted. A general formula for all even lengths is not established. Independent mathematical audit has not been performed.
