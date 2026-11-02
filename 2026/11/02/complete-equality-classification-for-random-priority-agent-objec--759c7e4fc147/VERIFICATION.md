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

# Reproduction guide

Run both standalone programs beside this document with a C++17 compiler and Python 3:

```sh
g++ -std=c++17 -O2 -Wall -Wextra -pedantic verify_cpp.cpp -o verify_cpp
./verify_cpp
python3 verify_python.py
```

The C++ certificate enumerates exactly \(24^4=331{,}776\) profiles and all 24 priorities for each profile. It checks integer frequencies for numerators 0 through 24, specifically \((317664,1728,5040,6912,432)\) for 0 through 4 and zero beyond, 432 equality profiles, six disjoint relabeling orbits of size 72 each, the exact canonical representatives, and one maximizing acceptable pair per extremizer. The Python implementation independently enumerates 55,296 profiles after a justified sixfold object-label quotient and obtains \((52944,288,840,1152,72)\). It separately verifies the normal forms' unassignment marginals, unique maximizing pair and identical per-priority outcomes.

Both programs completed with `VERIFY_CPP_OK` and `VERIFY_PY_OK`, respectively, from the supplied source files. The proof is a finite complete enumeration for this specified domain, with an independently written cross-check; it is not an asymptotic proof for arbitrary market sizes or an independent external audit.
