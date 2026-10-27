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
# Reproducible verification

Compile `verification/ideal_pairs.cpp` and `verification/direct_ternary.cpp` with a C++17 compiler; run the first without arguments and the second with each integer argument from 1 to 5. Run `verification/verify_ie.py` with Python 3. No input files, third-party libraries, network service, or precomputed look-up tables are required.

The first C++ program generates all Boolean downsets and tests pairs for the maximal-zero immediate-cover property. The second enumerates all monotone maps directly in a linear extension of the inclusion order and independently checks the full back condition against each zero world. Both give 0, 3, 63, 3604, 3242450 in dimensions one through five. The second also counts 0, 5, 111, 7080, 7805614 surjective monotone maps, respectively. The Python program independently verifies the induced-poset downset inclusion–exclusion counts 0, 3, 63 for dimensions one through three.

Finite verification is not evidence for an all-dimensional claim beyond the separately stated mathematical proof. A complete comparison against every prior specialist work has not been performed. Independent mathematical audit has not been performed.
