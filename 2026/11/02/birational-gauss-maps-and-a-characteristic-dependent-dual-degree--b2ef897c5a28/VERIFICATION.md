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

# Reproducibility and proof boundaries

The embedded `check_dual.py` is a standalone Python 3 exact-integer verifier. Execute `python check_dual.py`. A successful run reports `VERIFY_OK`, with a count of admissible parameter pairs.

It checks: (i) the characteristic reduction of the explicit derivative numerator that guarantees a separable intermediate map, (ii) the count of infinity branches \(n\gcd(r,2)\), (iii) the three polar valuations and the \(2n\) exceptional correction, (iv) the total polar degree in both the generic and special regimes, and (v) the explicit first wild examples \((q,n,r)=(9,2,5)\) and \((125,18,7)\). The implementation uses no external libraries.

The program does **not** certify that a finite scan exhausts all finite fields, that a function-field inclusion is birational, or that a published theorem is absent. Those issues are addressed by the mathematical proof, the source comparisons and the explicit residual risks. The wild different-exponent inequality and Riemann--Hurwitz step are proved at the mathematical level rather than by bounded computation. Independent validation has not been performed.
