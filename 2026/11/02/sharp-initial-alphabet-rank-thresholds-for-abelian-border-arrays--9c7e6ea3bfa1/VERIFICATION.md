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

# Verification record

Two independent complete canonical-partition enumerations and two independently implemented border-array computations were executed on the provided source files. Both enumerators generated the Bell-number partition counts through length eleven and exactly the `CENSUS.csv` table. The C++ program checked the two border routines against one another on every canonical word, and verified each stored witness by recomputation. The Python program independently reproduced all rank counts, including the four rank-five profiles at length eleven.

To reproduce with only standard compilers/interpreters:

```sh
g++ -std=c++17 -O2 -Wall -Wextra -pedantic verify.cpp -o verify
./verify
python3 verify_independent.py
```

The required terminal markers are `VERIFY_OK` and `INDEPENDENT_VERIFY_OK`, respectively. Both were observed on the supplied files. The largest exhaustive input family contains exactly 678,570 canonical partitions, not a sample. The checked domain is complete through length eleven only. The length-greater-than-eleven rank-five existence follows symbolically by prefix persistence; no higher-length maximal rank was computed. Independent audit has not been performed.
