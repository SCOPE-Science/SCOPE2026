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

# Reproduction and scope of checking

The reproducible sources `check_gp3.py` (Python 3 standard library) and `check_gp3.cpp` (standard C++17) construct the same labelled graph by independent data structures and confirm the rank formula and fixed-space dimension for every \(7\le n\le120\). The Python implementation uses integer-bit pivot elimination; C++ uses row-bitset elimination and explicit matrix products. The C++ program also enumerates all \(2^{20}\) states of \(GP(10,3)\) and checks one-step image cardinality and fixed states, independently of its rank algorithm. Run `python3 check_gp3.py` and `g++ -std=c++17 -O2 -Wall -Wextra check_gp3.cpp -o check_gp3 && ./check_gp3`. Exact stdout from both runs is provided in `check_gp3_py_output.txt` and `check_gp3_cpp_output.txt`.

The mathematical proof applies to every integer \(n\ge7\) and has no empirical extrapolation: the finite checks are consistency tests. The exact primitive-period spectrum of the reversible component and all individual cycles is not determined. No independent external audit has been conducted.
