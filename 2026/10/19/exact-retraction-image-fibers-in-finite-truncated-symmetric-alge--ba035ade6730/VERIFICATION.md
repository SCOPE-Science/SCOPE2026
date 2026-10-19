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

# Mathematical verification
The embedded `check_retractions.py` contains exhaustive substitution enumeration for five prime-field cases and an additional direct matrix enumeration over the extension field \(\mathbb F_4\). It reports the number of idempotent maps, distinct images, and the fiber multiplicity of every image, and asserts equality with the closed formulas. Executing `python3 check_retractions.py` with Python standard library returns `ALL_EXACT_CHECKS_PASSED_WITH_F4` after the six cases succeed.

The proof is independent of the computation: nilpotence permits arbitrary maximal-ideal substitutions, invertible tangent substitutions are automorphisms, and explicit conjugation reduces a retraction to a coordinate projection. The tangent-identity stabilizer gives the image count, and arbitrary assignments of complementary coordinate generators to a specified image's maximal ideal give its fiber. The code exhausts the named finite parameters only and does not certify any untested parameter. No external mathematical audit has occurred.
