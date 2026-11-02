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

## Verification record
Run `python3 verify.py` from the extracted package directory. The checker uses only the Python standard library. It independently enumerates all \(\mathbb F_2\)-algebra automorphisms by exhaustive generator-image search, checks the monomial relations, and requires an invertible tangent map. It also verifies the explicit proposed group isomorphism against all ordered pairs of the 32 automorphisms.

Observed output:

```
VERIFY_OK: A,B have 32 automorphisms each; 1,024 isomorphism-law checks; dimension-four comparison 8 versus 24; distinct square-map kernels.
```

This is exhaustive for the fixed finite algebras in the theorem, but does not replace the classification proof or independently establish publication priority. The abstract group isomorphism is not an isomorphism of algebraic group schemes.
