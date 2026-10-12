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

The standalone `verify.py` artifact was read from its packaged path before replay.

It constructs all proper subspaces of \(\mathbb F_2^3\) in the point/normal model, with the zero subspace included as an isolated vertex. It then exhaustively tests every one of the \(32768\) vertex subsets for standard zero forcing, checks the explicit size-eight forcing trace, constructs the seven-dimensional Gram witness and computes its rank exactly over the rationals.

For the symmetry census, the checker enumerates all \(168\) invertible \(3\)-by-\(3\) matrices over \(\mathbb F_2\), applies the induced point action and inverse-transpose plane action, and partitions all \(1204\) minimum sets into orbits.

Exact replay output:

```text
POLYNOMIAL {8: 1204, 9: 2100, 10: 1792, 11: 980, 12: 364, 13: 91, 14: 14, 15: 1}
MINIMUM_SETS 1204
EXPLICIT_WITNESS (0, 1, 2, 3, 4, 8, 9, 11)
FORCE_TRACE [(1, 13), (2, 12), (4, 10), (3, 14), (8, 6), (9, 5), (10, 7)]
GRAM_RANK 7
GL32_ORDER 168
MINIMUM_SET_ORBIT_SIZES [28, 84, 84, 84, 84, 168, 168, 168, 168, 168]
VERIFY_OK
```

The lower bound and minimum-rank result are established symbolically by the Gram witness and the standard nullity inequality. The exhaustive computation is used only for finite coefficients and the finite orbit census.
