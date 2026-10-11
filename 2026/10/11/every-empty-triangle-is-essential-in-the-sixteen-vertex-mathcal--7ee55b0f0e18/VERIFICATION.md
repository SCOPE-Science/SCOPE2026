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

The complex reconstructs
\[
f=(16,116,200,100).
\]
Contracting a fixed spanning tree gives a rank-\(101\) graph-cycle lattice. The verifier checks an explicit \(100\times100\) facial-relation minor with determinant \(-4\), while a primitive integral cocycle annihilates all \(200\) facial relations. Thus the relation rank is exactly \(100\).

Modulo \(2\), the relation rank is \(98\). Smith determinantal-divisor reasoning therefore gives exactly two nontrivial invariant factors, both \(2\), and one free generator:
\[
H_1\cong\mathbb Z\oplus(\mathbb Z/2)^2.
\]

The same reduction gives exact coordinates \((n,\epsilon_1,\epsilon_2)\), where \(n\in\mathbb Z\) is the primitive free coordinate and \(\epsilon_1,\epsilon_2\in\mathbf F_2\) are torsion coordinates.

Exhaustive enumeration finds \(507\) graph triangles, \(200\) facial triangles, and \(307\) empty triangles. No empty triangle has zero coordinate. The zero-free-coordinate classes have multiplicities
\[
55,\quad53,\quad49,
\]
and the four unoriented free-coordinate-\(1\) classes have multiplicities
\[
38,\quad38,\quad37,\quad37.
\]

Exact successful output:

`VERIFY_OK f=16,116,200,100 H1_Z=Z+Z2+Z2 maximal_minor_det=-4 rank_mod2=98 graph_triangles=507 facial3=200 empty3=307 all_empty3_nonzero=yes torsion_systoles=157 torsion_counts=55,53,49 primitive_infinite_systoles=150 lift_counts=38,38,37,37`
