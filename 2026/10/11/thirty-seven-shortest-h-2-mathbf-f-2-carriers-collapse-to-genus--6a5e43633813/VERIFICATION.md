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

`verify.py` embeds the complete \(93\)-tetrahedron presentation and uses only the Python standard library.

It reconstructs
\[
f=(16,109,186,93)
\]
and computes
\[
\operatorname{rank}\partial_2=93,\qquad
\operatorname{rank}\partial_3=92.
\]
Thus
\[
H_2(K;\mathbf F_2)\cong\mathbf F_2.
\]

For every vertex set of size at most nine, the verifier constructs its complete local \(2\)-cycle space and reduces those cycles modulo ambient tetrahedral boundaries. The exact numbers of supporting subsets at sizes \(1,\ldots,9\) are
\[
0,0,0,0,0,0,0,0,37.
\]

For each of the \(37\) minimizers, an elementary-collapse search preserving all nine vertices reaches a complex with \(9\) vertices, \(30\) edges, \(20\) triangles, no tetrahedra, connected one-skeleton, edge degree two, and cyclic vertex links. The Euler characteristic is \(-1\), so each terminal surface is \(N_3\). The verifier then checks that its mod-two fundamental cycle is nonzero in ambient \(H_2\).

Exactly four minimizing induced subcomplexes already have this surface form before any collapse.

Exact successful output:

`VERIFY_OK f=16,109,186,93 H2_F2_dim=1 min_vertex_support=9 carriers9=37 already_induced_N3=4 collapse_to_9vertex_N3=37 ambient_fundamental_class_nonzero=37 support_counts_le9=0,0,0,0,0,0,0,0,37`
