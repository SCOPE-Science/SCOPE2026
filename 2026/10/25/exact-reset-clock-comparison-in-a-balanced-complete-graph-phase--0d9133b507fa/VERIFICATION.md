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

Run `python verify.py` using Python 3. The program requires only the standard library and solves the complete independent stationary second-moment system with exact rational arithmetic, including off-diagonal terms, without substituting the claimed coarse-moment formulas. It checked 45 parameter sets for each of the two protocols and printed `PASS: 45 exact-rational all-generator scenarios; 2 protocols each`.

The general proof is algebraic, not an extrapolation from the finite tests. The stationary generator equations for \(\mathbb E\|X\|^2\) and \(\mathbb E S^2\), the force-frequency balance and the stationary contraction are reproduced in `RESULT.md`. Tests use \(N\in\{2,3,4,5,6\}\), positive rational rate and coupling values, and nonzero balanced frequency vectors. They cannot establish priority or nonlinear-Kuramoto behavior. Independent review has not been performed.
