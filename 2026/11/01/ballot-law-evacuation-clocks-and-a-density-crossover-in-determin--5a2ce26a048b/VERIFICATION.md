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
# Reproducible checks and boundaries

Run `python3 check_python.py` with Python 3 and run `c++ -O2 -std=c++17 check_cpp.cpp -o check_cpp && ./check_cpp` with a C++17 compiler. Both scripts are standalone and use only standard libraries. Outputs from these runs are included under `check_python.out` and `check_cpp.out`.

The Python implementation advances each particle based on the full old state, checks first-empty times and the height formula for every word through \(n=15\), and cross-checks exact integer-weighted Bernoulli CDFs at three ratios of initial occupancy and vacancy probabilities. The C++ implementation independently represents states as bit fields, computes updates with a different code path, and checks the time law and every integer shell through \(n=20\). Both programs are exhaustive **only for the explicitly enumerated finite sizes**.

The universal identity follows mathematically from height descent on each update, including the right-edge exit. The finite CDF follows from a standard lattice-walk reflection count, and the limit laws from gambler's ruin, the reflection/invariance principle and the classical central limit theorem. Programs do not establish novelty or mathematical priority, and no independent audit has been performed.
