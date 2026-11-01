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

# Reproduction of the finite checks

Run `python3 verify.py` in a directory containing the accompanying standalone script. Python 3.10 or later and the standard library suffice. The script enumerates all nonempty faces of the Boolean simplex up to eight vertices, calculates exact furtherness timestamps, and reduces boundary columns separately over the prime fields of sizes \(2\), \(3\), and \(5\), without employing the theorem's cone-boundary basis. It also enumerates actual chains of the nonempty-subset poset up to five ground vertices and independently calculates the order-complex persistence over \(\mathbb F_2\). The two computations test the natural subdivision identification.

Expected output:

```
ORDER_COMPLEX_OK cases=14 chains=6086
VERIFY_OK n2..8 cases=35 direct_field_reductions=105 simplices_examined=3549 positive_bars=1291 boundary_primes=(2,3,5)
```

All assertions executed successfully in the reported computation. They verify small parameter cases, not the theorem for all \(n\), and field tests alone cannot exclude integral torsion. The explicit unimodular filtered basis and its proved timing inequalities supply the infinite-family and integral argument. The result is not independently audited.
