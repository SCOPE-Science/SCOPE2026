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

Translate a nonobtuse parallelogram vertex to the origin and let the adjacent side vectors be \(a,b\). Then
\[
a\cdot b\ge0.
\]
The two boundary chains to the opposite vertex are
\[
0\to a\to a+b
\]
and
\[
0\to b\to a+b.
\]

On the second edge of the first chain,
\[
\frac{d}{dt}\lVert a+tb\rVert^2
=
2a\cdot b+2t\lVert b\rVert^2\ge0.
\]
On the second edge of the other chain,
\[
\frac{d}{dt}\lVert b+ta\rVert^2
=
2a\cdot b+2t\lVert a\rVert^2\ge0.
\]
The first edge of each chain has obviously increasing distance. Hence every circle centered at the chosen vertex meets each chain at most once.

The lower bound \(N(Q)\ge2\) is local: at an edge-interior boundary point a sufficiently small centered circle cuts that edge twice, and at a vertex it cuts the two incident edges once each.

`verify.py` symbolically checks the derivative identities and then independently enumerates critical-radius intervals for several deterministic parallelograms. It confirms the at-most-two intersection property at the selected nonobtuse vertex.

The finite sweep is diagnostic only. The proof for every nondegenerate parallelogram is the monotonicity argument above.
