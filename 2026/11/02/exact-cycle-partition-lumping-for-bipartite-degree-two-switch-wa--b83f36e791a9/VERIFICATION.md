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

# Verification

Run the complete state enumerator `python3 verify_switch_cycletypes.py` (Python 3 standard library), and independently run `g++ -std=c++17 -O2 -Wall -Wextra verify_switch_cycletypes.cpp -o verify_switch_cycletypes && ./verify_switch_cycletypes` (C++17). Both are standalone and need no downloaded data.

The Python algorithm enumerates every labelled binary matrix with two ones in every row/column for \(n=2,3,4,5\), computes connected components, and uses edge-pair swaps to calculate observed type transitions. The C++ algorithm uses row bitmasks, explicitly visits each of the \(\binom n2^2\) rectangles for each matrix, and searches the bipartite components independently for \(n=2,3,4,5,6\). Exhaustive state totals are respectively \(1,6,90,2040,67950\); at \(n=6\), cycle strata have \(43{,}200\), \(16{,}200\), \(7{,}200\), \(1{,}350\) matrices of types \((6)\), \((2,4)\), \((3,3)\), \((2,2,2)\).

Both programs independently assert every observed transition-type count equals the analytic formula for every tested state, and every type's matrix count equals its closed multiplicity formula. The C++ execution completed successfully with `CPP_RECTANGLE_CYCLE_LUMPING_PASS` and Python with `PYTHON_EXHAUSTIVE_SWITCH_LUMPING_PASS`. Outputs are diagnostic, not substitutes for the all-parameter cyclic-edge proof. Full historical-literature exhaustiveness and independent scholarly validation are not claimed.
