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

The all-alphabet upper bound and code construction are proved in `RESULT.md`; the programs below only check the formulas and distinguishability for sample alphabets. Run from the folder containing the scripts:

```sh
python3 verify_latin_grain.py
c++ -std=c++17 -O2 verify_modular_grain.cpp -o verify_modular_grain
./verify_modular_grain
```

`verify_latin_grain.py` constructs an idempotent Latin square from diagonal constraints and exact row/column uniqueness for \(q=3,4,5,6\). It checks all received words for collisions and returns `VERIFICATION_OK`. Its binary test checks the six displayed words. Its observed size counts for \(q=2,3,4,5,6\) were `6, 21, 52, 105, 186`, with respective total distinct output counts `12, 63, 172, 365, 666`. This is not an enumeration of every optimal code.

`verify_modular_grain.cpp` constructs the modular family for odd \(q=3,5,7,9,11\). Its observed size counts were `21, 105, 301, 657, 1221`, and output counts `63, 365, 1099, 2457, 4631`. It returned `VERIFICATION_OK`. The modulo construction applies to all odd cardinalities, not just the tested ones.

All computations use exact integer arithmetic and direct output-set comparison, without floating-point tolerance. The classical existence theorem for all other \(q\ge3\) is invoked in the mathematical proof, not re-proved by finite checks. Scientific originality is a literature assessment with a residual risk, and no independent audit has been performed.
