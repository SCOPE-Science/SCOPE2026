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

The analytic proof reduces the two sides of Liu’s parameterized inequality to exact algebraic defects and then studies one explicit isosceles boundary family. The accompanying `verify.py` performs independent numerical and exact-rational consistency checks of those reductions.

The checker verifies: (1) direct evaluation of the weighted middle term against the reduced formula on randomized nondegenerate triangles and interior points; (2) the two scaled defect identities; (3) nonnegativity of the classical defects on the samples; (4) the boundary-family formulas using exact rational arithmetic for rational half-angle parameters; (5) isolation of the unique root of \(u^4-8u+3\) in \((0,1)\), the numerical endpoint constants, and the quartic relation for \(\alpha_*\); and (6) explicit interior counterexamples for parameters just beyond each endpoint.

Finite computations are not used to infer universal validity, uniqueness, or novelty. The infinite statements rely on the symbolic derivation, the monotonicity of \(u^4-8u+3\) on \((0,1)\), and continuity of Euclidean distances. The literature comparison is a search-based originality assessment, not a proof that no equivalent statement exists.
