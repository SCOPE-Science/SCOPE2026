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

The proof is analytic. The accompanying `verify.py` provides a deterministic numerical replay of the following checks:

1. random nonsingular affine parallelograms have all four vertices on the constructed circumellipse;
2. direct ellipse and parallelogram areas satisfy \(\operatorname{area}(E)/\operatorname{area}(Q)=\pi/(2\sqrt{1-c^2})\);
3. \(\delta=\operatorname{artanh}|c|\) reproduces the exact \((\pi/2)\cosh\delta\) profile;
4. the defect equals \(\pi\sinh^2(\delta/2)\) and dominates \((\pi/4)\delta^2\);
5. the formulas are unchanged under additional nonsingular affine transformations.

Finite floating-point tests are not a proof and are used only to detect implementation or algebra transcription errors. The rigorous argument is the symbolic matrix calculation in `RESULT.md`. No independent validation has been performed.
