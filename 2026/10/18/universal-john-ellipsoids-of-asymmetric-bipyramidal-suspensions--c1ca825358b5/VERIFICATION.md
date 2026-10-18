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

# Verification of the asymmetric-suspension theorem

Run `python3 verify.py` from the same folder as `RESULT.md`. The bundled standard-library checker verifies 6,132 combinations of algebraic identities, tight cone-containment constraints, unique stationary aspect ratios, strict sampled height-imbalance comparisons, and symmetric/cone endpoint ratios. The checker did complete successfully when the package was assembled.

Additional unconstrained three-dimensional numerical optimization was performed for rectangular bases at apex heights \((1,2)\), \((0.2,3)\), \((1,1)\), \((0.01,3)\), and \((3.4,0.8)\). The optimizer permitted general ellipsoid orientation and location; its parameter discrepancies from the theorem were below \(2\times10^{-8}\). The accompanying finite checker avoids a mandatory external numerical optimization package.

These checks are not independent certification. The proof in `RESULT.md`, specifically the symmetry and horizontal-shape reduction, sharp square-root containment constraints, global uniqueness of the one-dimensional optimum, and strict convexity in apex-height imbalance, establishes the infinite-dimensional scope over all admissible bases. The tests do not cover arbitrary symbolic convex bodies by enumeration. The result assumes a centrally symmetric full-dimensional base and two positive axial apex heights. Earlier obscure priority sources may exist.
