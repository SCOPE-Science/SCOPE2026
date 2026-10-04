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
The universal proof is independent of finite enumeration.

Direct multiplication gives
\[
[(x,y,z),(x',y',z')]=(0,0,x\cdot y'-x'\cdot y).
\]
For every nonzero symplectic vector \(v\), the map
\[
u\longmapsto B(u,v)
\]
is a surjective linear functional. Therefore noncentral conjugacy classes are exactly the \(q\)-element fibers indexed by nonzero vectors, and adjacency is exactly orthogonality.

The packaged checker `artifacts/verify.py` constructs the groups for
\[
(n,q)=(1,4),(2,2),(2,3),(2,4),(3,2).
\]
It verifies the center, all predicted conjugacy orbits, all commuting-class adjacencies, the projective clique blocks, degrees, diameter, a Lagrangian clique witness, common-neighbor counts, spectral multiplicities, and the first two spectral moments. The \(\mathbf F_4\) arithmetic is implemented directly as
\[
\mathbf F_2[t]/(t^2+t+1).
\]

The checker returns `VERIFY_OK`.

Finite computation is not used to prove the theorem.
