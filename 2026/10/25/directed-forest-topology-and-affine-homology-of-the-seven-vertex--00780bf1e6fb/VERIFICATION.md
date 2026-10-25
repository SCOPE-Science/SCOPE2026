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

# Reproducibility and boundaries
Run `python3 verify.py` in a directory containing the embedded script. It uses only the Python \(3\) standard library and recreates the twenty-one directed arcs. It enumerates every incoming-arc selection, checks all parent cycles, constructs every simplex, executes the deterministic face-matching algorithm, and checks acyclicity by a topological sort of the entire directed nonempty Hasse diagram. A second exact calculation via the directed matrix-tree theorem yields \(392\) rooted spanning trees per vertex. Signed Lefschetz traces are recomputed for all \(21\) affine automorphisms, with a cyclotomic representation dimension-and-character check.

Expected terminal line: `VERIFY_OK`. Expected preceding certificate:

```
f_vector=21,189,931,2646,4116,2744; total_nonempty=10647
matrix_tree_cofactor=392; spanning_out_trees=2744
morse_pairs=5067; critical=one_0_cell,512_5_cells
nonempty_hasse_incidences=50799; topological_sort=10647
affine_group_order=21; character=(512,1,-1); irreps=(24,25,73)
```

The finite topological sort is a complete proof of acyclicity for this enumerated poset, not a probabilistic sample. The homotopy claim follows using discrete Morse theory; the representation follows by signed Lefschetz theory and rational semisimplicity. The program does not prove any assertion about larger tournaments or test originality against literature. Independent audit is not performed.
