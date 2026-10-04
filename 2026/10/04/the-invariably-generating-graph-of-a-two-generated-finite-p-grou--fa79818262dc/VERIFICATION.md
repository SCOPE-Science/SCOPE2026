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
The universal proof uses two exact standard facts for finite \(p\)-groups:
\[
[G,G]\le\Phi(G)
\]
and Burnside's basis theorem.

The first makes the quotient image of an element invariant under conjugation. The second gives
\[
\langle x,y\rangle=G
\quad\Longleftrightarrow\quad
\{\overline x,\overline y\}
\text{ is a basis of }G/\Phi(G).
\]
For a noncyclic two-generated group,
\[
G/\Phi(G)\cong\mathbf F_p^2.
\]
Therefore two conjugacy classes invariably generate exactly when their nonzero quotient images lie on different projective lines. This proves the entire multipartite description.

The packaged checker `artifacts/verify.py` independently constructs
\[
D_8,\quad C_4\times C_4,\quad C_9\times C_3,\quad H_3,
\]
enumerates subgroup lattices and maximal subgroups, forms their Frattini intersection, enumerates conjugacy classes, and tests invariable generation by all representative pairs. It then verifies the claimed projective-line partition edge-for-edge.

It returns `VERIFY_OK`.

Finite computation is not used as the proof of the universal theorem.
