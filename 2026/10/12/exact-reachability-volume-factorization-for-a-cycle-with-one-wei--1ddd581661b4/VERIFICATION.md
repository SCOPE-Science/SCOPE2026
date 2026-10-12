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

# Reproduction checks

The standalone standard-library program `verify.py` constructs the exact scaled integer Laplacian for each rational weight, generates the complete ordered Krylov matrix, and computes its determinant with fraction-free Bareiss elimination. After restoring the rational denominator, it compares this independently evaluated determinant to the closed theorem.

Run `python3 verify.py`. An observed successful execution yielded:

```text
VERIFY_OK: 112 exact rational Kalman determinants; dimensions 3..18
Boundary cases checked: unweighted cycle, open path, and signed-edge resonance
```

The weights checked for each dimension were \(0\), \(1/3\), \(3/5\), \(1\), \(3/2\), \(3\), and \(-1/(n-1)\). This directly tests the path sign, the uniform-cycle rank loss, ordinary nonunit weights, and the signed zero-mode resonance. The checker uses no external library and does not rely on preexisting computed matrices.

These are finite exact-arithmetic tests and do **not** prove the asserted identity for every integer dimension. The universal proof is the reflection-block and resultant argument in `RESULT.md`; its nonstandard step is the reduction of the full Krylov determinant to the product of cross-block characteristic factors, followed by the Fourier multiplicity count. A separate independent audit has not been performed.
