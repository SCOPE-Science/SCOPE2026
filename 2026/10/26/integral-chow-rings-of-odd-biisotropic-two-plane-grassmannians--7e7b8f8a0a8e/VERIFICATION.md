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

A standalone Python 3 exact-integer checker is included as `verify.py`. Run `python3 verify.py`; it needs no third-party package. It executes the Pieri rule on the integral Schubert basis of \(\operatorname{Gr}(2,2n+1)\) for \(2\le n\le15\), constructs the entire middle intersection matrix and checks its determinant is \(1\), finds a determinant-one minor in every relevant multiplication-by-\(x^2\) map below the middle, and verifies the top Plücker integral equals Catalan \(C_{2n-1}\). Observed output:

```
VERIFY_OK n=2..15 middle_integral_forms_det=1; low_degree_h2_primitive=true; Plucker_Catalan_degrees=true
degree_samples=[(2, 5), (3, 42), (4, 429), (5, 4862), (6, 58786), (7, 742900), (8, 9694845)]
```

The universal argument is the integer Schubert Pieri triangular-minor proof, the recurrence for determinants of the middle matrix, integral Lefschetz/Poincaré duality, and the Gysin projection formula, reproduced in `RESULT.md`. The check is an independent exact-arithmetic consistency test of finitely many instances, *not* a computer proof for arbitrary \(n\). The cycle-class isomorphism depends on the published affine cellular decomposition. The formula is not claimed for \(k\ge3\), nongeneral pencils or equivariant/quantum rings. The \(n=2\) comparison is known prior art; the novelty claim starts at \(n=3\). No independent audit has been performed.
