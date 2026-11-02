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

The standalone Python file `verify_heawood.py` has no third-party dependencies and produces `VERIFY_OK` when run with Python 3.8 or later. The generated execution text is in `verify_output.txt`. It verifies the 21 point–line incidences of the Fano plane, the 14-vertex graph and its genus-eight cycle lattice, all 168 linear automorphisms and their six conjugacy classes, vertex and edge Frobenius orbits, and exact order-two, order-three, order-four and order-seven integral lattice normal forms. The basis certificates have determinants \(1,-1,-1,1\), respectively, and the matrix identities are checked over integers. Algebraic descent, the normalization sequence and classification of finite-field tori are proved in `RESULT.md`, not certified by finite enumeration. No independent human or external audit has been conducted.
