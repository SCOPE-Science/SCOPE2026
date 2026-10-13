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

# Verification scope

The proof is algebraic for all \(q=2^m\), \(m\ge2\). The standalone script `artifacts/verify.py` is a finite sanity check and **not** an infinite-parameter certificate.

`python3 artifacts/verify.py` requires only the Python 3 standard library. It implements polynomial-basis field arithmetic for the irreducible moduli `0b111`, `0b1011`, and `0b10011`, constructs the columns directly, and uses Gaussian elimination to search all subsets of sizes two, three, and four. It tests **minimality** of each identified dependency and equality of the complete observed set to the predicted explicit set. It also checks projective-line Steiner incidence, cardinalities of all minimal three-helper sets for every value position, and an explicit family of pairwise disjoint recoveries for each value position.

A completed invocation returned these scientific results:

```
GF(4) VERIFY_OK: rank=4, circuits_3=4, circuits_4=4, derivative_STS_blocks=1, value_disjoint=1
GF(8) VERIFY_OK: rank=4, circuits_3=56, circuits_4=56, derivative_STS_blocks=7, value_disjoint=3
GF(16) VERIFY_OK: rank=4, circuits_3=560, circuits_4=560, derivative_STS_blocks=35, value_disjoint=7
VERIFY_OK
```

The checks enumerate only fields with at most sixteen elements, and the code uses unit column multipliers. The all-field statement and invariance under arbitrary nonzero multipliers are proved symbolically in `RESULT.md`. Independent audit has not been performed.
