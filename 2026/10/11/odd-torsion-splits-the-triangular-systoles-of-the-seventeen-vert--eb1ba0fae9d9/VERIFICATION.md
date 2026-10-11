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

`verify.py` embeds the complete \(100\)-tetrahedron presentation and uses only the Python standard library.

Contracting a spanning tree leaves \(101\) graph-cycle generators. Integral unimodular reduction of the \(200\) triangular-face relations isolates \(99\) unit pivots. The residual block is divisible by \(3\); after dividing by \(3\), its Smith reduction is one unit pivot and one zero column. Thus
\[
H_1(K;\mathbb Z)\cong\mathbb Z\oplus\mathbb Z/3.
\]

The explicit integral cocycle gives the free coordinate and evaluates to \(1\) on \((1,5,7)\). The explicit mod-three cocycle vanishes on that free generator and evaluates to \(1\) on \((1,2,9)\), so the two evaluations give exact coordinates.

The verifier enumerates every three-vertex clique. It finds \(439\) graph triangles, \(200\) faces, and \(239\) nonfaces. None has coordinate \((0,0)\). Up to orientation the exact counts are
\[
\{\pm t\}:130,\qquad
\{\pm g\}:41,\qquad
\{\pm(g+t)\}:34,\qquad
\{\pm(g+2t)\}:34.
\]

Exact successful output:

`VERIFY_OK f=17,117,200,100 H1_Z=Z+Z/3 graph_triangles=439 facial3=200 empty3=239 all_empty3_nonzero=yes pure_order3=130 primitive_free_types=41,34,34 unoriented_types=t|g|g+t|g+2t smith=1^99,3,0`
