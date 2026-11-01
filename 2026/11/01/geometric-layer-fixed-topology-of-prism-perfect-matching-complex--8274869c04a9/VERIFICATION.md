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

# Reproducible verification

Run from the directory containing the packaged files:

```sh
python3 verify_fixed_prism.py
```

The checker uses the Python standard library, exact finite enumeration, and binary-matrix reduction. It constructs **all** perfect matchings of each sample prism, forms every candidate orbit-face and compares extendability to an actual perfect matching. It then computes all reduced mod-two Betti numbers of the geometric fixed complex. These are compared with the predicted degree and the exact number of base-graph perfect matchings. For sample graph automorphisms it compares a signed perfect-matching permutation trace with the alternating signed simplex-count Lefschetz trace.

Test families: cycles of lengths 3 through 8, paths of lengths 2 through 6, complete graphs of orders 3 through 5, and the complete bipartite graph with parts of size 3. In particular, the even cycle tests give reduced homology ranks 2 in degrees 1, 2 and 3 for lengths 4, 6 and 8. The four-vertex complete graph gives rank 3 in degree 1; the six-vertex complete bipartite graph gives rank 6 in degree 2. The script terminates with `ALL_CHECKS_PASSED` on success.

The arbitrary-graph conclusion follows from the theoretical proof in `RESULT.md`, not from extrapolation of finite tests. Computations here are mod-two checks, not exhaustive integral-homology certificates; integrality is proved by the explicit relative chain complex. The proof concerns geometric fixed points, not a fixed-vertex subcomplex. No external or independent audit has been performed.
