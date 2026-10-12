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
The proof is symbolic and valid over an arbitrary field.

The packaged checker `artifacts/verify.py` independently enumerates the full-support two-dimensional evolution algebras over
\[
\mathbf F_q,\qquad q\in\{2,3,5,7\}.
\]

For each structure matrix it enumerates every one-dimensional subspace, tests which subspaces are ideals, and checks semiprimeness directly from the condition that no nonzero ideal has square zero.

It separately checks primeness by testing products of all pairs of nonzero ideals.

The direct classifications agree exactly with the symbolic defect locus
\[
ad-bc=0,\qquad a^3+b c^2=0.
\]

The checker also verifies the formulas for the numbers of perfect, semiprime-nonperfect, nonsemiprime, and total semiprime matrices.

The checker returns `VERIFY_OK`.

Finite computation is not used to prove the arbitrary-field theorem.
