---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

For an ideal (S,T), the minimal excluded elements are precisely the vertices outside S and the edges of E(S) outside T. Over a triple fixed by rho cubed each vertex is absent at most once. On each edge, t_(i+1)=a_i-t_i, where a_i indicates that both endpoints belong to S_i. Thus 2t_0=a_0+a_2-a_1, excluding odd weight of (a_0,a_1,a_2). This excludes edges within the always-present vertex set X and edges between distinct missing-time classes. For an edge of class j (both endpoints in X union Y_j, not both in X), the unique edge state is at j+2 modulo three. Consequently every always-present vertex must be supplied by newly selected edges from each class in turn, exactly the three-neighbour-colour condition. Conversely S_i=V minus Y_i and T_i=E(G[X union Y_(i+1)]) give E(S_i)=T_i disjoint union T_(i+1); the endpoints of T_(i+1) are exactly X union Y_(i+2), by the neighbour condition and absence of isolated vertices. This recovers both parts of rowmotion. No ideal is fixed (a proper ideal acquires a minimal omitted element, and the full ideal goes to the empty ideal). The cyclic action on colourings is free since V minus X is nonempty. In a biclique a nonempty admissible X must be a whole shore (otherwise G-X is connected), leaving the surjection count 3^t-3*2^t+3 on the other shore; for maximum degree at most two no nonempty X is admissible. A fresh minimal-complement versus component-colouring enumeration compared orbit sets and all three reconstructed transitions on all 43 connected labelled graphs of orders two through four; this is corroboration only. The frozen 771-graph and other reported tests were not replayed.

## originality

PASS

Credit is for the general graph-incidence classification and reduction, not the rowmotion definition or the already covered K_(2,b) and apparently also star specializations. No inspected passage states or yields the graph-wide independent-cut, three-neighbour-colour criterion. This is a best-of-knowledge judgment, not a priority certificate.

## value

PASS

The bijection classifies the actual orbits, replaces iteration over order ideals by a static test on independent cuts and coloured components, and isolates the precise structural obstruction for a non-universal three-cycle. It is useful beyond verifying isolated period counts; no efficiency guarantee for evaluating the sum is assumed.

The dated certificate retains the supplied scientific assessment, sources and limitations.
