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

# Reproducibility checks

The main evidence is the explicit incidence factorization, the invariant ordinary-coordinate decomposition, and the three displayed core matrices in `RESULT.md`. These give all graph dimensions and all finite fields of characteristic two. The following independently implemented finite checkers corroborate the proof; neither is an independent audit.

Run `python3 check_linear.py`. It constructs the punctured rook graph adjacency matrices as row-bit matrices over the prime field, verifies predicted ranks for powers 0–6 and the relevant universal polynomial identities on 100 dimension pairs from 2 through 11. Its actual output is `linear_output.txt`.

Run `g++ -O2 -std=c++17 check_states.cpp -o check_states && ./check_states`. The program builds the graph directly from rook moves, simulates every binary configuration for 21 graph sizes with at most 17 sites and verifies eventual least period and exact first periodic entry time, totaling 419400 labelled states. Its actual output is `states_output.txt`.

The simulation and size-bounded rank tests are not infinite proofs. The all-parameter theorem uses the dimension-independent invariant decomposition and exact core arithmetic. No claims are made for fields of odd characteristic or deletions of more than one vertex. Independent audit has not been performed.
