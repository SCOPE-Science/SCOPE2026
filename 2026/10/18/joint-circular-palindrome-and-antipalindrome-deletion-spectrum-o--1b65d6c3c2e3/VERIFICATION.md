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

Build the source checker with `g++ -O2 -std=c++17 verify.cpp -o verify` and run `./verify cycles.csv` from the same directory. The executable reconstructs all \(65536\) local pairings and an independent depth-first Eulerian list, verifies the equality of their \(2048\) canonical cycles, tests the complete set of length-five circular windows, and performs two independent score calculations for both palindrome types for all \(65536\) cuts. It compares each calculated score to `cycles.csv`, verifies the joint and marginal table and orbit decomposition, and reports `VERIFY_OK` on success. In the reviewed run, `VERIFY_OK pairings=65536 generator_pairings=2048 independent_Eulerian_DFS=2048 cyclic_cuts=65536 LPS_methods=2 anti_LPS_methods=2 joint_cells=19 symmetry_orbits=528 anti_marginal=26:388,28:1308,30:288,32:64 pal_marginal=25:76,26:114,27:1380,28:286,29:192 csv_rows=2048` was observed.

The proof is an exact finite exhaustion at order five. Cross-checks with longest-common-subsequence values are corroborative and are not substituted for the rigorous interval-recurrence proof. No externally independent scientific audit is claimed.
