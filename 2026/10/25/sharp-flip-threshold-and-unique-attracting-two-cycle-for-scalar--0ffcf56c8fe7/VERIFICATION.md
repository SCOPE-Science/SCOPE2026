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

# Reproduction and proof boundary

Run `python verify.py` with Python 3.9 or newer. No nonstandard Python packages or downloaded data are required. The direct finite checks cover 63 normalized momentum/step configurations, 3,000 direct finite-difference Jacobian comparisons, seven algebraic critical-center configurations, four 40,000-step critical relaxations, and an illustrative exact algebraic cycle. All checks completed without assertion failure in the actual package source.

The proof in `RESULT.md`, not the finite checks, establishes the quantifiers over every \(0\le\beta<1\), every \(c>0\), and all two-cycle states. In particular, the uniqueness of prime period two follows from the strict monotonicity of the scalar soft-sign, the local cycle stability from the Schur test applied to the exact cycle Jacobian, and critical asymptotics from the discrete center-manifold normal form. The program does not exhaust initial conditions, establish global attraction, exclude higher-period cycles, or certify priority.

The model is an analytically normalized scalar method. Neither practical finite-degree Newton–Schulz dynamics nor independent external validation is checked here.
