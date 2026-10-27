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
# Reproduction and limits

Run `python3 verify_q5.py` (Python 3.10+). It uses only the standard library and prints the fixed-edge symmetry reduction, exact branch-search counters, all-color-pair verification, and the resulting value. An independently coded C++17 checker `verify_q5.cpp`, compiled with `g++ -std=c++17 -O3 verify_q5.cpp -o verify_q5` and executed as `./verify_q5`, verifies the same upper obstruction plus a twelve-edge packing.

The Python checker rebuilds the complete conflict graph from cube edges and checks every unordered pair, not merely a list of preselected constraints. The C++ checker has different data and edge-scan loops. Outputs recorded in `checks.txt`. The exhaustive calculation proves only an exact statement for Q5; it is not a formal theorem prover or an independently audited certification. Checking the coloring is direct, whereas the lower bound relies on the stated completeness of the enumerator and the elementary edge-transitivity argument.
