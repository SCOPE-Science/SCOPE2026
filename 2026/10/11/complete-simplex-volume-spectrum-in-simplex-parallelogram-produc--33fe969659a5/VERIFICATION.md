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

Run `python3 verify.py` with an unmodified Python 3 standard-library installation. The checker constructs all product vertices for each \(n=1,2,3,4\), enumerates every \((n+3)\)-vertex subset, evaluates each integer homogeneous determinant using fraction-free Bareiss elimination with exact divisibility assertions, and compares each three-class histogram to the formulas.

Expected output:

```
DIM 3 COUNTS 12,56,2
DIM 4 COUNTS 288,480,24
DIM 5 COUNTS 4488,3328,192
DIM 6 COUNTS 55760,20480,1280
VERIFY_OK n=1..4 integer_determinants_and_spectrum
```

The proof of the infinite family does not rely on running this checker: it follows from the unimodular barycentric reduction, the six segment types of a square, exhaustive symbolic counting, and separate-affinity vertex reduction. The checker supplies independent exact-arithmetic low-dimensional diagnostics, not an independent audit. It does not enumerate the continuum of nonvertex maximizing simplices, nor certify priority against unexamined historical publications.
