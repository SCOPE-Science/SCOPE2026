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

# Mathematical verification

The claimed identity and inequality are established analytically in `RESULT.md`, not by finite computation. Reproduce the supplementary checks by running `python3 verify.py` from a directory containing the embedded files; this uses only the Python standard library.

The checker confirms the three-variable polynomial factorization in exact rational arithmetic; the independent barycentric formula \(\int_T\lVert x\rVert_2^2dx=\operatorname{area}(T)(\sum\lVert v_i\rVert_2^2+\lVert\sum v_i\rVert_2^2)/12\) for inscribed triangles; the limiting isosceles right-triangle moment \(1/3\); and both signs of the first nonzero cubic variation around the equilateral triangle.

The exhaustive domain is not finite. The exact proof covers all admissible triangles by vertex extension, the angular integral, the trigonometric reduction, and the product factorization. The finite numerical tests verify algebraic normalizations and selected instances only. Independent external validation has not been performed.
