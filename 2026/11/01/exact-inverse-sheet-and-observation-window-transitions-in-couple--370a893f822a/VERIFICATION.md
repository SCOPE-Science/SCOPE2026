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

# Verification of the coupled-map inverse-fiber result

The proof of all-real-target multiplicities is the explicit target diffeomorphism in `RESULT.md` followed by one-variable cubic monotonicity. The \(1,2^N,3^N\) window theorem requires the outer-root enclosure argument, also given there; no finite experiment is used to extrapolate either assertion.

Run `python3 verify.py` from a directory containing this file and `verify.py`. The script uses only Python's standard library, evaluates the full Jacobian with exact fractions, and prints on successful execution:

```
Exact forward/inverse and full Jacobian identity cases: 90
Exact zero-target preimage count: N= 2 count= 9
Exact zero-target preimage count: N= 3 count= 27
Exact zero-target preimage count: N= 5 count= 243
Two-in-box exact witness: L=3/2, h(y)=3/2; roots 1 and (-1+sqrt(13))/2
All checks passed
```

The script was executed in the packaging environment; its tests are reproductions of exact finite identities and examples, not universal proof certificates. The result does not classify multi-step preimages, forward orbit basins, or invariant boxes. Independent audit has not been performed.
