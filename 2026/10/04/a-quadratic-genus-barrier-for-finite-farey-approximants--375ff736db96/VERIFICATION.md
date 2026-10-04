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

The proof is symbolic.

For every vertex \(v\), the induced subgraph on the closed neighborhood \(N[v]\) has no removable vertex:

- \(v\) has at least three neighbors by \(\varphi_0\);
- for every neighbor \(w\) of \(v\), the edge \(\{v,w\}\) lies in exactly two triangles, providing two distinct common neighbors \(z_1,z_2\in N[v]\);
- therefore \(w\) has at least the three neighbors \(v,z_1,z_2\) inside the induced closed neighborhood.

Thus every vertex of \(G[N[v]]\) has degree at least \(3\). If \(|N[v]|\le n\), this contradicts \(\psi_n\). Hence
\[
\deg(v)+1=|N[v]|\ge n+1,
\]
so
\[
\deg(v)\ge n.
\]

For a connected component \(H\),
\[
|V(H)|\ge n+1
\]
and
\[
2|E(H)|\ge n|V(H)|.
\]

If \(H\) embeds in orientable genus \(g\), then
\[
|E(H)|\le3|V(H)|-6+6g.
\]

Combining the last two inequalities yields
\[
(n-6)|V(H)|\le12(g-1).
\]
Using \(|V(H)|\ge n+1\) gives
\[
g\ge1+\left\lceil\frac{(n-6)(n+1)}{12}\right\rceil.
\]

The bundled checker evaluates this integer expression and verifies the algebraic implication over a finite range.

## Limits

The finite replay checks arithmetic only. The arbitrary-\(n\) theorem is established by the symbolic local-neighborhood and Euler-characteristic argument above.

No optimality or matching upper bound is verified.
