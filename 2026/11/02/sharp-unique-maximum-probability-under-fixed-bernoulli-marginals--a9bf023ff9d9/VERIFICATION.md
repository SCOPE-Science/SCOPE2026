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

For q>0, the conditional inclusion vector p_i/q has coordinates in [0,1] and sum at least one. The box cut by integer sum bounds is precisely the convex hull of the indicated subset vectors: two fractional coordinates permit opposite perturbations, and a single fractional coordinate either permits a perturbation or violates integrality of a tight sum bound. Thus if S≤2q the conditional law can be supported on sizes 1 and 2, attaining 2q−S, and if S≥2q it can be supported on sizes ≥2, attaining zero. For the upper endpoint, fixing mass s on sizes ≥2 leaves required aggregate inclusion mass y+s, with each coordinate capped by min(p_i,s), and it also requires y≥s. Conversely these conditions suffice by the same subset hull, filling capped coordinates to sum y+s and assigning the remainder to singletons. Equivalently the cap inequality is ∑(p_i−s)_+≤q−s, giving s_* as the maximum of zero and (sum of the k largest p_i minus q)/(k−1) over 2≤k≤d. The singleton constraints are exactly p_i≤q, and the empty constraint is s≤q. Every prefix ratio is ≤y and ≤q (use the total S and p_i≤q, respectively), so the minimal s is attainable. This also verifies the stated sorting complexity and the example prefix maxima 17/20 and 19/40, giving U=1/10 and 19/40. When q=0 the law is empty; when y=0 a disjoint singleton law works. Mixing the extremizers covers the interval. The packaged exact-rational LP code was inspected, not executed; CHECK_OUTPUT.txt records 190 feasible grid comparisons and the two examples, finite corroboration only.

## originality

PASS

Credit the classical first-moment lower bound, the general maximum-coupling feasibility theorem and transport duality, and the same-day winner-label theorem for selecting one maximizer under ties. The supported distinct claim is the exact heterogeneity-sensitive upper endpoint for a unique Bernoulli maximum of value one, with attainment for arbitrary labeled input and prescribed union. The same-day winner-label theorem has a different objective and its unique-winner strengthening excludes atomic data. An equivalent explicit formula elsewhere remains possible; sampled search results are not historical priority evidence.

## value

PASS

When the union and event rates are known but dependence is not, the singleton probability measures how often a unique event accounts for a nonempty outcome. An exact interval with a fast arithmetic evaluation replaces an exponential-size joint-law optimization, and the unequal-marginal example shows a substantive tightening that cannot be recovered from the marginal sum alone.

The dated certificate retains the supplied scientific assessment, sources and limitations.
