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

The standalone `verify.py` artifact was read from its packaged path before replay.

For each
\[
3\le r\le10,
\]
the checker builds all nonempty proper subsets of \([r]\), joins two vertices exactly when they intersect, initializes the theorem's \(r\) white vertices, and replays zero forcing until all vertices are blue.

It also constructs the matrix
\[
A_{S,T}=|S\cap T|
\]
and checks that every off-diagonal zero/nonzero entry agrees exactly with graph nonadjacency/adjacency. For
\[
3\le r\le6,
\]
its rank is computed exactly over rational arithmetic and equals \(r\).

For \(r=3\) and \(r=4\), every vertex subset is exhaustively tested, independently confirming
\[
Z(G)=2^r-r-2.
\]

Exact replay output:

```text
r=3: n=6, constructed ZFS size=3, forces=3, Gram pattern OK
r=4: n=14, constructed ZFS size=10, forces=4, Gram pattern OK
r=5: n=30, constructed ZFS size=25, forces=5, Gram pattern OK
r=6: n=62, constructed ZFS size=56, forces=6, Gram pattern OK
r=7: n=126, constructed ZFS size=119, forces=7, Gram pattern OK
r=8: n=254, constructed ZFS size=246, forces=8, Gram pattern OK
r=9: n=510, constructed ZFS size=501, forces=9, Gram pattern OK
r=10: n=1022, constructed ZFS size=1012, forces=10, Gram pattern OK
r=3: exhaustive Z=3, minimum ZFS count=15
r=4: exhaustive Z=10, minimum ZFS count=442
VERIFY_OK
```

The finite checks do not prove the arbitrary-\(r\) lower bound. That bound follows from the exact rank-\(r\) Gram construction together with the general inequality \(M(G)\le Z(G)\).
