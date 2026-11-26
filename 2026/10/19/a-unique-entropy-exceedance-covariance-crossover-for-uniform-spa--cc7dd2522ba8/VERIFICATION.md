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

For the repaired result and the frozen analytic claims: conditioning on X1=x leaves an independent uniform simplex of mass 1−x. Its entropy expectation and the beta marginal give q_m(x) and μ_m=Harmonic(m)−1 as stated. The centered g_m has both endpoints negative, strictly negative second derivative and zero beta mean. It has exactly two sign transitions; the covariance tail integral has derivative −m times the beta density times g_m, begins and ends at zero, and has exactly one interior root. At m=2 the count at 1/2 is constant. On the scale x=u/m I checked m g_m(u/m)→φ(u)=u(2−γ−log u)−1 and the domination by a polynomial-log factor times exp(−u/2), using −(m−u)log(1−u/m)≤u. The change of variables gives F(c)=integral_c^infinity exp(−u)φ(u)du. Integration by parts yields the E1 expression. Strict concavity, the three signs of φ, zero total mean and the vanishing far tail give a unique interior sign switch of F. Two fixed bracketing points with opposite signs and the finite uniqueness then give mt_m→c_*. An independent computation via conditioning on the event X1>t and translating the entire simplex, not the frozen beta-tail implementation, gave scaled roots 1, 1.16549626046383, 1.45609977024377 and 1.69139877837763 at m=2,3,8,250; quadrature of exp(−u)φ gave c_*=1.70032102613268934 (/tmp/opencode/scope-review-analytic.py 3). At t=1.8/m and large m the concentration form log m−H_m has positive covariance and the quadratic score has negative covariance because its finite threshold is 2/(m+2). I checked the narrowed Finding, lemma, comparisons and slogan in repairs/3; frozen scripts were inspected, not executed.

## originality

PASS

PASS is for the repaired explicit entropy-specific covariance limit and scaling constant, not for the frozen presentation of the finite switch as the distinguishing finding. The distinct universal convex-statistic record has a conditional-simplex identity and a strict-convexity proof that transfer directly to f(x)=x log x, notwithstanding the endpoint C¹ assumption in its theorem statement: near t=0 the transformed coordinates are at least Y_j/2, and |log Y_j| is integrable under the beta marginal, so its derivative proof still works. Negating the statistic gives exactly the finite entropy sign law. The repair credits that coverage and uses the finite law only as a lemma. Neither that record nor the related exact Greenwood law gives the entropy-specific scaled mixed covariance and its zero, the focus of the surviving result. No priority conclusion is drawn from catalogue dates.

## value

PASS

The repaired result measures where two natural spacing diagnostics change their dependence on the mean-gap scale, not merely a specialization of the finite crossover. It gives a full limiting curve and a strict, mathematically interpretable separation from the Greenwood threshold. For instance the two concentration scores give opposite covariance signs with the same exceedance count for limiting thresholds in (c_*,2), so the distinction can matter to the interpretation of diagnostics.

The dated certificate retains the supplied scientific assessment, sources and limitations.
