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

# Finite verification and proof coverage

Run `python VERIFY.py` using a standard Python 3 interpreter. The script has no third-party dependencies. It enumerates all binary two-dimensional subspaces in lengths \(4,5,6\), computes each subspace's Euclidean Gram determinant, and constructs graph edges from nonzero intersections. Breadth-first search from every vertex gives all pairwise distances; a separately implemented alternating-pairing predicate tests the proposed three-case distance classification.

Observed output:

```
n=4; planes=20; spheres=(1, 9, 9, 1); check=PASS
n=5; planes=80; spheres=(1, 21, 54, 4); check=PASS
n=6; planes=336; spheres=(1, 45, 270, 20); check=PASS
VERIFY_OK
```

The finite checks include the smallest admissible parameter \(n=4\), both parities of \(n\), every starting vertex, and every possible target vertex for each of these three lengths. They do not certify infinitely many lengths. The infinite proof rests on the exact Gram-to-alternating identity, an explicit intermediate-plane criterion, independence of two pairing functionals, and a count in the alternating orthogonal complement.

These checks do not constitute independent external validation. The literature comparison and its residual risk are documented in `REVIEW.md` and `AUDIT.json`.
