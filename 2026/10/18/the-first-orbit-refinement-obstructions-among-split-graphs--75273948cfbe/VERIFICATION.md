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

# Reproducible finite verification

The finding is a finite classification over split graphs with at most ten vertices. The complete presentations are indexed by clique size \(k\) and a multiset of independent-neighbourhood masks on \(k\) bits, eliminating the need for a large external graph-database dependency. All representations, including duplicate graph-isomorphism types, are tested.

Run from the directory holding these files:

```sh
g++ -std=c++17 -O3 -Wall -Wextra verify_split_cutoff.cpp -o verify_split_cutoff
./verify_split_cutoff > cutoff_census.txt
g++ -std=c++17 -O3 verify_split_small_independent.cpp -o verify_split_small_independent
./verify_split_small_independent > independent_census.txt
python3 verify_split_ten.py cutoff_census.txt > ten_replay.txt
```

The compiled main checker checks all 1,731,702 presentations of split graphs of orders 1–10 (including 1,592,513 at order ten); it reports zero failures through nine and 71 ten-vertex failing presentations. The 71 entries and four complete canonical mask lists appear in `cutoff_census.txt`. Every count is derived from the precise mask-multiset enumeration formula in `RESULT.md`. The independent checker re-enumerates all representations through nine using incidence-matrix row permutations, with a separate explicit cross-part-twin check, and agrees with the main checker. The Python checker reconstructs all 71 exception graphs, checks their degrees and canonical classes, then independently calculates full-graph automorphism orbits of representatives. Its output confirms four graph-isomorphism classes of multiplicities 6, 10, 10, 45 and their stated class profiles.

The code supplies a decidable exhaustive finite certificate, not a theorem about unbounded graph order. All output files are retained for comparison, but the source and the exhaustiveness argument must be inspected as well; output text alone cannot certify a classification. No external independent audit was performed. An undiscovered previously published specialization remains a priority risk.
