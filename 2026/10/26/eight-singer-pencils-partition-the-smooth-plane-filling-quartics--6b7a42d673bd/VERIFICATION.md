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
# Verification guide

Run, in a directory containing the packaged files:

```sh
python3 verify_matrices.py
python3 verify_groebner.py
```

The matrix checker uses only the Python standard library. It enumerates all \(512\) binary \(3\times3\) matrices, all \(168\) invertible matrices, and the \(24\) smooth filling scalar classes. It checks exact determinant conditions, the eight order-seven cyclic Singer groups, the eight sum-closed two-spaces, the disjoint partition, full projective transitivity and stabilizers, and three exhaustive outsider orbits.

The second checker requires SymPy and independently constructs the homogeneous filling-quartic equations from matrix coordinates. It enumerates all \(255\) nonzero forms and computes Gröbner bases for the singularity ideal in each of the three affine charts, over characteristic two. It requires the unit ideal in all charts for geometric smoothness, then enumerates the pencil sums. Its results agree with the first checker. The actual successful reference outputs are included as `matrix_check_output.txt` and `groebner_check_output.txt`. Their lines `PASS` were obtained by executing the packaged scripts.

The theorem is a complete finite-domain classification, with geometric smoothness tested over the algebraic closure. It does not claim a proof of the general Homma--Kim theorem, nor independently audited verification of this result. For the algebraic reduction, see the statement and proof in `RESULT.md`, especially equation (1) and the three determinant-orbit cases.
