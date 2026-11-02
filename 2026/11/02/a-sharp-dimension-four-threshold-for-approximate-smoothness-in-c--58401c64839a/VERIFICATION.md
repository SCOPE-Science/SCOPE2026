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

# Verification record

The claim is proved by an exhaustive analytic classification of vertices, active supporting functionals and their dual distances. The key nonstandard identity is the dual norm \(\|h\|_*=b_1+(s-1)b_2\) for \(1<s<2\), where \(b_1,b_2\) are the two largest coefficient magnitudes; its proof is a fractional-knapsack argument over the full cube–crosspolytope intersection.

Execute `python3 artifacts/verify.py` from the extracted finding directory. Actual output:

```
VERIFY_OK 20 full-polytope exact-rational cases
```

The program enumerates all signed two-support vertices and all displayed facet normals and compares the largest active dual distance with the claimed coefficient at five rational parameters in dimensions two through five. It uses only the Python standard library. Finite checks do not establish the infinitely quantified statement; the proof independently handles arbitrary dimension, every real parameter and both endpoint ranges.

The novelty comparison examines the original mathematical works on approximate smoothness and this norm-ball family, plus published different-invariant results on the same body. Its unavoidable limitation is incomplete historical bibliographic coverage. No independent audit or external certification was performed.
