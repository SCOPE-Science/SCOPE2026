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

`verify.py` embeds all \(107\) tetrahedra and uses only the Python standard library.

Contracting a spanning tree leaves \(108\) graph-cycle generators. Integral unimodular reduction of the \(214\) triangular-face relations isolates \(106\) unit pivots. Every entry in the residual two-column block is divisible by \(4\); after dividing by \(4\), the residual Smith reduction is a rank-two identity. Therefore
\[
H_1(K;\mathbb Z)\cong(\mathbb Z/4)^2.
\]

The tracked column basis change supplies exact mod-\(4\) quotient coordinates. Both coordinate functionals are checked on all \(214\) facial relations. The triangles \(\{2,4,11\}\) and \(\{1,3,9\}\) certify coordinate generators \((1,0)\) and \((0,1)\).

The verifier enumerates every graph triangle. It finds \(519\) three-cliques, of which \(214\) are faces and \(305\) are nonfaces. None of the \(305\) has zero homology coordinate, and all \(15\) nonzero coordinate classes occur.

Up to orientation, the six order-\(4\) inverse-pair classes occur
\[
52,51,51,48,45,38
\]
times, while the three nonzero order-\(2\) classes occur
\[
13,5,2
\]
times.

Exact successful output:

`VERIFY_OK f=17,124,214,107 H1_Z=Z4+Z4 graph_triangles=519 facial3=214 empty3=305 all_empty3_nonzero=yes all_15_nonzero_classes=yes order4_inverse_pair_counts=52,51,51,48,45,38 order2_counts=13,5,2 smith=1^106,4,4`
