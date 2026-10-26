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

## Reproducible checks

Run `python verify.py` using Python 3. Only standard-library modules are needed. The verifier constructs exact quotient fields \(\mathbb F_{3^6}\), \(\mathbb F_{3^8}\), and \(\mathbb F_{3^{10}}\); computes the rank of the Frobenius-linear polar map for specified nonzero coefficients; and counts Artin–Schreier points by exhaustive trace tests in the first two fields.

The verified cases are \((p,h,n,a,b)=(3,2,3,1,1)\), \((3,3,4,1,1)\), \((3,3,4,1,2)\), \((3,4,5,1,1)\), and \((3,4,5,2,1)\). They obey \(r\le2\gcd(h,2n)\), and the three actual counts obey the announced bound.

The universal statements are proved by the abstract fixed-vector lemma, trace pairing, Gauss sums, and elementary treatment of \(n\le h\); no finite experiment has been extrapolated into an infinite claim. Field-polynomial irreducibility should be checked independently if altering the hard-coded modulus table.
