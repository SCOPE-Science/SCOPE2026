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

For fixed failed e=xy, the resistance is the supremum over voltage potentials p of 2(p_x−p_y)−Σ_{d≠e}w_d(p_{d+}−p_{d−})² (complete the square around the unit-current solution). This independently gives convexity in w. The worst case is convex and invariant under the cost-preserving group, so averaging gives a symmetric design no worse than any independent allocation. A vanishing weight sends the mate-deletion resistance to infinity, since the mate deletion leaves that current terminal attached by the vanishing conductance alone. In the averaged design the surviving mate is in series with the other routes in parallel, giving 1/a+2/((m−2)a+b) or 1/b+2/((m−1)a). With A=m−1, d=m−2 and r=b/a, the scaled branch difference has sign r−1 because A(d+r)−2r=Ad+(m−3)r>0. Derivatives of the budget-scaled active branches on r≥1 and r≤1 are respectively t+(2td−2A)/(d+r)² and 2t/A−A/r². The first derivative has the sign of t[(d+r)²+2d]−2A, strictly increasing as a sign numerator; the second is strictly increasing. Evaluating signs at r=1 yields t_−=2A/(m²−3), t_+=A²/2 with t_−<t_+ (A≥2 and m²−3≥6); thus the unique minima of the two half-intervals combine to exactly the three stated branches, including both endpoints of the plateau. The stated a,b and D follow by substitution. At m=3, B=1 the exact three example resistances are 8,12,36. The statement supplies an unrestricted optimum value and an attaining symmetric design, not a classification of all asymmetric optima.

## originality

PASS

Worst-outage resistance allocation and even an equal-conductance plateau are present in nearby work. The distinct supported contribution is the exact transition law for single-deletion endpoint resistance on the two-hub family, including both out-of-plateau ratios. Neither a general robustness formulation nor the even-cycle outage sum supplies it.

## value

PASS

Parallel two-hop routes are a natural model where loss of an edge changes both where the terminal is attached and which complete route is available. The exact transition is the value: equal conductances remain optimal across a price interval whose multiplicative width grows as m³/4, yet conductance moves in opposite directions outside it. Standard convexity alone predicts none of these thresholds or that growing price tolerance.

The dated certificate retains the supplied scientific assessment, sources and limitations.
