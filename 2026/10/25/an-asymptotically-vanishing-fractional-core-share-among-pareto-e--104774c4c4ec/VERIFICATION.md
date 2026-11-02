---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-27.md",
      "INDEPENDENT_AUDIT_2026-10-27.json"
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

Under Hare quota q=(k+1)/k, a committee containing common candidate c is core stable; private-only committees are stable exactly if they represent at least k-1 distinct ordinary voter groups. A blocking proposal must serve all members of any coalition with quota constraints, and the guardian cases are accounted for. Core+ is not assumed equivalent to integral core: apply Theorem 3.3 of Becker–Greger–Peters, the exact strict payment/reserve characterization. With c in W, construct an explicit payment certificate with strictly sub-quota losing-candidate reserves; without c, each ordinary voter must retain enough reserve to protect common candidate c, and Cauchy–Schwarz yields a lower bound >=k/2>(k+1)/k for k>=3, so no certificate. Combinatorial disjoint types give C(kr,k-1) for c-committees and r^k+k(k-1)C(r,2)r^(k-2) private-only stable committees. A direct utility-sum argument shows no size-k committee is strictly Pareto dominated. For fixed k, private-only count has degree k in r vs core+ count degree k-1. I independently enumerated 170 complete committees across four small profiles, all affordable integral proposals, Pareto comparisons and independent SciPy LP payment feasibility; agreement holds. The polynomial classification is analytic and does not follow from finite LP tolerance.

## originality

PASS

The existence of at least one core+ committee, its Farkas payment certificate, and qualitative separation of core from Lindahl-style priceability are prior (Becker–Greger–Peters 2026; Berker et al. 2025; Gölz–Yaghoubizade 2026). The inspected primary 20-page Becker paper contains a universal existence theorem, not an exact labeled-committee census for a universal/private/guardian approval instance. An older one-private-per-voter example addresses r=1 only, and a degree-capped coincidence result has incompatible supporter-count assumptions. What is assessed is complete fixed-k, growing-r enumeration and the vanishing core+-among-core share, even while every committee is Pareto efficient. This new implication is not entailed by existential core+ or known qualitative gap.

## value

PASS

A natural quantitative question left open by an existence theorem is whether the stronger fractional core criterion is common among ordinary-core outcomes. The structured clone family provides an exact classification and demonstrates the strongest possible limiting separation (fraction tending to zero) while controlling Pareto efficiency. It is an exact self-contained combinatorial result with clear elections-theory relevance, not a generic claim about random elections or arbitrary profiles.

The dated certificate retains the supplied scientific assessment, sources and limitations.
