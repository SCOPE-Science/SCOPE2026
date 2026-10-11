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

`verify.py` uses only the Python standard library and reconstructs the complex from the published \(A_4\) generators and the facet-orbit seeds.

It verifies the surface face vector
\[
(12,42,28)
\]
and checks edge incidences and vertex links.

After a spanning-tree contraction, the graph-cycle lattice has rank \(31\). Unimodular integer elimination isolates \(27\) unit relations and leaves a one-row residual relation of gcd \(2\). Thus
\[
H_1(K;\mathbb Z)\cong\mathbb Z^3\oplus\mathbb Z/2.
\]

Three integral cocycles and one mod-two cocycle are checked on all \(28\) facial relations. The cycles
\[
(1,2,12),\quad(1,3,4),\quad(1,4,6)
\]
give the three free basis classes, while
\[
(1,2,5,7,8,11)
\]
is an explicit pure order-two witness.

All \(48\) triangular cliques are exhausted. Exactly \(20\) are nonfaces, and every one is nonzero with primitive free projection. Their free projections have four unoriented directions; both torsion lifts occur in each direction, with counts \(4\) and \(1\). The published \(A_4\)-action has carrier orbits \(4,12,4\) and two four-element orbits on the eight unoriented homology classes.

Exact successful output:

`VERIFY_OK f=12,42,28 surface=N4 H1_Z=Z^3+Z/2 graph_triangles=48 facial3=28 empty3=20 all_empty3_nonzero=yes all_free_projections_primitive=yes simple_integral_1_systole=3 free_directions=4 both_torsion_lifts_each=yes lift_counts_each=4+1 A4_carrier_orbits=4,4,12 A4_class_orbits=4,4 class_orbit_multiplicities=1|4 smith=1^27,2 torsion_witness_len=6`
