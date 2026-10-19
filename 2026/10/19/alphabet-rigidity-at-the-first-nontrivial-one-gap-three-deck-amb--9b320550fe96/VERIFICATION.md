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

The delivered `verify_gapped_qary.cpp` is a standalone standard-library C++17 checker. Compile with `c++ -O2 -std=c++17 verify_gapped_qary.cpp -o verify_gapped_qary` and execute `./verify_gapped_qary`.

It performs two genuinely different exact constructions of every 39-coordinate one-gap three-deck vector for each of the \(3^n\) ternary words, for \(1\le n\le13\). It compares the full sets of nonsingleton pairs and all class statistics, verifies injectivity at lengths three through twelve, and verifies the exact twelve-doubleton classification at length thirteen. The base enumeration has precisely \(1{,}594{,}323\) words and does not sample. All coordinates are within the range of unsigned eight-bit integers at length thirteen. The independent mathematical projection to arbitrary alphabets is proved in `RESULT.md` and cannot be established by finite enumeration alone.

The theorem is computationally assisted, not independently certified. No external audit has been performed. No conclusions are made about length fourteen or longer.
