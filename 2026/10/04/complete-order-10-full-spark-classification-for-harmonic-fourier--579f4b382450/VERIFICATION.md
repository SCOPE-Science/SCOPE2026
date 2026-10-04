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

The proof and the exact finite certificate were checked against the stated domain of every nonempty proper row subset of the order-10 DFT.

`verify_z10_fullspark.py` uses integer arithmetic in the cyclotomic quotient \(\mathbb Z[z]/(z^4-z^3+z^2-z+1)\). It enumerates every uniformly distributed row set for cardinalities \(1\) through \(5\), every column subset of matching cardinality, all affine orbits under units and translations modulo \(10\), and then uses the published complement invariance for cardinalities \(6\) through \(9\). No floating-point zero test is used.

Replay result:

```
m uniform full nonfull affine_orbits
1 10 10 0 1
2 20 20 0 1
3 60 60 0 2
4 30 20 10 2
5 20 20 0 1
6 30 20 10 2
7 60 60 0 2
8 20 20 0 1
9 10 10 0 1
bad4_orbit_size 10
bad4_rep (0, 1, 3, 4) witness_cols (0, 1, 2, 6) det (0, 0, 0, 0)
VERIFY_OK
```

The finite computation is exhaustive for the claimed order. It is not evidence for a theorem at other composite Fourier orders. The external theorem used to reject nonuniform row sets is the cited general necessity result of Alexeev--Cahill--Mixon; the verifier focuses on the uniformly distributed cases where sufficiency is at issue.
