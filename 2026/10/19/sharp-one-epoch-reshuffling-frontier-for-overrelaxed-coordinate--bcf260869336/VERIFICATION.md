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

# Verification scope

The standard-library-only `verify.py` computes exact rational quadratic energies for every one of the four possible ordered pairs of coordinate updates and compares their average to the claimed identity. It covers 5,880 exact tests of the formula and diagonal renormalization with multiple rational normalized Hessians, gradient starts and stepsizes; additional tests cover the explicit reversed inequality, the complementary initial gradient, and zero difference at the sharp threshold. Execute `python verify.py` to replay. The code does not search all real parameters, and finite checks do not certify the universal claim; the proof establishes the infinite range.
