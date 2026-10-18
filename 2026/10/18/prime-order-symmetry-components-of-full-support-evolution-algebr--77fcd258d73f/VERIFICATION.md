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

The reproducible independent finite-test program is `artifacts/check_symmetry_locus.py`. It requires only Python 3 standard libraries and can be run using `python3 artifacts/check_symmetry_locus.py` from this directory. It independently enumerates prime-order permutations of degrees 4, 5, 6; verifies each off-diagonal orbital dimension and prime-cyclic orbital closure; enumerates normalized full-support invertible matrices over the fields of orders 2 and 3 in degree 4 and tests their ordinary permutation stabilizers; and independently enumerates several prime-order fixed strata in degrees 4 and 5 over prime fields.

Observed output:

```
ORBIT_CLOSURE 4 17
ORBIT_CLOSURE 5 69
ORBIT_CLOSURE 6 299
WHOLE_OPEN_LOCUS 4 2 0 0
WHOLE_OPEN_LOCUS 4 3 1392 240
FIXED_LOCI 4 3 2 1 7 40
FIXED_LOCI 4 5 2 1 7 9216
FIXED_LOCI 4 3 2 2 6 8
FIXED_LOCI 4 3 3 1 4 12
FIXED_LOCI 5 3 2 1 13 2016
FIXED_LOCI 5 3 2 2 10 352
FIXED_LOCI 5 3 3 1 8 96
ALL_PRIME_ORDER_SYMMETRY_CHECKS_PASSED
```

The geometric component classification is proved for arbitrary dimension and characteristic; the finite enumerations are not offered as a substitute for that proof. The finite-field asymptotic is for fixed dimension as the prime-power field size increases. The calculation concerns ordinary automorphisms, not infinitesimal group-scheme directions. No independent audit has been performed.
