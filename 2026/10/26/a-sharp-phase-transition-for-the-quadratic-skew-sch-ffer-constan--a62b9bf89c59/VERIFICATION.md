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

The analytical proof checks all edge pairs through the rotation \(R(u,v)=(u-v,u)\), reflection \(Q(u,v)=(u,u-v)\), and symmetry \((x,y)\mapsto(y,-x)\). Both displayed candidate branches have exact zero subgradients in the convex reduced problem. The cubic polynomial is strictly decreasing throughout \([0,1]\), so the transition is unique. The trial-pair factorization controls the other relative-edge orbit.

Run the standard-library Python file `verify.py` using `python verify.py`. It checks seven rational parameter values, all thirty-six ordered edge pairs with an eleven-by-eleven rational sample grid, the proposed candidates, and agreement at the cubic root. Exact finite fractions are used at sample rational points. The computed sample count is 30,492 ordered pair evaluations. The numerical root check is finite precision. Neither the grid nor the decimal checks constitute a proof for all real parameters.

The exact theorem rests on symbolic facet inequalities, two convex subgradient certificates, an algebraic sign condition, and reciprocal symmetry as detailed in `RESULT.md`. The original motivating source is arXiv:2610.03050v1. No independent audit or validation is claimed.
