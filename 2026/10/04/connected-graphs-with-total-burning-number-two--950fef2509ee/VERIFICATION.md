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

The accepted theorem is verified by a self-contained argument.

1. For every graph \(H\) with at least two vertices, \(b(H)=2\) if and only if some vertex has at most one nonneighbor. This is exactly the two-round covering condition \(V(H)=N_H[x_1]\cup\{x_2\}\).
2. For a vertex-node \(v\) of \(T(G)\), the exact number of nonneighbors is
   \[
   (n-1-d_G(v))+(m-d_G(v)).
   \]
   Requiring this to be at most one, together with connectivity, forces \(v\) to be universal and permits at most one edge not incident with \(v\).
3. Therefore the vertex-source case gives exactly a star or a star plus one edge between leaves.
4. For an edge-node \(uv\) of \(T(G)\), the \(n-2\) vertex-nodes outside \(\{u,v\}\) are nonneighbors, so the two-round criterion forces \(n\le3\). The connected graphs at those orders are already in the two classified families.
5. In each classified family the star center has zero or one nonneighbor in \(T(G)\), proving sufficiency.

An auxiliary finite check enumerated every connected isomorphism type in the standard Graph Atlas through seven vertices, constructed its total graph, and tested the two-round criterion. No counterexample was found. This finite check is not used to establish the infinite theorem.

The literature comparison verified the standard total-burning definition \(b_T(G)=b(T(G))\), the known bound \(b(G)\le b_T(G)\le b(G)+1\), and the published motivation to characterize prescribed total-burning values. Targeted searches did not find an equivalent classification. Search completeness remains the principal originality limitation.
