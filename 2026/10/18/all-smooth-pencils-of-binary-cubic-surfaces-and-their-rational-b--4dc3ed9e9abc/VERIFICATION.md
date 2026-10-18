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

The exact smoothness test is the surjectivity of the gradient multiplication map from four copies of homogeneous cubics to homogeneous quintics. This was executed orbitwise, covering all nonzero ternary-degree-three forms in four variables (20 binary coefficients). The 36 geometrically smooth projective representatives were independently checked by 144 Gröbner unit-ideal tests on all four projective affine charts.

The primary C++ pencil census enumerated 30,017,433,600 ordered bases by weighting each of 36 orbit-representative sums over the 322,560 smooth forms; dividing by six yields 5,002,905,600 pencils. A separate Walsh-transform implementation checked the total from additive convolution; a separately coded coefficient evaluator checked all 16 rational-base-point bins. All values agreed.

For the fifteen-point base stratum, a separate calculation enumerated the 28 smooth filling cubic forms and 56 compatible pencils, verified transitivity of their projective orbit under explicit generators, and checked that the five common rational lines on every such pencil are pairwise skew. The executable programs and expected outputs are bundled as ordinary files. These computations do not prove statements about smoothness of the scheme-theoretic base curve, and no independent external review has been performed.
