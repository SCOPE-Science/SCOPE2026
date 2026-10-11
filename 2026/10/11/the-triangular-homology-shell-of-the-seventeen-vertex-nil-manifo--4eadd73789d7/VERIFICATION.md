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

`verify.py` embeds the complete \(103\)-tetrahedron presentation and uses only the Python standard library.

The one-skeleton has \(120\) edges. Contracting a spanning tree leaves \(104\) graph-cycle generators. Integral unimodular reduction of the \(206\) facial triangle relations produces Smith data
\[
1^{101},2,0,0,
\]
so
\[
H_1(K;\mathbb Z)\cong\mathbb Z^2\oplus\mathbb Z/2.
\]

Two integral cocycles and one mod-two cocycle annihilate every facial relation. Explicit triangular cycles evaluate to
\[
(-1,0,0),\qquad(0,-1,0),\qquad(0,0,1),
\]
so these evaluations supply exact coordinates on the proved quotient.

Exhaustion finds \(467\) graph triangles: \(206\) faces and \(261\) nonfaces. No nonface has zero coordinate. Up to orientation the exact counts are
\[
56,\ 35,\ 34,\ 34,\ 34,\ 37,\ 31
\]
for
\[
t,\quad g_1,\quad g_1+t,\quad g_2,\quad g_2+t,\quad g_1-g_2,\quad g_1-g_2+t,
\]
respectively.

Exact successful output:

`VERIFY_OK f=17,120,206,103 H1_Z=Z^2+Z/2 graph_triangles=467 facial3=206 empty3=261 all_empty3_nonzero=yes pure_torsion=56 free_shell=g1:35,34|g2:34,34|g1-g2:37,31 smith=1^101,2,0,0`
