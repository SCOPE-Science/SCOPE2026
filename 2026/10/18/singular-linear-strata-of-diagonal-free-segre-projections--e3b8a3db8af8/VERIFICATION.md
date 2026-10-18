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

# Reproducibility

Use Python 3 with SymPy and run `python3 verification/check_crown.py` from the directory containing `RESULT.md`. The independent enumerator constructs all faces via intersections of the exact \(3n\) facet equations and checks the corresponding primitive-normal Smith forms. Expected output:

```
n=3 faces=49 singular_faces=15 components=9
n=4 faces=349 singular_faces=50 components=14
n=5 faces=1911 singular_faces=140 components=20
n=6 faces=9327 singular_faces=357 components=27
VERIFY_OK
```

All four cases completed successfully in an exact-arithmetic replay. The checker additionally verifies that every singular face lies in one of the predicted maximal strata, and that none of the simplicial normal cones has nontrivial lattice index. No random computation is used. Finite computation cannot certify the infinite-family theorem or novelty; the proof's face and integral-semigroup arguments are essential for both.
