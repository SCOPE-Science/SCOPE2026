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

`verify.py` embeds the complete \(99\)-tetrahedron presentation and uses only the Python standard library.

The one-skeleton has \(115\) edges. Contracting a spanning tree leaves \(100\) graph-cycle generators. Integral unimodular reduction of the \(198\) facial relations isolates \(98\) unit pivots. The residual block is twice an integral matrix whose Smith form is one unit pivot and one zero column. Thus the full Smith form is
\[
\operatorname{diag}(1^{98},2,0),
\]
so
\[
H_1(K;\mathbb Z)\cong\mathbb Z\oplus\mathbb Z/2.
\]

The explicit integral cocycle in the verifier gives the free coordinate and evaluates to \(1\) on \((1,2,9)\). The explicit mod-two cocycle vanishes on that free generator and evaluates to \(1\) on \((1,2,7)\), so it gives the torsion coordinate.

Exhaustion finds \(494\) graph triangles: \(198\) faces and \(296\) nonfaces. The nonfaces have exact coordinate counts
\[
(0,0):37,\qquad
(0,1):112,\qquad
(\pm1,0):69,\qquad
(\pm1,1):78.
\]

Exact successful output:

`VERIFY_OK f=16,115,198,99 H1_Z=Z+Z/2 graph_triangles=494 facial3=198 empty3=296 null_empty3=37 systoles=259 pure_torsion=112 primitive_free=69 primitive_free_plus_torsion=78 smith=1^98,2,0`
