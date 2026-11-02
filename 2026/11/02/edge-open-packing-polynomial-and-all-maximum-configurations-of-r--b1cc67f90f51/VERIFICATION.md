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

# Reproducible checks and proof limits

The included `check_rook.cpp` is a complete standalone C++17 program. It constructs the rook graph directly from row/column adjacency, enumerates edge subsets by size, and tests the original third-edge exclusion between each selected pair. It separately computes the theorem's coefficient formula. Build with `g++ -O3 -std=c++17 -Wall -Wextra -pedantic check_rook.cpp -o check_rook` and run `./check_rook`.

All predicted coefficients for all subset sizes were compared exhaustively for eleven rectangular boards: \((2,2),(2,3),(2,4),(2,5),(3,3),(3,4),(3,5),(3,6),(4,4),(4,5),(5,5)\). Also independently tested zero admissible sets at one edge beyond the proposed maximum. The maximum-count sequence in this order was \(4,12,30,70,45,72,360,1170,288,1440,10800\); the program printed `VERIFY_OK`.

This is finite verification. Mathematical correctness for every \(m,n\ge2\) relies on the row/column-disjoint induced-star decomposition and its counting proof. No independent external audit has been performed.
