---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-29.md",
      "INDEPENDENT_AUDIT_2026-10-29.json"
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

Unique rooted infection paths and conditional common-source Bernoulli trials imply E I_v=q^depth. Condition on non-root edges; convexity of E phi(c+sum_j A_j Bernoulli(p)) follows from nonnegative mixed second differences. For incomparable pair (u,v), their two path edges leaving LCA contribute E P² instead of q²; other sources each contribute q. The resulting exact variance-index identity, q exponent, convex-order dominance and star/path bounds follow. Independently exact checked 3-leaf star P in {1/4,3/4} against q=1/2: variances 9/8 vs 3/4, all discrete stop losses. Analytical argument, not this check, covers arbitrary trees.

## originality

PASS

Qualified best-of-knowledge originality: Previously known infectious-period dependence and marginal infection order do not logically yield total-final-size convex order or topology extremal index without conditioning and joint infection calculus. Still possible older general convex-order theorem could specialize. Prior formulation/implication comparisons are documented; search nonhits are not proof of priority.

## value

PASS

Gives a whole-distribution stochastic order under individual infectiousness heterogeneity plus an exact efficiently computable LCA variance sensitivity index and sharp topology extremizers. It addresses risk independent of mean final size and carefully states supremum not attained by finite periods.

The dated certificate retains the supplied scientific assessment, sources and limitations.
