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

# Reproducibility and finite scope

From the package root run with Python 3.10 or later:

```sh
python3 scripts/check_mask.py
python3 scripts/check_sets.py
```

Both scripts are self-contained Python standard-library computations. The first enumerates the entire Boolean lattice of \(16\) vertex positions, tests nonempty distinct closed-ball intersections, enumerates legal one-codeword swaps, checks natural cube isometries, and runs BFS for every natural orbit representative. Its complete output must match `outputs/check_mask.json`. The second starts from actual binary quadruples, excludes every 6-element identifying code, enumerates all 7-element codes, derives the exchange graph through common 6-subsets, and runs BFS from every state. Its output must match `outputs/check_sets.json`.

The two methods use distinct state encodings and independent adjacency construction. Each also obtains exactly 192 six-code configurations if only pairwise distinctness is required and the condition that every intersection be nonempty is deleted; these are **not** identifying codes under the stated definition. All \(65536\) subsets are covered by the first program, so its minimum proof is exhaustive. By monotonicity, the second program's negative test at size \(6\) also excludes all smaller subsets. Neither run is an infinite-family proof nor verifies potential external priority. The calculated graph and orbit representatives are labeled explicitly in `RESULT.md`.
