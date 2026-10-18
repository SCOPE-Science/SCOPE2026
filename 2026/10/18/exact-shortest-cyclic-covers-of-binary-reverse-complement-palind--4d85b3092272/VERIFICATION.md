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

Compile with `c++ -std=c++17 -O2 -Wall -Wextra verify.cpp -o verify_antipal` and execute `./verify_antipal`. The code implements complete augmented de Bruijn BFS and an independently formulated maximal-overlap Held–Karp subset optimization, with explicit cyclic-window checks.

Expected exact output values: lengths `2,9,26,67`; rooted counts `1,2,14,1232`; number of required words `2,4,8,16`. The terminal output includes `VERIFY_OK antipal_cover_k=2,4,6,8 independent_overlap_TSP_and_rooted_BFS`.

The finite exhaustive algorithms prove only the four stated orders. The state search explores 4,190,096 distinct states before the final eight-bit goal, of 8,388,608 possible augmented states. The tour DP computes only optimum lengths, whereas the BFS also counts rooted optima. No independent audit has been performed.
