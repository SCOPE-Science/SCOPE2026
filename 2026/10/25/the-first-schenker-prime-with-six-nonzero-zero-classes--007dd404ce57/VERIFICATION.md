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

# Reproducibility

Build `verify_minimum.cpp` with any conforming C++17 compiler; no external libraries or downloaded datasets are used:

```sh
c++ -std=c++17 -O2 -Wall -Wextra -pedantic verify_minimum.cpp -o verify_minimum
./verify_minimum
python3 verify_roots.py
```

`verify_minimum.cpp` independently sieves all primes up to \(2339\), tests every nonzero residue for each, and asserts the exact six roots, least-prime property, all \(345\) smaller primes, and their multiplicity histogram \((121,140,65,14,4,1)\). The integer recurrence is justified in `RESULT.md`. It prints `VERIFY_OK` only after successful assertions; no external dataset or approximation is used.

`verify_roots.py` verifies the six-root set using a second modular representation with invertible factorials for \(0\le j<2339\). Its loops likewise enumerate every \(1\le r<2339\) and print `VERIFY_OK` after exact comparison. Both source programs were compiled/executed or interpreted from their actual file paths; results agreed.

The conclusion is finite. Neither verification program checks all primes beyond the finite cutoff, settles unboundedness, or certifies independent scholarly novelty. Independent audit status remains not performed.
