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

The self-contained program `verify_cycle_zonotope.py` uses Python's standard library only. Invoke `python verify_cycle_zonotope.py`; the expected final line is `VERIFY_OK`. It verifies every orientation of a cycle of size \(3\) through \(8\), the primitive signed circuit of oriented incidence roots, every maximal incidence minor as a unimodular basis, the orientation counts, and the predicted singular torus-fixed-point multiplicities. The recorded output is in `verification_output.txt`.

The program does **not** prove normality of every semigroup, algebraic equality of all toric ideals in arbitrary size, or global purity by finite enumeration. The mathematical proof relies on the standard total-unimodularity integrality theorem and the Jacobian criterion in the explicit charts. There is no claim of independent audit or of a completed classification of singular-component incidences.
