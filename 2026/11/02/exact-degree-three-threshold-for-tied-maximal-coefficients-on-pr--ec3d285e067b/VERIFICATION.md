---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

By the polydisk maximum principle, torus factorization and surjectivity of z^beta, the norm is the circle norm of a/w+b+cw. Make the endpoints nonnegative by rotating the circle and the output, so their sum follows an ellipse with semiaxes s=|a|+|c| and d=||a|-|c||. To maximize the squared translated norm, complete squares with multiplier lambda>s^2: the upper bound apart from |b|^2 is lambda+s^2 t1^2/(lambda-s^2)+d^2 t2^2/(lambda-d^2). At an interior minimizing lambda the square-completion point is a unit vector. At the lower limit the major-axis linear term must vanish and the minor-axis maximizing coordinate fits in the disk, so the first coordinate can complete the boundary; the circle case is rotationally invariant. Thus the bound after infimizing is exact. At each lambda the major-axis weight is no smaller than the minor-axis weight, so the smallest possible peak places the translation on the minor axis, also covering a flat ellipse or vanishing center coefficient. After normalization the coefficient moduli are (1,1,t) in some order. The squared minimal peak is 4+t^2 for the outer tie. For a mixed tie the maximand is (2+2t+t^2)+2(1-t)x-4tx^2 on [-1,1]; the vertex enters at t=1/5. The resulting pieces give excess over 13/5+t+t^2 of 7/5-5t and (25t^2-22t+5)/(20t), both positive on their ranges. Meanwhile (2+t^(3/2))^(4/3)<13/5+2t^(3/2)<=13/5+t+t^2. This proves strictness at p=3/2 including two-term ties, and increasing p preserves it; a monomial attains equality. For the degree-two witness the circle expression is 1+w-w^(-1), attaining squared norm 5; comparing fourth powers gives 27>25. This verifies failure at the immediately smaller degree.

## originality

PASS

Pass is for the sharp finite degree threshold and strict coefficient inequality on the stated tied class. The phase-minimization conclusion is a special case of Neuwirth's theorem, and the high-degree part overlaps general comparable-coefficient contractivity. Neither alone gives the uniform coefficient comparison at exponent 3/2. The frozen record presents phase analysis as a proof ingredient, not a separate historical novelty claim.

## value

PASS

A three-term progression is the simplest sparse support on which phases can obstruct exact contractivity. Separating phase obstruction from magnitude imbalance by a tied-maxima hypothesis gives a natural, dimension-independent test case. The exact transition between degrees two and three replaces a very large general sufficient degree for this class and identifies when equality can occur.

The dated certificate retains the supplied scientific assessment, sources and limitations.
