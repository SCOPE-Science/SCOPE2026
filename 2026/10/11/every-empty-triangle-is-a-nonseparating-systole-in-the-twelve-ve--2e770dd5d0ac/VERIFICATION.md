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

`verify.py` embeds the complete 44-facet presentation of the twelve-vertex genus-six surface and uses only the Python standard library.

It verifies that the one-skeleton is the complete graph \(K_{12}\), every edge has degree two, and the Euler characteristic is \(-10\). Exact bit-vector reduction of the 44 facial triangle boundaries has rank \(43\), giving \(\dim H_1(K;\mathbf F_2)=12\).

All \(220\) vertex triples are enumerated. The \(44\) faces are null boundaries; all \(176\) nonfacial triangles reduce to nonzero classes. Equality of reduced vectors gives \(110\) classes with triangular multiplicities \(1^{\times56},2^{\times48},4^{\times6}\).

For symmetry, every automorphism is determined by the image of vertex \(0\) and an isomorphism of its eleven-cycle link with the target link. The verifier exhausts all \(264\) such maps, obtaining exactly \(12\) facet-preserving automorphisms, then computes every support orbit and class orbit.

Exact successful output:

`VERIFY_OK f=12,66,44 chi=-10 genus=6 H1_F2_dim=12 missing3=176 all_missing3_nonzero=yes triangular_classes=110 multiplicities=1:56,2:48,4:6 aut=12 support_orbits=4,4,12,12,12,12,12,12,12,12,12,12,12,12,12,12 class_orbits=(12,1)x4,(4,1)x2,(12,2)x3,(6,2)x2,(6,4)x1 quadruple_classes_one_orbit=yes`

The program proves the finite combinatorial and homological assertions. The final word “nonseparating” additionally uses the standard theorem that a simple closed curve in a closed orientable surface separates exactly when its mod-two homology class is zero.
