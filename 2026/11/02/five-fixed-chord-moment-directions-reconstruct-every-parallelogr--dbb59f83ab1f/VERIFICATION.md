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
The mathematical proof uses four independently auditable facts: (1) an affine square yields a uniform-plus-atom chord law under uniform transverse offsets; (2) its first two moments invert the maximal length and atom weight with valid endpoints; (3) any degree-four homogeneous binary polynomial with five distinct projective roots is identically zero; and (4) two explicit rational strip representations are noncongruent but give identical absolute evaluations in four directions. These do not rely on the checker.

Run `python3 check_chords.py` (standard library only). Expected messages:

```text
EXACT_FOUR_VIEW_NONCONGRUENCE_AND_FULL_LAW_AMBIGUITY_PASSED
EXACT_FIVE_VIEW_BINARY_QUADRATIC_RECOVERY_PASSED
INDEPENDENT_OFFSET_LINE_CLIPPING_MOMENTS_PASSED 21
MOMENT_INVERSION_ENDPOINTS_AND_INTERIOR_PASSED
ALL_CHECKS_PASSED
```

The exact checks cover the four-view example and a five-view rational example. The direct numerical line-clipping tests compare 21 independently integrated mean/second moments against the analytic law; this is not an exhaustive proof of universal recovery. No statistical error estimates, computational formal proof, or independent review are asserted.
