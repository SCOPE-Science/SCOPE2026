---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

Minimizing the follower's stage cost gives u=Θx/(2R). Substitution gives the factor 2Rx₀²/B² multiplying the quartic, with the two weights at states x₀ and ax₀. Reflection about zero excludes negative multipliers; the derivative at zero and the strictly positive derivative on [A,∞) give 0<a<A. At η=1 the exact identity G−A²=(a²−Aa+1)² gives the two distinct minima for A>2; the centered quartic y⁴+(2−A²/2)y² plus constant gives the unique minimum for A≤2. For η≠1, the linear term A(η−1)y and reflection about A/2 select one strict half-line. There the derivative in z=|y| starts negative, rises to infinity, and either is increasing throughout or first decreases and then increases. Thus its unique positive root is simple and globally minimizing. Evaluating G′/2 at a=1 for 1<A<2 gives η−(A−1)(3−A); for A>2 evaluation at a± gives (η−1)a± and locates each optimizer beyond the appropriate equal-depth branch. Compactness of the minimizers as η tends to 1 gives the stated one-sided limits. Differentiation along the simple roots yields the envelope gap a₊²−a₋²=A√(A²−4). At A=2 the stationary equation is 2y³+δy+δ=0, with y tending to zero, so y³/δ tends to −1/2. I recomputed the exact leader costs directly from the two stages at Θ=−4, −1 and −5/2, obtaining 25/2, 25/2 and 1681/128.

## originality

PASS

The model, myopic response, and general scalar finite-horizon cost are prior. Specializing Proposition 2 of Matt–Bolognani–Dörfler already gives this quartic, and depressed-quartic algebra is classical. The supported distinct contribution is the complete global selection and closed-loop stability diagram at two periods, with exact jump and critical cusp. The closest inspected source solves high-cost and long-horizon problems and describes stability of a given gain, rather than giving this two-period global phase classification. The indexed quartic and stability comparisons concern different objectives and dynamics.

## value

PASS

Two is the shortest horizon at which the same incentive affects a later state cost. The result distinguishes three meaningful ways the optimal multiplier approaches or crosses the stability boundary: ordinary crossing, cubic-root singular crossing, and a jump with stable and unstable co-optima. It gives exact parameter thresholds and quantifies the jump in both the multiplier and the normalized value derivative, which an observation of nonconvexity or a numerical optimizer would not establish.

The dated certificate retains the supplied scientific assessment, sources and limitations.
