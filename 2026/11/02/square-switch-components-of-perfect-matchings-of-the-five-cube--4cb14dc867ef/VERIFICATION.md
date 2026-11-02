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

# Reproducible verification of square-flip components in the five-cube

Two complete standalone source files are supplied and require no external datasets or mathematical packages. The C++ program requires a compiler supporting C++17; the Python implementation uses only the Python 3 standard library.

Run:

```sh
g++ -O3 -std=c++17 q5_verify_cpp.cpp -o q5_verify_cpp
./q5_verify_cpp
python3 q5_verify_python.py
```

Expected C++ success markers:

```text
Q5_BIPARTITE_PARTNER_EXHAUSTIVE_PASS
Q5_202_COMPONENTS_AND_EXACT_EDGES_PASS
matchings=589185 flip_edges=3219360 components=1x120 4x80 99280x1 489465x1
```

Expected Python success markers:

```text
Q5_INDEPENDENT_80_EDGE_BITSET_EXHAUSTIVE_PASS
Q5_SYMMETRY_ORBITS_FROZEN_AND_FOUR_CYCLE_COMPONENTS_PASS
states 589185 edges 3219360 components [(1, 120), (4, 80), (99280, 1), (489465, 1)]
```

The full Python output additionally contains the exact degree histogram. The C++ verifier uses a bijection from even vertices to odd vertices to encode each perfect matching, tests all partner swaps and applies exact disjoint-set connectivity. The Python verifier instead enumerates undirected edge subsets, constructs all \(80\) coordinate squares, toggles every applicable square, computes component sizes, and checks the \(5!\cdot 2^5\) cube-symmetry group actions on exceptional components. The implementations verify the claimed finite structures, not a theorem about general cube dimension. Exhaustive code is accompanied by arguments proving that each enumeration and flip test is complete; experimental sampling alone is not used as proof. These are mathematical self-checks, not independent scholarly auditing.
