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

# Reproduction

Run `python verify.py` with standard Python. This checks the mathematical formula independently from its proof using matrix enumeration and finite-field row reduction. All matrices in the minimal nilpotent orbit are enumerated by nonzero vector/functionals with zero pairing, with repeated rank-one operators removed. Every ordered pair of these operators is included in the tally.

Complete target-space checks: \((q,n)=(2,2),(3,2),(4,2),(5,2),(2,3),(3,3),(2,4)\). Complete checks of **attained** targets together with selected unattained targets: \((q,n)=(4,3)\). The latter is not an exhaustive check of the full target space. The implementation uses an explicit quadratic irreducible polynomial for the extension field \(\mathbb F_4\). The expected counts for rank-two targets are recomputed by finding their image and invariant projective lines.

The finite checks produced, respectively, \(3,8,15,24,21,104,105\) distinct nonzero rank-one square-zero summands in the seven complete-target cases and \(315\) in the additional extension-field case; each test reported `VERIFY_OK` and the final status was `VERIFY_OK`.

These tests establish no infinite or all-prime-power statement by themselves. That conclusion follows from the finite-dimensional symbolic argument in `RESULT.md`. No independent audit has been performed.
