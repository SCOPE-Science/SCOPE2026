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

For a closed equivelar surface with eight \(k\)-gonal faces and vertex degree \(3\), double counting gives
\[
E=4k,\qquad V=\frac{8k}{3}.
\]
Thus \(3\mid k\). Face-neighbourliness requires at least one edge for each of the \(28\) unordered face pairs, so \(4k\ge28\); divisibility then gives \(k\ge9\).

Euler's formula yields
\[
g=\frac{2k}{3}-3.
\]
The repeated-adjacency surplus is exactly
\[
D=E-28=4k-28.
\]
At the minimum \(k=9\), this gives \(E=36\), \(V=24\), \(g=3\), and \(D=8\).

For any fixed face in that minimal case, its nine edges are distributed among the seven other faces, each at least once. The excess sum is therefore \(9-7=2\). If every face pair shares at most two edges, the doubled-pair graph has ordinary degree two at each of its eight vertices. Its connected components are simple cycles, so their lengths are at least three. The unordered integer partitions of eight into parts at least three are precisely \(8\), \(5+3\), and \(4+4\).

The packaged checker reproduces these identities and exhausts that final partition list. The finite check is a replay aid only; it does not establish geometric realizability of any cycle type.

Unproved limits: no existence or nonexistence theorem for the \(5+3\) type, no treatment of pair multiplicity above two in the cycle classification, and no geometric embedding classification.
