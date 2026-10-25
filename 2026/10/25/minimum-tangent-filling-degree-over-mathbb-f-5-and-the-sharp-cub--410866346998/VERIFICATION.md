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

Compile `verify.cpp` with `g++ -O2 -std=c++17 verify.cpp -o verify && ./verify`, and run `python3 check_witnesses.py`. Both programs use exact arithmetic in the five-element field and no network calls. The exhaustive certificate normalizes a nonzero coefficient vector by its first nonzero coordinate; thus all scalar classes, not merely a sample, are tested. It enumerates the complete rational projective plane, gradients at smooth zeros, and their tangent-line incidence masks.

Verified console output:

```text
DEGREE=1 SCALAR_CLASSES=31 FILLING=0 MAX_COVERAGE=6/31
DEGREE=2 SCALAR_CLASSES=3906 FILLING=0 MAX_COVERAGE=21/31
DEGREE=3 SCALAR_CLASSES=2441406 FILLING=0 MAX_COVERAGE=29/31
QUARTIC_POINTS=11 SIX_TANGENTS_PENCIL=YES COVERED=31/31
VERIFY_OK
QUARTIC_TANGENT_PENCIL=6 POINTS=11 COVERAGE=31/31
CUBIC_POINTS=10 COVERAGE=29/31 OMITTED=(1,1,4),(1,4,4)
WITNESS_VERIFY_OK
```

The mathematical argument additionally checks geometric smoothness symbolically; a finite-field smooth-point test alone would not certify geometric smoothness. Results concern only the specified field and degrees, and neither independent scientific validation nor an independent audit has been performed.
