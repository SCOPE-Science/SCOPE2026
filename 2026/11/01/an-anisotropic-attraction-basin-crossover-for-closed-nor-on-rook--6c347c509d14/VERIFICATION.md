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
# Reproducibility and mathematical limits

Run `python3 checks/check_direct.py` from the package root. The output terminates with `DIRECT_OK total_states 169808`. This verifier recomputes each cell's closed-neighborhood NOR directly and checks orbit lengths, counts, basin sizes, recurrent configurations and the strict dominance property across nine boards.

Compile and run the independently structured program using `g++ -std=c++17 -O2 checks/check_projection.cpp -o check_projection && ./check_projection`. Its output terminates with `PROJECTION_OK total_states 1676112`, covering ten boards. It computes row and column masks directly, builds complementary rectangles, and independently checks inclusion–exclusion basin sizes and total conservation. The recorded console outputs are packaged under `checks/`.

Both scripts were executed successfully on the included source versions. The proof in RESULT.md is the only justification for claims over arbitrary dimensions and for the asymptotic regimes. Neither finite program establishes novelty. An earlier 2012 primary article was not accessible in full, so historical overlap cannot be categorically excluded. Independent external review remains unperformed.
