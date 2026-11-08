---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-04.md",
      "INDEPENDENT_AUDIT_2026-11-04.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

For each integer n>=3 the hat Gram matrix is G=(4I+S+S^{-1})/6. Its inverse row is the periodic sum of b_j=sqrt(3)(-(2-sqrt(3)))^abs(j), solving the tridiagonal Green equation. Each continuous evaluation kernel is affine on cells and a convex combination of knot kernels; integrating its absolute value yields the stated F(a_j,a_{j+1}) and an attaining sign input. The infinite-line kernel has L1 norm exactly 2. Periodization cannot increase that norm, and specified opposite-sign overlapping translates cancel on a positive-measure interval for every finite odd/even n, making L_n<2. The reverse triangle inequality with geometric tails gives 0<2-L_n<=4sqrt(3)r^floor(n/2)/(1-r). Reproduction of constants and nontrivial sign changes yields L_n>1 and negativity defect (L_n-1)/2. An independently written exact rational cyclic-matrix computation recovered the n=3..12 values, including 16/9,17/9,257/132,2923/1485, all strictly below 2. The all-n statements follow from analytic Green-function/periodization proofs, not the finite experiment.

## originality

PASS

Best-of-knowledge PASS for exact finite cyclic uniform spline L_n, finite strict inequality, sharp supremum 2 and quantitative limit. Classical periodic arbitrary-knot bounds, nonperiodic unrestricted-knot extremal constant 3 and generic stable-basis inequalities are credited prior and do not imply this exact finite norm without nonstandard kernel evaluation. Search misses are not novelty proofs; older cardinal B-spline mass-matrix computations are a residual historical risk.

## value

PASS

The sharp operator endpoint norm is the natural stability constant of a fundamental L2 spline orthoprojector. Complete rational norms for every mesh size, the finite strictness and exponential approach to a sharp constant, and exact positivity defect are useful independently of general nonsharp boundedness. This is a meaningful natural all-size classification rather than an arbitrary finite slice.

The dated certificate retains the supplied scientific assessment, sources and limitations.
