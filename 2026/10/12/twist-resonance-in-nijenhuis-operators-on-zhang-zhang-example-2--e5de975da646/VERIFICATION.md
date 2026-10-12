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
The bundled checker reconstructs Example 2.6 and the four source Nijenhuis conditions.

For
\[
\Phi_0(\varepsilon)=\lambda\varepsilon,\qquad \Phi_1=P,
\]
symbolic simplification verifies the complete criterion
\[
P\beta=\beta P,\qquad \det(P-\lambda I)=0.
\]
It also reconstructs the three deformation maps and verifies the formulas in `RESULT.md`.

Over
\[
\mathbf F_3,\quad\mathbf F_5,\quad\mathbf F_7,
\]
the checker exhaustively compares the direct source equations with the structural criterion for every nonzero twist \(\mu\), and verifies both count and rank-profile formulas.

Over \(\mathbf F_3\) and \(\mathbf F_5\), it constructs the full automorphism group and every conjugacy orbit, including the two resonant nilpotent square classes.

The checker returns `VERIFY_OK`.

Finite enumeration is replay evidence. The arbitrary-field theorem is symbolic.
