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

# Finite verification of the Pappus edge-resolving classification

Run `python3 verify.py` (Python \(\ge3.8\), standard library only). In a separate implementation run `g++ -std=c++17 -O2 verify_independent.cpp -o verify_independent && ./verify_independent`.

The Python verifier reconstructs the \(18\)-vertex, \(27\)-edge affine incidence graph, checks graph distances against explicit field formulas, builds all \(351\) edge-pair distinguishing constraints (\(198\) distinct), and compares the geometric minimum-base classification against **every** four-element subset. It checks every smaller subset, all \(262144\) subsets by two equivalent but separately coded predicates, and exact graph automorphism orbits using \(216\) explicitly constructed maps.

Observed output:

```text
VERIFY_OK graph=Pappus(18,27) biaffine_AG(2,3) girth>=6 diam=4 BFS_formula_agree=yes
VERIFY_OK edge_pairs=351 distinct_separation_masks=198 size_le3_success=0 four_bases=540 geometry_agree_on_3060_four_subsets=yes
VERIFY_OK 262144_subsets pair_masks_vs_direct_signatures=exact edge_resolving=254100 nonresolving=8044
VERIFY_OK vertex_resolving_subset_edge_resolving=yes vertex_resolving=243834 edge_only=10266 four_base_overlap=216
VERIFY_OK polynomial=4:540,5:5976,6:17106,7:31392,8:43704,9:48620,10:43758,11:31824,12:18564,13:8568,14:3060,15:816,16:153,17:18,18:1
VERIFY_OK automorphisms=216 five_orbits=54,216,108,108,54 basis_types={(0, 0): 27, (2, 0): 108, (2, 1): 324, (2, 2): 54, (4, 0): 27}
VERIFY_OK representatives=[((0, 1, 3, 4), 54), ((1, 3, 9, 12), 216), ((2, 3, 9, 12), 108), ((1, 5, 9, 12), 108), ((4, 6, 9, 12), 54)]
VERIFY_CPP_OK all_262144_masks edge_bases=540 metric_bases=216 edge_resolving=254100 vertex_resolving=243834
VERIFY_CPP_OK polynomial=4:540,5:5976,6:17106,7:31392,8:43704,9:48620,10:43758,11:31824,12:18564,13:8568,14:3060,15:816,16:153,17:18,18:1
```

These exhaustive calculations concern one finite graph. They do not establish the analogous claims for different orders or settle priority against inaccessible or unindexed literature. The five orbit sizes additionally have a direct group-theoretic justification from the explicit affine collineations and incidence duality in `RESULT.md`.
