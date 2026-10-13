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
The bundled checker `artifacts/verify.py` reconstructs the four-dimensional Lie–Yamaguti products
\[
[e_1,e_2]=2e_4,
\qquad
\llbracket e_1,e_2,e_1\rrbracket=e_4
\]
and the two weight-zero Rota–Baxter identities.

For a symbolic rank-one operator \(R=u\otimes\ell\), it verifies the universal binary defect
\[
-2\ell(e_4)\bigl(\ell(x)h(y)-\ell(y)h(x)\bigr)u,
\qquad
h(x)=u_1x_2-u_2x_1,
\]
and the universal ternary defect
\[
-\ell(e_4)u_1\ell(z)\bigl(\ell(x)h(y)-\ell(y)h(x)\bigr)u.
\]

Over \(\mathbf F_3\), the checker constructs all \(3201\) rank-at-most-one matrices and tests the defining identities directly on every basis pair and triple. The direct solution set is exactly the union described in `RESULT.md`, with \(1257\) points. It also checks \(E_{21}\) directly.

The exact determinantal component counts are replayed over \(\mathbf F_5\), \(\mathbf F_7\), and \(\mathbf F_{11}\), yielding respectively
\[
22345,
\qquad
153265,
\qquad
2106841.
\]

The checker returns `VERIFY_OK`.

Finite enumeration is replay evidence. The arbitrary-field classification is established by the symbolic defect identities and the linear-dependence argument in `RESULT.md`.
