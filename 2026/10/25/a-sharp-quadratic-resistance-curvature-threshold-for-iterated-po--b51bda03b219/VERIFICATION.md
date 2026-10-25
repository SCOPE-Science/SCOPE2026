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

# Verification and reproducibility

The theorem is established analytically in `RESULT.md`. Run `python verify.py` with Python 3 and SymPy to reproduce the exact checks.

The checker independently constructs grounded Laplacian inverses with rational arithmetic for 99 distinct iterated-pyramid graphs, calculates all edge effective resistances, and verifies both vertex curvatures. A separate symbolic Chebyshev-polynomial route checks 446 exact settings of the quadratic threshold. The output from the completed run was:

```
EXACT_OK independent_laplacian_cases=99 spectral_threshold_cases=446
```

No numerical tolerances are used. These calculations are not an exhaustive enumeration over arbitrary dimensions; the all-parameter statement rests on the spectral proof, Jensen's inequality, the convex chord bound, and the separate small-polygon cases.

The fixed unit-conductance interpretation must not be changed into a claim about existence of favorable edge weights, which is a different curvature problem.
