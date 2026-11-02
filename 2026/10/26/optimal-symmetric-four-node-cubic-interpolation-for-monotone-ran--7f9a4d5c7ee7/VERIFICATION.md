---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-31.md",
      "INDEPENDENT_AUDIT_2026-10-31.json"
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

PASS: Every monotone sample vector is a convex combination of the two constant and three increasing-step vectors; linearity reduces all coefficient and x quantifiers to those five. Terminal-step L3=(x+1)(x²-a²)/[2(1-a²)] has sole negative critical value E(a) at (sqrt(1+3a²)-1)/3; middle-step sum L2+L3=1/2+x(1+a+a²-x²)/[2a(1+a)] has extrema ±H(a), while first step reflects L3. Exact derivative signs show E increases 0→∞ and H decreases ∞→0, giving one global minimax intersection. Independently reconstructed Lagrange basis and step critical values at a=1/3,2/5,0.4458209225,1/2,7/10. Original verify.py provides rational interval signs enclosing a* in (0.4458209224,0.4458209226). The proof covers endpoints x=±1 and all admissible samples, including ties; does not imply interpolant monotonicity.

## originality

PASS

PASS, best knowledge: full symmetric variable-node and entire-interval minimax statement differs both in interval and parameter quantifiers from the published uniform four-node central-cell finding (its √3/27 bound). Berrut–Trefethen barycentric formula and unrestricted Lebesgue constants do not optimize the order-constrained cone. The shape-preserving Fritsch–Carlson Hermite procedure changes the interpolant and is not stronger coverage. Source comparison is substantive, but unindexed small-degree interpolation formulae may already contain the same optimizer.

## value

PASS

PASS: choosing inner interpolation nodes to minimize worst overflow for bounded ordered measurements is a natural numerical safety/design problem, distinct from best Lebesgue stability. The exact minimax optimum balances terminal versus central step defects, and is strictly better than the uniform a=1/3 and Chebyshev–Lobatto a=1/2 grids for this objective. It is a nontrivial exact small-degree extremal result, not a renamed fixed-grid constant.

The dated certificate retains the supplied scientific assessment, sources and limitations.
