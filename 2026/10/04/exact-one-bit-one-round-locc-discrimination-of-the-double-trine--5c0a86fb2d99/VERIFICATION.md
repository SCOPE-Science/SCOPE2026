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

The analytic proof reduces the protocol optimization to a one-parameter planar projector problem and then solves the exact Helstrom dual. The bundled script independently performs the following finite checks:

- evaluates the claimed radical to high precision;
- reconstructs all pair-active dual circles for the three weighted trine states;
- reconstructs the all-three-active dual candidate when algebraically admissible;
- verifies feasibility of candidate duals on a dense grid of Alice projector angles;
- checks that the maximum grid value occurs at a symmetry-equivalent \(\sigma_x\) direction and agrees with the radical;
- checks the posterior-prior vector \((1/3,(2+\sqrt3)/6,(2-\sqrt3)/6)\).

The dense grid is not an exhaustive proof over a continuum. The continuum conclusion relies on the convexity and monotonicity arguments in `RESULT.md`. No independent audit has been performed.
