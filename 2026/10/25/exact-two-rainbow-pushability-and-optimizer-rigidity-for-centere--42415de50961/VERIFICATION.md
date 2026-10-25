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

# Verification and scope
Run `python3 verify_exact.py` using Python 3.10 or later. No third-party packages are required. The script constructs the linear centroid constraints and the pentagon edge-incidence matrix, and iterates over exact dihedral-and-law-swap support orbits. For every mask it solves the affine equations in the quadratic field \(\mathbb Q(\sqrt5)\), checks negative-definiteness of the restricted Hessian via exact leading principal minors, and retains only strictly positive stationary distributions. The program explicitly prints the eleven surviving orbit representatives, asserts that their largest value equals \((73+\sqrt5)/110\), and exactly checks strict complementarity on the four inactive coordinates of the attaining configuration. The proof of why every global optimizer is represented is given in RESULT.md, under the minimal-support quadratic principle.

Checks actually completed: the standalone verifier ran successfully on its source file; the lower-bound distributions were checked for positivity, normalization, collective centering, and exact common-edge probability; a separate floating-point nonlinear optimizer reproduced the optimum numerically. The numerical check is supporting evidence only. The result has not received independent validation or external code review.
