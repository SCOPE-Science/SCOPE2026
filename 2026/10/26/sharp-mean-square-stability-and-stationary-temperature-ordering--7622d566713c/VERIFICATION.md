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
Execute `python verify.py` using Python 3 with `sympy` installed. The checker independently enumerates all binary midpoint patterns for batch sizes 2 through 7, computes the random-affine multiplier and independent Gaussian noise coefficients, and compares them to the formulas in RESULT.md using exact rationals. It also checks algebraic factorizations in symbolic \(K\) and the strict negative upper bound on \(Q_j'\).

These checks do **not** replace the argument for arbitrary integer \(K\), the derivative proof of uniqueness, or the random-affine invariant-law theorem. No formal proof assistant or external independent scientific audit was used. The numerical cubic roots quoted in RESULT.md are approximations, not machine certificates.
