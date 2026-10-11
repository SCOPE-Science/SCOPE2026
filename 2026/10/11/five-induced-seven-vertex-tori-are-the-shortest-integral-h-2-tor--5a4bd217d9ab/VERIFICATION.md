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

`verify.py` and `certificate.json` form a standalone exact replay package using only the Python standard library.

The certificate provides an integer \(204\times102\) matrix \(B\) and an integer \(102\times204\) matrix \(L\). Replay verifies
\[
\partial_2B=0,\qquad LB=I,
\]
and rank \(102\) for \(\partial_2\). Therefore the columns of \(B\) are the full integral \(2\)-cycle lattice.

With
\[
H=L\partial_3,
\]
replay verifies \(BH=\partial_3\) and
\[
\lvert\det H\rvert=2.
\]
Thus the integral second homology is exactly \(\mathbb Z/2\).

A mod-two quotient detector is reconstructed from \(H\). Every vertex support of size at most seven is exhausted. Counts of supports admitting a detector-one cycle at sizes \(1\) through \(7\) are
\[
0,0,0,0,0,0,5.
\]
The five size-seven supports are exactly the five listed in the finding.

For each support replay verifies the induced face vector \((7,21,14)\), absence of tetrahedra, degree two at every surface edge, cyclic vertex links, a coherent orientation, and an integral fundamental cycle with nonzero quotient detector. Each is therefore an induced torus representing the unique nonzero integral \(H_2\)-class.

Exact successful output:

`VERIFY_OK f=17,119,204,102 H2_Z=Z/2 min_vertex_support=7 carriers7=5 all_carriers_induced_orientable_tori=yes all_carriers_nonzero_torsion=yes support_counts_le7=0,0,0,0,0,0,5 supports=1-2-4-5-9-11-13;1-2-4-5-9-11-14;1-4-5-6-9-11-13;1-5-6-8-9-11-13;1-6-8-9-10-11-13`
