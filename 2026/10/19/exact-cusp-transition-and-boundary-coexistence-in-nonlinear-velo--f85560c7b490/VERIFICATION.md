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

The mathematical proof is in `RESULT.md`. The independent finite-volume consistency program `verify.py` requires Python 3, NumPy and SciPy. Run `python verify.py` from this directory. The program assembles a two-orientation continuous-time Markov generator using upwind transport and instantaneous velocity reset to a central cell. It checks positivity, mass conservation, convergence of three one-sided slopes toward analytical predictions, the positive curvature at the exact local transition, and increasing discretized boundary densities in the predicted divergent regime.

Actual output from the program:

```text
shear-thickening / origin minimum: predicted slope=0.010000000; 2001 cells=0.010048452; 4001 cells=0.010024200
shear-thickening / cusp and edge peaks: predicted slope=-0.008750000; 2001 cells=-0.008716105; 4001 cells=-0.008733102
linear-drag control: predicted slope=-0.008750000; 2001 cells=-0.008690354; 4001 cells=-0.008720140
critical curvature: predicted=0.022307223; discrete=0.022387842
edge lower-bound power=-0.820000000; edge cells=88.453775, 156.070259
PASS: 5 independent discretization/edge checks
```

The full analytical classification follows instead from the forward-generator identities, the reset source strength, and the positive no-tumble subpopulation estimate. The finite grids cannot certify an infinite-density boundary divergence, the uniqueness of any local minimum, or scientific originality. No external independent audit or validation was performed.
