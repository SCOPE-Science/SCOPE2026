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
# Reproducing the finite integral homotopy calculation

The file `verify.py` is complete and uses Python 3 standard-library functions only. From the directory containing `verify.py`, run:

```sh
python3 verify.py
```

The verifier builds the sixteen-vertex Shrikhande graph directly from the six Cayley differences, proves its vertex degrees and pairwise common-neighbor counts by exhaustive loops, and identifies exactly thirty-two triangles. It enumerates all nonempty vertex masks twice (triangle containment and direct triple adjacency), then checks the complete face vector and constructs the specified greedy face matching.

Every one of the 48,272 nonempty-face Hasse incidences is oriented according to the matching. Kahn's topological sort must visit all 8,950 faces. This checks acyclicity of the matching, rather than relying on a heuristic. The five-by-fourteen Morse boundary is rebuilt by signed gradient-path recursion; five columns (zero-based indices 0, 1, 4, 9 and 11) form a determinant-one integer minor. The complete matrix and critical face masks appear in `certificate.json` for straightforward human inspection. The executable independently recalculates the matrix before comparing it with those expected values.

Finally, binary linear algebra is performed on the **original simplicial boundaries**, not on the reduced Morse matrix. The ranks of the eight nonzero boundary maps are checked as 15, 105, 423, 1029, 1467, 1101, 314 and 16, giving reduced mod-two homology only in degree six with rank nine. These ranks are only corroboration; the integral statement depends on the acyclic matching and unit determinant.

The expected terminal marker is `ALL_VERIFY_OK`. The source code and finite tables are supplied in the same package, without network fetches or unstated dependencies. The proof establishes this one finite graph only; there is no infinitely quantified enumeration claim. Independent external mathematical validation has not been performed.
