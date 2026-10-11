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

`verify.py` reconstructs the eighteen-facet regular nine-vertex torus from the published orbit and group generators and uses only the Python standard library.

A deterministic spanning-tree contraction leaves \(19\) graph-cycle generators. Integral unimodular reduction of the \(18\) facial triangle relations produces
\[
\operatorname{diag}(1^{17},0,0),
\]
so
\[
H_1(K;\mathbb Z)\cong\mathbb Z^2.
\]

Two explicit integral cocycles annihilate every facial relation and evaluate to a basis on two explicit triangular cycles. They therefore give exact integral coordinates on the proved quotient.

The verifier enumerates every three-vertex clique and obtains \(27\) graph triangles, \(18\) faces, and \(9\) nonfaces. The nonfaces have exact oriented coordinate multiplicities
\[
(0,-1):3,\qquad(1,0):3,\qquad(-1,1):3,
\]
so all are nonzero and primitive.

The verifier then tests all \(9!\) vertex permutations and recovers exactly \(108\) simplicial automorphisms. Their induced integral homology matrices form a set of size \(12\), with kernel size \(9\). The full group is transitive on all nine carriers; the kernel has three carrier orbits of size \(3\), exactly matching the three homology directions.

Exact successful output:

`VERIFY_OK f=9,27,18 H1_Z=Z^2 graph_triangles=27 facial3=18 empty3=9 all_empty3_nonzero_primitive=yes simple_integral_1_systole=3 unoriented_directions=3 carrier_counts=3,3,3 aut=108 aut_carrier_orbits=9 H1_action_image=12 H1_action_kernel=9 kernel_carrier_orbits=3,3,3 smith=1^17,0,0`
