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

# Reproducibility and verification

Execute `python3 verify.py` in this package directory using Python 3.10 or newer. The program requires only the standard library. It checks 313 small-tree instances with labelled vertices by direct enumeration of all vertex subsets, compares the **exact family of minimum dominating sets** with the theorem, and separately applies a root-status dynamic program. It then checks all 363 degree sequences with height between one and five and degrees two through four for spherically symmetric trees, and 425 further deterministic irregular trees up to height six with branching two or three. The recorded output was:

```
VERIFIED
brute_full_minimizer_classifications 313
all_spherical_branching_profiles 363
irregular_branching_DP_instances 425
total_instances 1101
```

The mathematical argument in `RESULT.md` is the unrestricted proof: finite instances cannot establish the result for arbitrary height or branching. The DP verifier and small exhaustive checks are corroborative, not independent expert audits. All referenced files are embedded in this package.
