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

`verify.py` embeds all \(96\) published four-simplices and uses only the Python standard library.

It reconstructs
\[
f=(15,105,230,240,96).
\]
Contracting a spanning tree of the complete one-skeleton leaves a rank-\(91\) graph-cycle lattice. Integral unimodular reduction of the \(230\) triangular-face relations gives
\[
\operatorname{diag}(1^{88},0,0,0),
\]
so
\[
H_1(K;\mathbb Z)\cong\mathbb Z^3.
\]

All \(455\) vertex triples are classified. Exactly \(230\) are faces and \(225\) are nonfaces. Every nonface has a nonzero primitive exact integral coordinate vector.

In the symmetry-adapted basis, identifying a vector with its negative yields exactly
\[
(1,0,0),(0,1,0),(0,0,1)
\]
with multiplicity \(46\) each,
\[
(1,1,0),(1,0,1),(0,1,1)
\]
with multiplicity \(18\) each, and
\[
(1,1,1)
\]
with multiplicity \(33\).

The published permutation \(a_i\mapsto b_i\mapsto c_i\mapsto a_i\) is checked on the full facet set. It cyclically sends the basis carrier on \((a_1,a_2,b_4)\) to those on \((b_1,b_2,c_4)\) and \((c_1,c_2,a_4)\).

Exact successful output:

`VERIFY_OK f=15,105,230,240,96 H1_Z=Z^3 graph_triangles=455 facial3=230 empty3=225 all_empty3_nonzero_primitive=yes simple_integral_1_systole=3 unoriented_classes=7 binary_subset_shell=yes singleton_counts=46x3 pair_counts=18x3 triple_count=33 order3_basis_cycle=yes smith=1^88,0^3`
