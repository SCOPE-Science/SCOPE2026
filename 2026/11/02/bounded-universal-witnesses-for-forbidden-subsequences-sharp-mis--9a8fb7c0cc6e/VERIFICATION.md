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

# Verification

Run `python3 verify.py` using standard-library Python. Observed output:

```
VERIFY_OK principal_instances=407 insertion_spheres=153 unary_exact_optima=9
```

The checker enumerates bounded forbidden-subsequence spectra, explicitly compares insertion sets, and searches all shorter unary hosts in nine small cases. The proof, rather than these finite checks, establishes all unbounded claims. Independent audit has not been performed.
