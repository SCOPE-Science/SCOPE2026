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

The exact determinant proof, cyclic-module proof, and fixed-point/gcd argument appear in `RESULT.md`. The standalone `verify.py` replays separate binary-matrix and polynomial-determinant calculations: it checks every permutation update order for ring sizes 3–7 and 480 deterministic additional orders at sizes 8–9, compares characteristic polynomials, evaluates ten return times by binary rank, and checks cyclic vectors and selected whole-orbit enumerations. The script prints:

```
VERIFY_OK characteristic_polynomials 6390 fixed_point_checks 59700 cyclic_vectors 5978 orbit_censuses 160
```

Finite enumeration does not establish the unrestricted result or independent verification. The explicit proof establishes the classification for all ring sizes and all return times. The additional historical comparison with Kim (2015) is limited to the available abstract: its full text was not examined.
