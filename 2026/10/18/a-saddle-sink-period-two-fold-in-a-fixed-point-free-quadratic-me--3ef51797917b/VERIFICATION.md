---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

For A>0 the second update excludes a fixed point and forces x'=-x for a two-cycle, with x nonzero. Choose x=u>0 and y=z-u/2. Adding and subtracting the first-coordinate closure equations gives z²+u²/4=1-1/B and A cos u=Bu²z. No solution is possible for B<=1; for 1<B<=4/3 the bound 2R<=1 keeps cos positive and z strictly positive, excluding endpoints and giving a bijection. The rescaled logarithmic second derivative is strictly negative by the separate estimates on t²<=1/2 and t²>=1/2; endpoint vanishing gives exactly the two/one/zero census. I reconstructed the Jacobian product: with c=Bu², trace=2-2c-S² and determinant=(1-c)²-H²; P(1) has sign opposite to G'_B. In the stated weak-gain stability range 1<B<=9/8, c<=1/2, H<1/2, and S<1/4. These imply positive determinant below one and P(-1)>0; the rising branch has one root in (0,1) and one above one, and Schur's inequalities give a sink on the falling branch. The bound 0<d<1 at equality is read within the same explicit stability subregion, as in the proof and scope, not throughout the counting region: for B=4/3, the fold relation already gives c>=8/9 and d=trace-1<0. For fold nondegeneracy one can take e=x'+u=y''-y as one residual and subtract a smooth multiple of e from the other to replace x' by -u. Their sum and difference then give the two scalar equations above via invertible row operations. Since z>0 one eliminates z, with the remaining equation having nonzero A derivative and nonzero u second derivative at the maximum; the unit multiplier is simple. Finally the interior maximizer continues by the implicit function theorem from t=√(2/3) and is the unique maximum by strict concavity. Expansion of B R³ and sec(2Rt) gives the relative coefficient 2(2/3)-1/2=5/6. The uploaded script was inspected, not executed; the proof is analytic.

## originality

PASS

The strongest exact census overlap is with a later-path Resultary record covering a wider count regime, not with the paper that introduced the map. The independent distinct content is the all-subcritical-forcing weak-gain saddle/sink classification and the second onset coefficient. The bounds and priority are assessed separately, and no novelty is assigned here to the map or to no fixed points.

## value

PASS

For a specific published fixed-point-free model, the result isolates a complete real primitive two-cycle birth mechanism near the natural gain threshold and answers which branch attracts for all subcritical amplitudes in a proved weak-gain range. This is stronger than visualization, the lack of fixed points, or an isolated small-forcing sink; the second onset coefficient also quantifies the location of the fold beyond its leading singular scaling.

The dated certificate retains the supplied scientific assessment, sources and limitations.
