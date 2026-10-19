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
# Verification record

Run `python3 artifacts/verify.py` using Python 3 and the standard library. The checker enumerates all three-by-three linear maps over the two prime fields, filters by *derived coefficient equations* equivalent to the affine weight-minus-one identity, then checks that original identity for every ordered pair of field elements for every accepted operator. It separately enumerates every affine automorphism of the Heisenberg canonical Lie affgebra and computes the images of all six normal forms under conjugation, asserting pairwise disjointness and exhaustion.

Expected replay:

```
q=2 operators=57 ranks={0: 8, 1: 24, 2: 24, 3: 1} 6 affine orbits=[2, 6, 24, 12, 12, 1] automorphisms=48
q=3 operators=244 ranks={0: 27, 1: 108, 2: 108, 3: 1} 6 affine orbits=[3, 24, 108, 36, 72, 1] automorphisms=1296
VERIFY_OK: complete prime-field affine-map scan, direct RB identities and full affine conjugacy orbits
```

No external packages, datasets or services are necessary. These are exhaustive for the two stated fields, not an exhaustive validation over all finite fields or infinite fields. The general proof uses Lie subalgebra classification and affine-automorphism transitivity, independently of these computations.
