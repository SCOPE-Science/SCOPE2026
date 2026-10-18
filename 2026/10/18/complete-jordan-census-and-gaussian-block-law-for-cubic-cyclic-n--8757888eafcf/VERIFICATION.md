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
# Verification notes

The standalone file `nakayama_jordan_check.py` was executed under Python 3 and terminated with `ALL_TRUNCATED_CYCLIC_JORDAN_CHECKS_PASSED`. It independently forms multiplication matrices from path concatenation, calculates finite-field ranks of their first two powers, and compares full type distributions with the claimed transfer-matrix polynomial. The exhaustive configurations are \((q,n)=(2,3),(2,4),(2,5),(2,6),(3,3),(3,4)\), covering \(12{,}730\) elements. An additional \(1{,}024\) pseudorandom examples over prime fields were checked in four configurations.

The mathematical proof verifies the extension-field cases and all positive cycle lengths in scope without relying on the finite checks. The Gaussian limit uses a standard independent-block reduction for bounded, finite-range-dependent summands. No independent mathematical audit has been performed.
