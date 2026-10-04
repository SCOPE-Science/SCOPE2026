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

The symbolic proof in `RESULT.md` establishes the theorem for every admissible number and size of levels.

`artifacts/verify.py` is a standard-library checker. It enumerates every self-function in three small weak orders, filters exactly the order-preserving maps, constructs the induced map on top chains from a tensor basis of augmentation-kernel differences, computes its rank by exact rational row reduction, and compares that rank with the theorem for every map.

Expected replay output is:

```text
levels=(2, 2) monotone=36 nonzero_top=4 rank_hist={0: 32, 1: 4}
levels=(2, 3) monotone=197 nonzero_top=48 rank_hist={0: 149, 1: 36, 2: 12}
levels=(2, 2, 2) monotone=446 nonzero_top=8 rank_hist={0: 438, 1: 8}
VERIFY_OK
```

The finite cases are checks only. They do not certify the infinite theorem by enumeration, and no claim is made about lower homology or full homotopy classes.
