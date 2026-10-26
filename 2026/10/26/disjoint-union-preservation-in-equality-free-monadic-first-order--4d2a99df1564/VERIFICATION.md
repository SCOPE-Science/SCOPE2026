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

# Verification and reproducibility

Run `python3 monadic_union_check.py` with Python 3. It exhausts all \(2^{2^c-1}\) families of nonempty unary-colour supports for \(c=1,2,3,4\), checks binary union closure, reconstructs join-irreducibles and compares the closed-form predicate against every support. It also checks finite labelled unary structures through four elements when \(c\le2\), and illustrates target-grammar rank sharpness.

Actual output:

```text
UNION_CLOSED_PROFILE_OK 1 2
UNION_CLOSED_PROFILE_OK 2 7
UNION_CLOSED_PROFILE_OK 3 61
UNION_CLOSED_PROFILE_OK 4 2480
RANK_TWO_SHARPNESS_EXAMPLE_OK
```

The finite enumeration checks exactly the claimed finite support instances; it is not a proof for all languages or infinite structures. The proof of the all-domain theorem instead proceeds by equality-free unary support induction, join-irreducible decomposition and a direct semantic equivalence for the constructed rank-two sentence. No machine-checked higher-order proof or independent audit has been performed.
