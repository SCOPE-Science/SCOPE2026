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

Capping the discrete counts and then ignoring marks for completed players leaves the finishing order unchanged. Poisson thinning and a common rescaling give independent Gamma(i, rate i) times for goals i=1,2,n, with no ties. Independently, for s>0, integrating 4x exp(-sx) above the third completion time and taking expectation gives 4 r_s(1/s^2+n/[s(n+s)]), where r_s=(n/(n+s))^n. Subtract the s=3 integral from s=2 to recover (2); expanding the product of the first two CDFs gives (1). The differences in (3) follow. An independent exact dynamic program in reviews/evidence-4-race.py used only the original discrete race: at residual state d, condition on the next active mark, choosing i with probability goal_i divided by the sum of active goals. It reproduced all three formulas at all 498 integers 2 through 499 and checked both required strict margins and the exact n=2 fractions and tie. For n>=500, the logarithmic inequalities bound r_c between exp(-c) and exp(-c)/(1-c^2/(2n)); both signs and coefficient extrema in (6)-(7) give the stated lower bounds. Independent rational Taylor bounds and fraction comparisons reproduce 20931734927/2484922590000 > 1/200 and 114949/10353000 > 1/100. This analytic tail, not finite extrapolation, completes the quantifier.

## originality

PASS

The new claim is the uniform two-gap theorem for the entire fixed-(1,2,n) integer family, not the Poisson embedding, Gamma representation, or isolated (1,2,3) ordering. Strongest inspected sources do not supply the uniform inequalities or a stronger result implying them.

## value

PASS

The first fixed pair of distinct positive integer goals defines a natural one-parameter test of a proposed rank pattern that fails for general triples. The theorem excludes both rank reversals and collapsing margins across this whole test family. It is an exact quantitative statement rather than an arbitrary finite check.

The dated certificate retains the supplied scientific assessment, sources and limitations.
