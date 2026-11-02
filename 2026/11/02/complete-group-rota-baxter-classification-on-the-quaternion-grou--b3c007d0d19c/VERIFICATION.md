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

The classification is proved symbolically using the unique involution of the quaternion group and the elementary-abelian quotient by its center. In the first branch the operator descends to a group homomorphism on that quotient; in the second, the map taking an element to its product with its image under the operator descends instead. Both quotient homomorphisms take values in the center.

The C++17 checker independently exhausts all \(2{,}097{,}152\) functions \(B:Q_8\to Q_8\) satisfying the necessary normalization \(B(1)=1\), evaluates all \(64\) ordered pairs for each candidate, and compares the exact solution set with the eight predicted functions. It also enumerates quaternion-group automorphisms, calculates orbit sizes, and evaluates the specified dual map. Its observed result was:

```text
VERIFY_OK candidates=2097152 operators=8 images=1:1,2:3,8:4 aut=24 orbit_sizes=1:2,3:2 dual=checked
```

The Python 3 checker implements signed-quaternion multiplication independently of the C++ table and verifies each predicted function, its cardinality, and its dual:

```text
FORMULA_CHECK_OK operators=8 image_cardinalities=1,2,2,2,8,8,8,8
```

Finite enumeration corroborates the symbolic classification but does not establish historical originality or independently certify the mathematics. The proof concerns the group \(Q_8\), not the quaternion algebra or general extraspecial groups.
