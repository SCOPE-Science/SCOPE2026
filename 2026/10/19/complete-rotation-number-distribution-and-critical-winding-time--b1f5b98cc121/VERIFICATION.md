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

# Reproduction of the numerical checks
Run `python verify.py` with Python 3 and no third-party dependencies. Its actual output was `VERIFY_OK 36`.

The program solves the published resonance relation numerically by bisection for six integer indices, forms each corner trajectory, constructs all four quarter-turn polygon chains, and computes shoelace area independently of the closed area formula at 36 combinations. It also evaluates the exact \(K=3\) special case and finite resonant-parameter asymptotic comparisons. It does not enumerate all levels or prove the asymptotic tail, and its floating-point tolerances do not constitute exact certification.

The universal mathematical checks consist of the geometric shoelace derivation, linear interpolation of rotation number along the original foliation, exact density differentiation, tail integration, and the displayed algebraic Taylor expansions in `RESULT.md`. No independent audit or outside validation has been performed.
